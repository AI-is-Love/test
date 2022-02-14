import opt
import math

#追球程序
def get_front(angle):
    if 10 > angle or angle> 350:
      vs, hs = 1,0
    elif 10 < angle <= 20:
      vs, hs = 1,-0.1
    elif 20 < angle <= 30:   # 45°至315°，足球不在坦克前方
      vs, hs = 1,-0.3
    elif 30 < angle <= 90:   # 45°至315°，足球不在坦克前方
      vs, hs = 1,-0.8
    elif 340 < angle <= 350:
      vs, hs = 1,0.1
    elif 330 < angle <= 340:   # 45°至315°，足球不在坦克前方
      vs, hs = 1,0.3
    elif 270 < angle <= 330:   # 45°至315°，足球不在坦克前方
      vs, hs = 1,0.8
    #球在坦克的后方
    elif 90 < angle <= 120:
      vs, hs = -1,1
    elif 120 < angle <= 150:
      vs, hs = -1,0.7
    elif 150 < angle <= 170:
      vs, hs = -1,0.3
    elif 170 < angle <= 180:
      vs, hs = -1,0.1
    elif 240 < angle <= 270:
      vs, hs = -1,-1
    elif 210 < angle <= 240:
      vs, hs = -1,-0.7
    elif 190 < angle <= 210:
      vs, hs = -1,-0.3
    elif 180 < angle <= 190:
      vs, hs = -1,-0.1
    else:
      vs, hs = 1,0
    return vs, hs  # vertical_speed, horizontal_speed
#获取足球的位置，进行编码 1 2 3 -1 -2 -3 4 5 6
def getBallPos(x,y):
    pos=0
    if x<=-30 and y>=10:
        pos = 1
    elif -30<=x<=30 and y>=10:
        pos = 2
    elif x>30 and y>=10:
        pos = 3
    elif x<=-30 and y<=-10:
        pos = -1
    elif -30<=x<=30 and y<=-10:
        pos = -2
    elif x>=30 and y<=-10:
        pos = -3
    elif -10<=y<=10 and x<=-30:
        pos = 4
    elif -10<=y<=10 and -30<=x<=30:
        pos = 5
    elif -10<=y<=10 and x>=30:
        pos = 6
    else:
        pos = 7
    return pos
    
