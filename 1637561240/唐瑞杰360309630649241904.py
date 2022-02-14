import opt
import math as m

def attact_control_speed(angle):
    """
    :param angle: 坦克与足球夹角，范围为[0,360], 逆时针方向
    :return: [垂直速度，水平速度]
    """
    # 45°至135°，足球在坦克左方
    if 45 < angle <= 135:
        vs, hs = 0.3, -1    # vertical_speed, horizontal_speed
    # 135°至225°，足球在坦克后方
    elif 135 < angle <= 225:
        vs, hs = -1, 0
    # 225°至315°，足球在坦克右方
    elif 225 < angle <= 315:
        vs, hs = 0.3, 1
    else:   # 315°至45°，足球在坦克正前方
        vs, hs = 1, 0
    return vs, hs  # vertical_speed, horizontal_speed

def attack():
    """
    坦克的策略函数，函数内需要实现此坦克的在每一帧的行为策略。
    使用opt库，获得场上比赛状态，根据状态施加你的自定义策略。
    该函数将会在比赛中的每一帧重复调用，直到比赛结束。
    :return: 当前状态下，当前坦克的操控值（前后速度，左右速度）
    """
    target_x = opt.BALL.x
    target_y = opt.BALL.y

    if not opt.TANK.is_ball_in_range(2):
        # 如果坦克-足球的直线距离较大，选择追击足球
        tank_angle_to_football = opt.TANK.angle_to(target_x, target_y)
        #print(tank_angle_to_football)
        # 根据相对角度计算 前后速度（v）和左右速度(h)
        vs, hs = attact_control_speed(tank_angle_to_football)
    else:
        # 如果坦克-足球的直线距离较小，微调位置进行进攻
        # 我们提供了根据球门，球和坦克的角度信息，判断是否有利于攻击的函数
        if opt.TANK.on_east_of(opt.BALL):
            # 若不利于进攻，输出需要调整到的目标方位
            target_x, target_y = opt.BALL.x - 3, opt.BALL.y
        tank_angle_to_football = opt.TANK.angle_to(target_x, target_y)
        vs, hs = attact_control_speed(tank_angle_to_football)
    return vs, hs

def face_to(angle):
    if 10 <= angle <= 180:
        vs, hs = 0.1, -1
    elif 180 < angle <= 350:
        vs, hs = 0.1, 1
    else:
        vs, hs = 1,0
    return vs, hs

def fire():
    angle = opt.TANK.angle_to(opt.BALL.x, opt.BALL.y)
    if opt.BALL.x-opt.TANK.x == 0:
        rng = 1000
    else:
        rng = (50-opt.TANK.x)*(opt.BALL.y-opt.TANK.y)/(opt.BALL.x-opt.TANK.x)+opt.TANK.y
    if -8<=rng<=8:
        if opt.TANK.on_west_of(opt.BALL) and opt.TANK.x > 0:
            if angle<5 or angle>355:
                opt.TANK.do_fire()

# -180 < r <= 180
def goto_right_slow(x, y, r):
    if opt.TANK.distance_to(x,y)<1:
        jiedian = [5, 180, -180, -5]
        jd = list(map(lambda x:x+r if 180>=x+r>=-180 else (x+r+360 if x+r<-180 else x+r-360), jiedian))
        if jd[0]<=opt.r2a(opt.TANK.r)<=jd[1] or \
           (jd[0]<=opt.r2a(opt.TANK.r)<=180 or -180<opt.r2a(opt.TANK.r)<=jd[1]) and jd[0]>jd[1]:
            vs, hs = 0.1, 1
            #print('111', vs, hs, opt.TANK.x, opt.TANK.y,opt.TANK.vx,opt.TANK.vy, opt.r2a(opt.TANK.r), opt.r2a(opt.TANK.vr))            
        elif jd[2]<opt.r2a(opt.TANK.r)<=jd[3] or \
             (jd[2]<opt.r2a(opt.TANK.r)<=180 or -180<opt.r2a(opt.TANK.r)<=jd[3]) and jd[2]>jd[3]:
            vs, hs = 0.1, -1
            #print('222', vs, hs, opt.TANK.x, opt.TANK.y,opt.TANK.vx,opt.TANK.vy, opt.r2a(opt.TANK.r), opt.r2a(opt.TANK.vr))
        else:
            if 45<r<135 or -135<r<-45:
                if opt.TANK.y-y>1:
                    vs, hs = -0.1,0
                    #print('333', vs, hs, opt.TANK.x, opt.TANK.y,opt.TANK.vx,opt.TANK.vy, opt.r2a(opt.TANK.r), opt.r2a(opt.TANK.vr))
                elif opt.TANK.y-y<-1:
                    vs, hs = 0.1,0
                    #print('444', vs, hs, opt.TANK.x, opt.TANK.y,opt.TANK.vx,opt.TANK.vy, opt.r2a(opt.TANK.r), opt.r2a(opt.TANK.vr))
                else:
                    vs, hs = 0,0
                    #print('555', vs, hs, opt.TANK.x, opt.TANK.y,opt.TANK.vx,opt.TANK.vy, opt.r2a(opt.TANK.r), opt.r2a(opt.TANK.vr))            
            else:
                if opt.TANK.x-x>1:
                    vs, hs = -0.1,0
                    #print('666', vs, hs, opt.TANK.x, opt.TANK.y,opt.TANK.vx,opt.TANK.vy, opt.r2a(opt.TANK.r), opt.r2a(opt.TANK.vr))
                elif opt.TANK.x-x<-1:
                    vs, hs = 0.1,0
                    #print('777', vs, hs, opt.TANK.x, opt.TANK.y,opt.TANK.vx,opt.TANK.vy, opt.r2a(opt.TANK.r), opt.r2a(opt.TANK.vr))
                else:
                    vs, hs = 0,0
                    #print('888', vs, hs, opt.TANK.x, opt.TANK.y,opt.TANK.vx,opt.TANK.vy, opt.r2a(opt.TANK.r), opt.r2a(opt.TANK.vr))            
    else:
        vs, hs = opt.TANK.goto(x,y)
        #print('999', vs, hs, opt.TANK.x, opt.TANK.y,opt.TANK.vx,opt.TANK.vy, opt.r2a(opt.TANK.r), opt.r2a(opt.TANK.vr))
    return vs, hs

# -180 < r <= 180
def goto_right_fast(x, y, r):
    if opt.TANK.distance_to(x,y)<2:
        jiedian = [45, 180, -180, -45]
        jd = list(map(lambda x:x+r if 180>=x+r>=-180 else (x+r+360 if x+r<-180 else x+r-360), jiedian))
        if jd[0]<=opt.r2a(opt.TANK.r)<=jd[1] or \
           (jd[0]<=opt.r2a(opt.TANK.r)<=180 or -180<opt.r2a(opt.TANK.r)<=jd[1]) and jd[0]>jd[1]:
            vs, hs = 0.1, 1
            #print('111', vs, hs, opt.TANK.x, opt.TANK.y,opt.TANK.vx,opt.TANK.vy, opt.r2a(opt.TANK.r), opt.r2a(opt.TANK.vr))            
        elif jd[2]<opt.r2a(opt.TANK.r)<=jd[3] or \
             (jd[2]<opt.r2a(opt.TANK.r)<=180 or -180<opt.r2a(opt.TANK.r)<=jd[3]) and jd[2]>jd[3]:
            vs, hs = 0.1, -1
            #print('222', vs, hs, opt.TANK.x, opt.TANK.y,opt.TANK.vx,opt.TANK.vy, opt.r2a(opt.TANK.r), opt.r2a(opt.TANK.vr))
        else:
            if 45<r<135 or -135<r<-45:
                if opt.TANK.y-y>1:
                    vs, hs = -0.1,0
                    #print('333', vs, hs, opt.TANK.x, opt.TANK.y,opt.TANK.vx,opt.TANK.vy, opt.r2a(opt.TANK.r), opt.r2a(opt.TANK.vr))
                elif opt.TANK.y-y<-1:
                    vs, hs = 0.1,0
                    #print('444', vs, hs, opt.TANK.x, opt.TANK.y,opt.TANK.vx,opt.TANK.vy, opt.r2a(opt.TANK.r), opt.r2a(opt.TANK.vr))
                else:
                    vs, hs = 0,0
                    #print('555', vs, hs, opt.TANK.x, opt.TANK.y,opt.TANK.vx,opt.TANK.vy, opt.r2a(opt.TANK.r), opt.r2a(opt.TANK.vr))            
            else:
                if opt.TANK.x-x>1:
                    vs, hs = -0.1,0
                    #print('666', vs, hs, opt.TANK.x, opt.TANK.y,opt.TANK.vx,opt.TANK.vy, opt.r2a(opt.TANK.r), opt.r2a(opt.TANK.vr))
                elif opt.TANK.x-x<-1:
                    vs, hs = 0.1,0
                    #print('777', vs, hs, opt.TANK.x, opt.TANK.y,opt.TANK.vx,opt.TANK.vy, opt.r2a(opt.TANK.r), opt.r2a(opt.TANK.vr))
                else:
                    vs, hs = 0,0
                    #print('888', vs, hs, opt.TANK.x, opt.TANK.y,opt.TANK.vx,opt.TANK.vy, opt.r2a(opt.TANK.r), opt.r2a(opt.TANK.vr))            
    else:
        vs, hs = opt.TANK.goto(x,y)
        #print('999', vs, hs, opt.TANK.x, opt.TANK.y,opt.TANK.vx,opt.TANK.vy, opt.r2a(opt.TANK.r), opt.r2a(opt.TANK.vr))
    return vs, hs