def attack(Tank,Ball):
    #获取的坦克和球的位置坐标
    tank_x = Tank.x
    tank_y = Tank.y
    ball_x = Ball.x
    ball_y = Ball.y
    #获取的球的运动方向
    ball_angle = math.atan2(Ball.vy,Ball.vx)
    ball_angle = opt.r2a(ball_angle)
    tank_angle = Tank.angle
    if tank_angle<0:
        tank_angle = 360+tank_angle
    ball_offset = ball_y+(50-ball_x)*math.tan(ball_angle)
    #获取的坦克与球的距离和角度
    t2b_distance = Tank.distance_to(ball_x, ball_y) 
    t2b_angle = Tank.angle_to(ball_x, ball_y);
    #获取球的位置编码  1 2 3 -1 -2 -3 4 5 6
    pos = getBallPos(ball_x,ball_y)
    #坦克与球的角度与坦克的 角度差
    degree = t2b_angle-tank_angle
    #坦克与球的角度相差不大的判断条件
    flag = -15<degree<15 or 345<degree or degree<-345
    # if flag and opt.TANK.face_enemy_door(0) and (270<=tank_angle or tank_angle>=90):
    #     Tank.do_fire()   
    if   pos ==  1: #ok
        if  ball_x > tank_x +1.5:
            vs, hs = get_front(t2b_angle)
        elif ball_x < tank_x-1.5:
            vs, hs = opt.TANK.goto(-47,12)  
        elif ball_y >= tank_y:
            if flag: 
                Tank.do_fire()
            if t2b_distance<3:
                vs, hs = 1,1
            else:
                vs, hs = get_front(t2b_angle+20)  
        elif ball_y < tank_y:
            if t2b_distance<3:
                vs, hs = 1,-1
            else:
                vs, hs = get_front(t2b_angle-20)  
        else:
            vs, hs = get_front(t2b_angle)
    elif pos == -1: #ok
        if  ball_x > tank_x +1.5:
            vs, hs = get_front(t2b_angle)
        elif ball_x < tank_x-1.5:
            vs, hs = opt.TANK.goto(-47,-12) 
        elif ball_y >= tank_y:
            if t2b_distance<3:
                vs, hs = 1,1
            else:
                vs, hs = get_front(t2b_angle+20)  
        elif ball_y < tank_y:
            if flag: 
                Tank.do_fire()
            if t2b_distance<3:
                vs, hs = 1,-1
            else:
                vs, hs = get_front(t2b_angle-20)  
        else:
            vs, hs = get_front(t2b_angle)
    elif pos ==  4: #ok
        if  ball_x > tank_x +1.5:
            vs, hs = get_front(t2b_angle)
            if flag:
                Tank.do_fire()
        elif ball_x < tank_x-1.5:
            vs, hs = 0,0 
        else:
            vs, hs = get_front(t2b_angle)
    elif pos ==  2 or pos == -2: #ok
        if not opt.TANK.face_enemy_door(-2) and t2b_distance<2.6:
            if ball_angle>0:
                vs, hs = get_front(t2b_angle-50) 
            elif ball_angle<0:
                vs, hs = get_front(t2b_angle+50) 
            else:
                vs, hs = get_front(t2b_angle)   
        elif not opt.TANK.face_enemy_door(-2) and t2b_distance<10:
            if ball_angle>0:
                vs, hs = get_front(t2b_angle+20) 
                if flag: 
                    Tank.do_fire()
            elif ball_angle<0:
                vs, hs = get_front(t2b_angle-20) 
                if flag: 
                    Tank.do_fire()
            else:
                vs, hs = get_front(t2b_angle) 
        else: 
            vs, hs = get_front(t2b_angle)
    elif pos ==  5: #ok
        if  ball_x > tank_x +1.5:
            if not opt.TANK.face_enemy_door(-2) and t2b_distance<2.6:
                if ball_angle>0:
                    vs, hs = get_front(t2b_angle-50) 
                elif ball_angle<0:
                    vs, hs = get_front(t2b_angle+50) 
                else:
                    vs, hs = get_front(t2b_angle)   
            elif not opt.TANK.face_enemy_door(-2) and t2b_distance<10:
                if ball_angle>0:
                    vs, hs = get_front(t2b_angle+30) 
                    if degree<-3:
                        opt.TANK.do_fire()
                elif ball_angle<0:
                    vs, hs = get_front(t2b_angle-30) 
                    if degree>3:
                        opt.TANK.do_fire()
                else:
                    vs, hs = get_front(t2b_angle) 
            else: 
                vs, hs = get_front(t2b_angle) 
        elif ball_x < tank_x-1.5:
            if ball_x <-10 and -11<ball_offset<11:
                vs, hs =0,0
            else:
                if ball_angle>5:
                    vs, hs = get_front(t2b_angle+20)  
                elif ball_angle<-5:
                    vs, hs = get_front(t2b_angle-20)
                else:
                    vs, hs = get_front(t2b_angle)  
        elif ball_y >= tank_y:
            if t2b_distance<3:
                vs, hs = get_front(t2b_angle-20)
            else:
                vs, hs = get_front(t2b_angle+20)  
        elif ball_y < tank_y:
            if t2b_distance<3:
                vs, hs = get_front(t2b_angle+20)
            else:
                vs, hs = get_front(t2b_angle-20) 
        else:
            vs, hs = get_front(t2b_angle)
    elif pos ==  3: #ok
        if  ball_x > tank_x +1.5:
            if not opt.TANK.face_enemy_door(-2) and t2b_distance<2.6:
                vs, hs = get_front(t2b_angle-30)
            elif not opt.TANK.face_enemy_door(-2):
                vs, hs = get_front(t2b_angle+30)
                if degree<-3:
                    opt.TANK.do_fire()
            else:
                vs, hs = get_front(t2b_angle)
        elif ball_x < tank_x-1.5:
            if  -1<ball_y-tank_y<1:
                vs, hs =0,0
            else:
                vs, hs = get_front(t2b_angle+30)
            # vs, hs = opt.TANK.goto(ball_x-10,ball_y) 
        elif ball_y >= tank_y:
            vs, hs = opt.TANK.goto(30,22)   
        elif ball_y < tank_y:
            if not opt.TANK.face_enemy_door(-2) and t2b_distance<2.6:
                vs, hs = get_front(t2b_angle+30)
            elif not opt.TANK.face_enemy_door(-2):
                vs, hs = get_front(t2b_angle-30)
            else:
                vs, hs = get_front(t2b_angle) 
        else:
            vs, hs = get_front(t2b_angle)
    elif pos == -3: #ok
        if  ball_x > tank_x +1.5:
            if not opt.TANK.face_enemy_door(-2) and t2b_distance<2.6:
                vs, hs = get_front(t2b_angle+30)
            elif not opt.TANK.face_enemy_door(-2):
                vs, hs = get_front(t2b_angle-30)
                if degree>3:
                    opt.TANK.do_fire()
            else:
                vs, hs = get_front(t2b_angle)
        elif ball_x < tank_x-1.5:
            if  -1<ball_y-tank_y<1:
                vs, hs =0,0
            else:
                vs, hs = get_front(t2b_angle-30)
            # vs, hs = opt.TANK.goto(ball_x-10,ball_y) 
        elif ball_y >= tank_y:
            vs, hs = opt.TANK.goto(30,-22)   
        elif ball_y < tank_y:
            if not opt.TANK.face_enemy_door(-2) and t2b_distance<2.6:
                vs, hs = get_front(t2b_angle+30)
            elif not opt.TANK.face_enemy_door(-2):
                vs, hs = get_front(t2b_angle-30)
            else:
                vs, hs = get_front(t2b_angle) 
        else:
            vs, hs = get_front(t2b_angle)
    elif pos ==  6: #ok
        if  ball_x > tank_x +1.5:
            if not -5<ball_offset<5 and t2b_distance<2.6:
                if ball_angle>0:
                    vs, hs = get_front(t2b_angle-60)
                else:
                    vs, hs = get_front(t2b_angle+60)
            elif not -5<ball_offset<5:
                if ball_angle>0:
                    vs, hs = get_front(t2b_angle+30)
                    if degree<-3:
                        Tank.do_fire() 
                else:
                    vs, hs = get_front(t2b_angle-30)
                    if degree>3:
                        Tank.do_fire() 
            else:
                vs, hs = get_front(t2b_angle)
                Tank.do_fire() 
        elif ball_x < tank_x -1.5:
            if  -1<ball_y-tank_y<1:
                vs, hs = get_front(t2b_angle)
            else:
                if ball_angle>0:
                    vs, hs = get_front(t2b_angle-20)
                else:
                    vs, hs = get_front(t2b_angle+20)
        else:
            if t2b_distance<2.6:
                if ball_angle>=0:
                    if -9<=ball_y<=9:
                        vs, hs = get_front(t2b_angle-80)
                        # opt.TANK.do_fire()
                    else:
                        vs, hs = get_front(t2b_angle-10)
                elif ball_angle<0:
                    if -9<=ball_y<=9:
                        vs, hs = get_front(t2b_angle+80)
                        # opt.TANK.do_fire()
                    else:
                        vs, hs = get_front(t2b_angle+10)
                else:
                    vs, hs = get_front(t2b_angle)   
            elif t2b_distance<10:
                if ball_angle>=0:
                    vs, hs = get_front(t2b_angle+20)
                    if degree<-3: 
                        opt.TANK.do_fire() 
                elif ball_angle<0:
                    vs, hs = get_front(t2b_angle-20) 
                    if degree>3: 
                        opt.TANK.do_fire() 
                else:
                    vs, hs = get_front(t2b_angle) 
            else: 
                vs, hs = get_front(t2b_angle)
    else:
        vs, hs = get_front(t2b_angle)
    return  vs, hs

#坦克1进攻策略编写
def tank1_update():
    return  attack(opt.TANK,opt.BALL)
#坦克2进攻策略编写
def tank2_update():
    return  attack(opt.TANK,opt.BALL)
#坦克3进攻策略编写   
def tank3_update():
    return  attack(opt.TANK,opt.BALL)

#防守策略编写
stop1=0
stop2=0
def tank4_update():
    global stop1
    ball_x =  opt.BALL.x
    ball_y =  opt.BALL.y
    t2d_angle = opt.TANK.angle_to(50, 0);
    t2b_angle = opt.TANK.angle_to(ball_x, ball_y);
    vx=opt.BALL.vx
    vy=opt.BALL.vy
    speed = math.sqrt(vx*vx+vy*vy)
    tank_angle = opt.TANK.angle
    if tank_angle<0:
        tank_angle = 360+tank_angle
    degree = t2b_angle-tank_angle
    flag = -8<degree<8 or 356<degree or degree<-356
    if ball_x>0 and opt.TANK.face_enemy_door(-2):
        stop1=1
        if speed<5 and 8<=ball_y<=8:
            opt.TANK.do_fire() 
        elif speed>25 and 20<=ball_y<=20:
            opt.TANK.do_fire()
        elif -10*speed/12<=ball_y<=10*speed/12: 
            opt.TANK.do_fire()
    else:
        stop1=0
    if stop1==0:
        if flag and ball_x<-30:
            opt.TANK.do_fire()  
        if flag and ball_x<-30 and -11<=ball_y<=11:
            vs, hs = get_front(t2b_angle)
        elif opt.BALL.y >= 3:#上
            vs, hs = opt.TANK.goto(-50,5.9)
        elif -3<opt.BALL.y<3:#中
            vs, hs = opt.TANK.goto(-50, 2.5)  
        else: #下
            vs, hs = opt.TANK.goto(-50, -2)
    else:
        vs, hs = 0,0
    return vs, hs