def choose_tank(x,y):
    d=[]
    friends = opt.my_other_tanks()
    d.append(friends[0].distance_to(x, y))
    d.append(friends[1].distance_to(x, y))
    d.append(friends[2].distance_to(x, y))
    d.append(friends[3].distance_to(x, y))
    d.append(opt.TANK.distance_to(x, y))
    if min(d[:4]) > d[4]:
        return True
    return False

def choose_enemy(x, y):
    d = []
    enemy = opt.enemy_tanks()
    d.append(enemy[0].distance_to(x, y))
    d.append(enemy[1].distance_to(x, y))
    d.append(enemy[2].distance_to(x, y))
    d.append(enemy[3].distance_to(x, y))
    d.append(enemy[4].distance_to(x, y))    
    return d.index(min(d))

l_x = 0
l_y = 0
flag5 = 0 #判断面对大脚远射，守门员是否已准备好
def defence():
    """
    坦克的策略函数，函数内需要实现此坦克的在每一帧的行为策略。
    使用opt库，获得场上比赛状态，根据状态施加你的自定义策略。
    该函数将会在比赛中的每一帧重复调用，直到比赛结束。
    :return: 当前状态下，当前坦克的操控值（前后速度，左右速度）
    """
    # 如果球在靠球门上半部分
    global flag5
    global l_x, l_y
    if l_x == opt.BALL.x:
        k = opt.BALL.y
    else:
        k = l_y-(l_y-opt.BALL.y)*(l_x+50)/(l_x-opt.BALL.x)

    # 上方角球
    if opt.BALL.x + 50 < 1 and opt.BALL.y > 8:
        if -1<opt.TANK.x+50<1 and -1<opt.TANK.y-8<1 and 0<1.57-opt.TANK.r<=0.1:
            vs, hs = 0,0
            #print('111111', opt.TANK.vx, opt.TANK.vy, opt.TANK.vr, opt.TANK.x, opt.TANK.y, opt.r2a(opt.TANK.r))
        else:
            vs, hs = goto_right_slow(-52, 6, 100)
            #print('222222', opt.TANK.vx, opt.TANK.vy, opt.TANK.vr, opt.TANK.x, opt.TANK.y, opt.r2a(opt.TANK.r))
    # 下方角球
    elif opt.BALL.x + 50 < 1 and opt.BALL.y < -8:
        if -1<opt.TANK.x+50<1 and -9<opt.TANK.y<-7 and 0<opt.TANK.r+1.57<=0.1:
            vs, hs = 0,0
            #print('333333', opt.TANK.vx, opt.TANK.vy, opt.TANK.vr, opt.TANK.x, opt.TANK.y, opt.r2a(opt.TANK.r))
        else:
            vs, hs = goto_right_slow(-52, -6, -100)
            #print('444444', opt.TANK.vx, opt.TANK.vy, opt.TANK.vr, opt.TANK.x, opt.TANK.y, opt.r2a(opt.TANK.r))
    # 接近球门    
    elif (opt.BALL.x+50 < 10 and -8<=opt.BALL.y<=8) or \
       (opt.BALL.distance_to(-50, 8) < 10 ) or \
       (opt.BALL.distance_to(-50,-8) < 10):
        vs, hs = opt.TANK.chase_ball()
        #print('555555', opt.TANK.vx, opt.TANK.vy, opt.TANK.vr, opt.TANK.x, opt.TANK.y, opt.r2a(opt.TANK.r))
    # 大脚远射
    elif flag5==1:
        vs, hs = opt.TANK.chase_ball()
        if opt.TANK.distance_to(-50,0) >0:
            flag5=0
    elif l_x-opt.BALL.x>0.1 and -8<k<8:
        n = l_y-(l_y-opt.BALL.y)*(l_x+45)/(l_x-opt.BALL.x)
        n = round(n, 1)
        degree = opt.relative_angle(-45, n, 0, opt.BALL.x, opt.BALL.y)
        degree = degree if degree<=180 else degree-360
        if opt.r2a(opt.TANK.r)>degree+5:
            new_n = n-2
        elif opt.r2a(opt.TANK.r)<degree-5:
            new_n = n+2
        else:
            new_n = n
        if opt.TANK.distance_to(opt.BALL.x, opt.BALL.y)>30:
            vs, hs = goto_right_slow(-45, new_n, degree)
        else:
            vs, hs = goto_right_fast(-45, new_n, degree)
        if vs==0 and hs==0:
            flag5 = 1
        #print('大脚远射',opt.BALL.x,opt.BALL.y,l_x, l_y,l_x-opt.BALL.x,opt.TANK.x,opt.TANK.y,opt.TANK.r,k,opt.remaining_time(),n, new_n, degree)
        #print('666666', opt.TANK.vx, opt.TANK.vy, opt.TANK.vr, opt.TANK.x, opt.TANK.y, opt.r2a(opt.TANK.r))
    # 回防
    elif opt.TANK.distance_to(-50,0)> 10 and opt.TANK.distance_to(-50,8) >10 and \
         opt.TANK.distance_to(-50, -8) > 10:
        vs, hs = opt.TANK.goto(-50, 0)
        #print('777777', opt.TANK.vx, opt.TANK.vy, opt.TANK.vr, opt.TANK.x, opt.TANK.y, opt.r2a(opt.TANK.r))
        if opt.TANK.is_stuck():
            vs, hs = -1,0
            #print('888888', opt.TANK.vx, opt.TANK.vy, opt.TANK.vr, opt.TANK.x, opt.TANK.y, opt.r2a(opt.TANK.r))
    # 其他
    else:
        if opt.TANK.distance_to(-50, 0) > 2:
            vs, hs = opt.TANK.goto(-50, 0)
            #print('999999', opt.TANK.vx, opt.TANK.vy, opt.TANK.vr, opt.TANK.x, opt.TANK.y, opt.r2a(opt.TANK.r))
        elif -0.5<opt.r2a(opt.TANK.r)<0.5:
            vs, hs = 0, 0
            #print('aaaaaa', opt.TANK.vx, opt.TANK.vy, opt.TANK.vr, opt.TANK.x, opt.TANK.y, opt.r2a(opt.TANK.r))
        else:
            if opt.r2a(opt.TANK.r) > 0.5:
                vs, hs = 0.1, 0.1
                #print('bbbbb', opt.TANK.vx, opt.TANK.vy, opt.TANK.vr, opt.TANK.x, opt.TANK.y, opt.r2a(opt.TANK.r))
            else:
                vs, hs = 0.1, -0.1
                #print('cccccc', opt.TANK.vx, opt.TANK.vy, opt.TANK.vr, opt.TANK.x, opt.TANK.y, opt.r2a(opt.TANK.r))
    #print("uuuuuu", l_x-opt.BALL.x, k)
    l_x = opt.BALL.x
    l_y = opt.BALL.y
    #print('tttttt', vs, hs, opt.r2a(opt.TANK.r), opt.TANK.vr, opt.TANK.x, opt.TANK.y, opt.score())
    
    return vs, hs
def leave_forbidden_zone(vs,hs):
    if opt.BALL.x<-45 and -12<opt.BALL.y<12 and \
       opt.TANK.x<-45 and -12<opt.TANK.y<12:
        print('ball.x =',opt.BALL.x,'ball.y =',opt.BALL.y,'tank.x =',opt.TANK.x,'tank.y =',opt.TANK.y)
        return 0,0
    else:
        return vs,hs

def start_way1(x,y):
    vs = 1
    angle = opt.TANK.angle_to(x, y)
    a = 38  #(0~45)
    if 180 < angle <= 360-a:
        hs = 1
    elif angle < 180:
        hs = -0.1
    else:
        hs = 0
    return vs,hs

def start_way2(x,y):
    vs = 1
    angle = opt.TANK.angle_to(x, y)
    a = 40  #(0~45)
    if a < angle <= 180:
        hs = -1
    elif angle > 180:
        hs = 0.1
    else:
        hs = 0
    return vs,hs

x, y = 0,0 #保存ball初始位置
flag12 = 0
def tank1_update():
    """
    坦克1的策略函数，函数内需要实现此坦克的在每一帧的行为策略。
    使用opt库，获得场上比赛状态，根据状态施加你的自定义策略。
    该函数将会在比赛中的每一帧重复调用，直到比赛结束。
    :return: 当前状态下，当前坦克的操控值（前后速度，左右速度）
    """
    global x
    global y

    if opt.TANK.x ==-12.5 and opt.TANK.y == 12.5:
        x = opt.BALL.x
        y = opt.BALL.y
    fire()
    if opt.TANK.is_stuck():
        return leave_forbidden_zone(-1, 0)
    if opt.BALL.x<-48 and opt.TANK.x<-48:
        if opt.TANK.on_north_of(opt.BALL) and opt.BALL.y>0:
            vs, hs = -1, 0
            #print("+++",opt.BALL.x,opt.BALL.y,opt.BALL.vx,opt.BALL.vy,opt.TANK.x,opt.TANK.y,opt.TANK.vx, opt.TANK.vy)
        elif opt.TANK.on_south_of(opt.BALL) and opt.BALL.y<0:
            vs, hs = -1,0
            #print("---",opt.BALL.x,opt.BALL.y,opt.BALL.vx,opt.BALL.vy,opt.TANK.x,opt.TANK.y,opt.TANK.vx, opt.TANK.vy)
    if opt.BALL.x>48 and opt.TANK.x>48:
        if opt.TANK.on_north_of(opt.BALL) and opt.BALL.y<0:
            vs, hs = -1, 0
            #print("***",opt.BALL.x,opt.BALL.y,opt.BALL.vx,opt.BALL.vy,opt.TANK.x,opt.TANK.y,opt.TANK.vx, opt.TANK.vy)
        elif opt.TANK.on_south_of(opt.BALL) and opt.BALL.y>0:
            vs, hs = -1,0
            #print("///",opt.BALL.x,opt.BALL.y,opt.BALL.vx,opt.BALL.vy,opt.TANK.x,opt.TANK.y,opt.TANK.vx, opt.TANK.vy)
    #print("^^^",opt.BALL.x,opt.BALL.y,opt.BALL.vx,opt.BALL.vy,opt.TANK.x,opt.TANK.y,opt.TANK.vx, opt.TANK.vy)
    if x == opt.BALL.x and y == opt.BALL.y:
        if flag12==1:
            vs, hs = 1,0
        else:
            #vs, hs = opt.TANK.chase_ball()
            #vs, hs = opt.TANK.goto(x, y)
            vs, hs = start_way1(x,y)
            #print("tank_1",'x=',opt.TANK.x,'y=',opt.TANK.y,'r=',opt.r2a(opt.TANK.r),'vs=',vs,'hs=',hs,'vx=',opt.TANK.vx,'vy=',opt.TANK.vy,'vr=',opt.TANK.vr)
            #enemy1 = opt.enemy_tanks()[0]
            #print("enemy1",'x=',enemy1.x,'y=',enemy1.y,'r=',opt.r2a(enemy1.r),'vx=',enemy1.vx,'vy=',enemy1.vy,'vr=',enemy1.vr)
        return vs, hs
    else:
        if opt.BALL.x > 48 and choose_tank(45,0):
            if opt.BALL.y < -8 or opt.BALL.y > 8:
                vs, hs = goto_right_fast(45, 0, 0)
                return vs, hs
            else:
                if -45<opt.r2a(opt.TANK.r)<45 and \
                    (0<opt.BALL.y-5*m.tan(opt.TANK.r)<5 or -5<opt.BALL.y-5*m.tan(opt.TANK.r)<0):
                    vs, hs = 1,0
                else:
                    vs, hs = goto_right_fast(45, 0, 0)
            return vs, hs
        else:        
            if opt.TANK.on_east_of(opt.BALL):
                # 若不利于进攻，输出需要调整到的目标方位
                target_x = opt.BALL.x - 3
                if opt.BALL.y>0:
                    target_y = opt.BALL.y - 3
                else:
                    target_y = opt.BALL.y + 3
                vs, hs = opt.TANK.goto(target_x, target_y)
            else:
                vs, hs = attack()
            return leave_forbidden_zone(vs, hs)