def tank5_update():
    global stop2
    ball_x =  opt.BALL.x
    ball_y =  opt.BALL.y
    t2d_angle = opt.TANK.angle_to(50, 0);
    t2b_angle = opt.TANK.angle_to(ball_x, ball_y);
    vx=opt.BALL.vx
    vy=opt.BALL.vy
    speed = math.sqrt(vx*vx+vy*vy)
    tank_angle = opt.TANK.angle
    if tank_angle<0:
        tank_angle = 360+tank_angle
    degree = t2b_angle-tank_angle
    flag = -8<degree<8 or 356<degree or degree<-356
    flag = -8<degree<8 or 356<degree or degree<-356
    if ball_x>0 and opt.TANK.face_enemy_door(-2):
        stop2=1
        if speed<5 and 8<=ball_y<=8:
            opt.TANK.do_fire() 
        elif speed>25 and 20<=ball_y<=20:
            opt.TANK.do_fire()
        elif -10*speed/12<=ball_y<=10*speed/12: 
            opt.TANK.do_fire()
    else:
        stop2=0
    if stop2==0:  
        if flag and ball_x<-30:
            opt.TANK.do_fire() 
        if flag and ball_x<-30 and -11<=ball_y<=11:
            vs, hs = get_front(t2b_angle)
        elif opt.BALL.y >= 3:
            vs, hs = opt.TANK.goto(-50, 2) 
        elif -3<opt.BALL.y<3:
            vs, hs = opt.TANK.goto(-50, -2.5)  
        else:
            vs, hs = opt.TANK.goto(-50, -5.9) 
    else:
        vs, hs = 0,0
    return vs, hs