def tank2_update():
    global flag2
    fire()
    if opt.TANK.is_stuck():
        return leave_forbidden_zone(-1, 0)
    if opt.BALL.x<-48 and opt.TANK.x<-48:
        if opt.TANK.on_north_of(opt.BALL) and opt.BALL.y>0:
            vs, hs = -1, 0
            #print("+++",opt.BALL.x,opt.BALL.y,opt.BALL.vx,opt.BALL.vy,opt.TANK.x,opt.TANK.y,opt.TANK.vx, opt.TANK.vy)
        elif opt.TANK.on_south_of(opt.BALL) and opt.BALL.y<0:
            vs, hs = -1,0
            #print("---",opt.BALL.x,opt.BALL.y,opt.BALL.vx,opt.BALL.vy,opt.TANK.x,opt.TANK.y,opt.TANK.vx, opt.TANK.vy)
    if opt.BALL.x>48 and opt.TANK.x>48:
        if opt.TANK.on_north_of(opt.BALL) and opt.BALL.y<0:
            vs, hs = -1, 0
            #print("***",opt.BALL.x,opt.BALL.y,opt.BALL.vx,opt.BALL.vy,opt.TANK.x,opt.TANK.y,opt.TANK.vx, opt.TANK.vy)
        elif opt.TANK.on_south_of(opt.BALL) and opt.BALL.y>0:
            vs, hs = -1,0
            #print("///",opt.BALL.x,opt.BALL.y,opt.BALL.vx,opt.BALL.vy,opt.TANK.x,opt.TANK.y,opt.TANK.vx, opt.TANK.vy) 
    #print("^^^",opt.BALL.x,opt.BALL.y,opt.BALL.vx,opt.BALL.vy,opt.TANK.x,opt.TANK.y,opt.TANK.vx,opt.TANK.vy)
    if x == opt.BALL.x and y == opt.BALL.y:
        if flag12==1:
            vs, hs = 1,0
        else:
            #vs, hs = opt.TANK.chase_ball()
            #vs, hs = opt.TANK.goto(x,y)
            vs, hs = start_way2(x,y)
            #print("tank_2",'x=',opt.TANK.x,'y=',opt.TANK.y,'r=',opt.r2a(opt.TANK.r),'vs=',vs,'hs=',hs,'vx=',opt.TANK.vx,'vy=',opt.TANK.vy,'vr=',opt.TANK.vr)
            #enemy2 = opt.enemy_tanks()[1]
            #print("enemy2",'x=',enemy2.x,'y=',enemy2.y,'r=',opt.r2a(enemy2.r),'vx=',enemy2.vx,'vy=',enemy2.vy,'vr=',enemy2.vr)
        return vs, hs
    else:
        if opt.BALL.x > 48 and choose_tank(45,0):
            if opt.BALL.y < -8 or opt.BALL.y > 8:
                vs, hs = goto_right_fast(45, 0, 0)
                return vs, hs
            else:
                if -45<opt.r2a(opt.TANK.r)<45 and \
                    (0<opt.BALL.y-5*m.tan(opt.TANK.r)<5 or -5<opt.BALL.y-5*m.tan(opt.TANK.r)<0):
                    vs, hs = 1,0
                else:
                    vs, hs = goto_right_fast(45, 0, 0)
            return vs, hs
        else:
            if opt.TANK.on_east_of(opt.BALL):
                # 若不利于进攻，输出需要调整到的目标方位
                target_x = opt.BALL.x - 3
                if opt.BALL.y>0:
                    target_y = opt.BALL.y - 3
                else:
                    target_y = opt.BALL.y + 3
                vs, hs = opt.TANK.goto(target_x, target_y)
            else:
                vs, hs = opt.TANK.chase_ball()
            return leave_forbidden_zone(vs, hs)
        #return attack()

def tank3_update():
    """
    坦克3的策略函数，函数内需要实现此坦克的在每一帧的行为策略。
    使用opt库，获得场上比赛状态，根据状态施加你的自定义策略。
    该函数将会在比赛中的每一帧重复调用，直到比赛结束。
    :return: 当前状态下，当前坦克的操控值（前后速度，左右速度）
    """
    fire()
    if (opt.TANK.angle_to(opt.BALL.x, opt.BALL.y)<5 or \
       opt.TANK.angle_to(opt.BALL.x, opt.BALL.y)>355) and \
       opt.TANK.vx ==0 and opt.TANK.vy==0 and opt.TANK.vr==0:
       #print(opt.TANK.angle_to(opt.BALL.x, opt.BALL.y), opt.score())
       return leave_forbidden_zone(1,0)

    if opt.TANK.is_stuck():
        return leave_forbidden_zone(-1, 0)
    if opt.BALL.x<-48 and opt.TANK.x<-48:
        if opt.TANK.on_north_of(opt.BALL) and opt.BALL.y>0:
            vs, hs = -1, 0
            #print("+++",opt.BALL.x,opt.BALL.y,opt.BALL.vx,opt.BALL.vy,opt.TANK.x,opt.TANK.y,opt.TANK.vx, opt.TANK.vy)
        elif opt.TANK.on_south_of(opt.BALL) and opt.BALL.y<0:
            vs, hs = -1,0
            #print('---',opt.BALL.x,opt.BALL.y,opt.BALL.vx,opt.BALL.vy,opt.TANK.x,opt.TANK.y,opt.TANK.vx, opt.TANK.vy)
    if opt.BALL.x>48 and opt.TANK.x>48:
        if opt.TANK.on_north_of(opt.BALL) and opt.BALL.y<0:
            vs, hs = -1, 0
            #print("***",opt.BALL.x,opt.BALL.y,opt.BALL.vx,opt.BALL.vy,opt.TANK.x,opt.TANK.y,opt.TANK.vx, opt.TANK.vy)
        elif opt.TANK.on_south_of(opt.BALL) and opt.BALL.y>0:
            vs, hs = -1,0
            #print("///",opt.BALL.x,opt.BALL.y,opt.BALL.vx,opt.BALL.vy,opt.TANK.x,opt.TANK.y,opt.TANK.vx, opt.TANK.vy)       
    #print("^^^",opt.BALL.x,opt.BALL.y,opt.BALL.vx,opt.BALL.vy,opt.TANK.x,opt.TANK.y,opt.TANK.vx, opt.TANK.vy)
    if opt.BALL.x > 48 and choose_tank(45,0):
        if opt.BALL.y < -8 or opt.BALL.y > 8:
            vs, hs = goto_right_fast(45, 0, 0)
            return vs, hs
        else:
            if -45<opt.r2a(opt.TANK.r)<45 and \
                (0<opt.BALL.y-5*m.tan(opt.TANK.r)<5 or -5<opt.BALL.y-5*m.tan(opt.TANK.r)<0):
                vs, hs = 1,0
            else:
                vs, hs = goto_right_fast(45, 0, 0)
            return vs, hs
    else:
        if opt.TANK.on_east_of(opt.BALL):
            # 若不利于进攻，输出需要调整到的目标方位
            target_x = opt.BALL.x - 3
            if opt.BALL.y>0:
                target_y = opt.BALL.y - 3
            else:
                target_y = opt.BALL.y + 3
            vs, hs = opt.TANK.goto(target_x, target_y)
        else:
            vs, hs = attack()
        return leave_forbidden_zone(vs, hs)

def tank4_update():
    """
    坦克4的策略函数，函数内需要实现此坦克的在每一帧的行为策略。
    使用opt库，获得场上比赛状态，根据状态施加你的自定义策略。
    该函数将会在比赛中的每一帧重复调用，直到比赛结束。
    :return: 当前状态下，当前坦克的操控值（前后速度，左右速度）
    """
    fire()
    if (opt.TANK.angle_to(opt.BALL.x, opt.BALL.y)<5 or \
       opt.TANK.angle_to(opt.BALL.x, opt.BALL.y)>355) and \
       opt.TANK.vx ==0 and opt.TANK.vy==0 and opt.TANK.vr==0:
        #print(opt.TANK.angle_to(opt.BALL.x, opt.BALL.y), opt.score())
        return leave_forbidden_zone(1,0)

    if opt.TANK.is_stuck():
        return leave_forbidden_zone(-1, 0)
    if opt.BALL.x<-48 and opt.TANK.x<-48:
        if opt.TANK.on_north_of(opt.BALL) and opt.BALL.y>0:
            vs, hs = -1, 0
            #print("+++",opt.BALL.x,opt.BALL.y,opt.BALL.vx,opt.BALL.vy,opt.TANK.x,opt.TANK.y,opt.TANK.vx, opt.TANK.vy)
        elif opt.TANK.on_south_of(opt.BALL) and opt.BALL.y<0:
            vs, hs = -1,0
            #print("---",opt.BALL.x,opt.BALL.y,opt.BALL.vx,opt.BALL.vy,opt.TANK.x,opt.TANK.y,opt.TANK.vx, opt.TANK.vy)
    elif opt.BALL.x>48 and opt.TANK.x>48:
        if opt.TANK.on_north_of(opt.BALL) and opt.BALL.y<0:
            vs, hs = -1, 0
            #print("***",opt.BALL.x,opt.BALL.y,opt.BALL.vx,opt.BALL.vy,opt.TANK.x,opt.TANK.y,opt.TANK.vx, opt.TANK.vy)
        elif opt.TANK.on_south_of(opt.BALL) and opt.BALL.y>0:
            vs, hs = -1,0
            #print("///",opt.BALL.x,opt.BALL.y,opt.BALL.vx,opt.BALL.vy,opt.TANK.x,opt.TANK.y,opt.TANK.vx, opt.TANK.vy)      
    #print("^^^",opt.BALL.x,opt.BALL.y,opt.BALL.vx,opt.BALL.vy,opt.TANK.x,opt.TANK.y,opt.TANK.vx, opt.TANK.vy)
    if opt.BALL.x > 48 and choose_tank(45,0):
        if opt.BALL.y < -8 or opt.BALL.y > 8:
            vs, hs = goto_right_fast(45, 0, 0)
            return vs, hs
        else:
            if -45<opt.r2a(opt.TANK.r)<45 and \
                (0<opt.BALL.y-5*m.tan(opt.TANK.r)<5 or -5<opt.BALL.y-5*m.tan(opt.TANK.r)<0):
                vs, hs = 1,0
            else:
                vs, hs = goto_right_fast(45, 0, 0)
            return vs, hs
    else:
        if opt.TANK.on_east_of(opt.BALL):
            # 若不利于进攻，输出需要调整到的目标方位
            target_x = opt.BALL.x - 3
            if opt.BALL.y>0:
                target_y = opt.BALL.y - 3
            else:
                target_y = opt.BALL.y + 3
            vs, hs = opt.TANK.goto(target_x, target_y)
        else:
            vs, hs = attack()
        return leave_forbidden_zone(vs, hs)

def min_distance():
    my_friends = []
    my_enemys = []
    for i in range(4):
        my_friends.append(opt.TANK.distance_to(opt.my_other_tanks()[i].x, opt.my_other_tanks()[i].y))
    for i in range(5):
        my_enemys.append(opt.TANK.distance_to(opt.enemy_tanks()[i].x, opt.enemy_tanks()[i].y))
    m_f = min(my_friends)
    m_e = min(my_enemys)
    return min(m_f, m_e)

def avoid_stuck(vs, hs, l_vs):
    if l_vs > 0 and opt.TANK.vx<=0 and min_distance()<3 and opt.BALL.x>-48:
        print(min_distance())
        if opt.TANK.y<0:
            return -1, 0.1
        else:
            return -1,-0.1
    return vs, hs

l_vs=0
def tank5_update():
    """
    坦克5的策略函数，函数内需要实现此坦克的在每一帧的行为策略。
    使用opt库，获得场上比赛状态，根据状态施加你的自定义策略。
    该函数将会在比赛中的每一帧重复调用，直到比赛结束。
    :return: 当前状态下，当前坦克的操控值（前后速度，左右速度）
    """
    global flag12
    global l_vs
    if x == opt.BALL.x and y == opt.BALL.y:
        if opt.TANK.cool_remain==0:
            flag12 = 1
            vs=0.1
            if 180>=opt.TANK.angle_to(x,y)>0.1:
                hs=-0.1
            elif 180<opt.TANK.angle_to(x,y)<359.9:
                hs=0.1     
            else:
                if 0.5>=opt.TANK.angle_to(x, y)>0:
                    hs=-0.1
                elif 359.5<=opt.TANK.angle_to(x, y)<360:
                    hs=0.1
                else:
                    hs=0
                opt.TANK.do_fire()
            #print('zzz', x, y, opt.TANK.angle_to(x, y), vs, hs, opt.TANK.cool_remain, opt.score(), opt.remaining_time())
            return vs, hs
        else:
            return 0,0
    else:
        flag12 = 0
        vs, hs = defence()
        vs, hs = avoid_stuck(vs, hs, l_vs)
        l_vs = vs
        return vs, hs