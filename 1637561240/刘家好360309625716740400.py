import opt
import math
# 赢 输

def take_enemy():
    en_list = opt.enemy_tanks()
    ball_pos = (opt.BALL.x, opt.BALL.y)
    dist_list = []
    for i in en_list:
        en_pos = (i.x, i.y)
        dist_list.append(get_distance(ball_pos, en_pos))
    lowest = 99999
    for i in dist_list:
        if i < lowest:
            lowest = i
    cloest_tank = en_list[dist_list.index(lowest)]
    vs, hs = opt.TANK.goto(cloest_tank.x, cloest_tank.y)
    if opt.TANK.x < -40:
        vs = -1
    return vs,hs

def get_distance(position1,position2):
    return math.sqrt((position1[0]-position2[0])**2 + (position1[1]-position2[1])**2)

def get_door_line():
    # 获取坦克到球门的两条直线
    # 返回一个长度为二的二维数组，分别存放两条直线的k和b
    x1 = opt.TANK.x
    x2 = opt.ENEMY_DOOR_LEFT.x
    y1 = opt.TANK.y
    y2 = opt.ENEMY_DOOR_LEFT.y
    k1 = (y1-y2) / (x1-x2)
    b1 = y1 / (k1*x)

    x2 = opt.ENEMY_DOOR_RIGHT.x
    y2 = opt.ENEMY_DOOR_RIGHT.y
    k2 = (y1-y2) / (x1-x2)
    b2 = y1 / (k2*x)

    return [[k1,b1],[k2,b2]]

def get_ball_line():
    # 获取坦克到球的直线
    x1 = opt.TANK.x
    x2 = opt.BALL.x
    y1 = opt.TANK.y
    y2 = opt.BALL.y
    k = (y1-y2) / (x1-x2)
    if k != 0 and x1 !=0:
        b = y1 / (k*x1)
    else:
        k,b = 1,0
    return [k,b]

def ball_predict(ball_line):
    # 判断x为50时，球的y是否在另外两条线之间
    ball_y = ball_line[0] * opt.ENEMY_DOOR_LEFT.x + ball_line[1]
    print(opt.TANK.cool_remain)
    if ball_y > opt.ENEMY_DOOR_RIGHT.y and ball_y < opt.ENEMY_DOOR_LEFT.y and not opt.TANK.is_ball_in_range(2):
        opt.TANK.do_fire()
    return


    

def attact_control_speed(angle):
    """
    :param angle: 坦克与足球夹角，范围为[0,360], 逆时针方向
    :return: [垂直速度，水平速度]
    """
    # 45°至135°，足球在坦克左方
    if 40 < angle <= 135:
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

KEEP = False
KEEPRemain = 1000
Kvs, Khs = 0, 0
LockNumber = 0

def LockSwitch(PolicyNumber):
    if PolicyNumber == 1:
        KeepPolicy1()
    elif PolicyNumber == 2:
        KeepPolicy3()
    else:
        pass

def KeepPolicy1():
    global KEEP,KEEPRemain,Kvs,Khs,LockNumber

    if KEEPRemain == 0:
        KeepPolicy2()  #进入阶段2，从球的前面截住球
    else:
        KEEPRemain -= 18    #减少死锁时间
        if opt.TANK.y < 0:  #在下边缘（右转）
            Kvs,Khs = 1,  0.3
        else:               #在上边缘
            Kvs,Khs = 1, -0.3

def KeepPolicy2():
    global KEEP,KEEPRemain,Kvs,Khs,LockNumber

    if not (opt.TANK.y <= opt.BALL.y+0.1 and opt.TANK.y >= opt.BALL.y-0.1):     #如果坦克还没有回正到球的y轴
        if opt.TANK.y < 0:
            Kvs,Khs = 1, -0.3
        else:
            Kvs, Khs = 1, 0.3
    else:
        KEEP = False     #解开死锁
        KEEPRemain = 1000   #重置死锁时间
        LockNumber = 0

def KeepPolicy3():
    global KEEP,KEEPRemain,Kvs,Khs,LockNumber

    if KEEPRemain == 0:
        KeepPolicy4()
    else:
        KEEPRemain -= 18
        if opt.TANK.y < 0:
            Kvs, Khs = 1,-0.3
        else:
            Kvs,Khs = 1,0.3

def KeepPolicy4():
    global KEEP,KEEPRemain,Kvs,Khs,LockNumber

    if not(opt.TANK.y <= opt.BALL.y + 0.1 and opt.TANK.y >= opt.BALL.y-0.1):
        if opt.TANK.y < 0:
            Kvs,Khs = 1,0.3
        else:
            Kvs, Khs = 1,-0.3
    else:
        KEEP = False
        KEEPRemain = 1000
        LockNumber = 0

def attack():
    """
    坦克的策略函数，函数内需要实现此坦克的在每一帧的行为策略。
    使用opt库，获得场上比赛状态，根据状态施加你的自定义策略。
    该函数将会在比赛中的每一帧重复调用，直到比赛结束。
    :return: 当前状态下，当前坦克的操控值（前后速度，左右速度）
    """

    global KEEP,KEEPRemain,Kvs,Khs,LockNumber

    target_x = opt.BALL.x
    target_y = opt.BALL.y
    
    if opt.TANK.is_ball_in_range(2) and opt.distance(opt.BALL.x, opt.BALL.y, 0, 0) < 20:
        if opt.TANK.is_stuck(0.7):
            vs,hs = -0.1, 0.1
        # 射击判断(自定)
    ball_predict(get_ball_line())
    
    if not KEEP:
        if not opt.TANK.is_ball_in_range(2):

            # 如果坦克-足球的直线距离较大，选择追击足球
            #tank_angle_to_football = opt.TANK.angle_to(target_x, target_y)
            # 根据相对角度计算 前后速度（v）和左右速度(h)
            #vs, hs = attact_control_speed(tank_angle_to_football)
            if opt.BALL.x  < -30 and opt.TANK.face_my_door():
                if opt.BALL.y < 0 :
                    target_y+=2
                else:
                    target_y-=2
                tank_angle_to_football = opt.TANK.angle_to(target_x, target_y-0.5)
                vs, hs = attact_control_speed(tank_angle_to_football)   
            else:
                vs, hs = opt.TANK.chase_ball()

        else:
            # 如果坦克-足球的直线距离较小，微调位置进行进攻
            # 我们提供了根据球门，球和坦克的角度信息，判断是否有利于攻击的函数
            if opt.TANK.on_east_of(opt.BALL):
            #if not opt.TANK.on_east_of(opt.BALL):
                # 若不利于进攻，输出需要调整到的目标方位
                target_x, target_y = opt.BALL.x - 5, opt.BALL.y
            if opt.TANK.is_ball_in_range(2):    
                if opt.BALL.x >= 45:
                    target_x -=2
                elif opt.BALL.x <= -40:
                    target_x -=3.2
            tank_angle_to_football = opt.TANK.angle_to(target_x, target_y-0.5)
            vs, hs = attact_control_speed(tank_angle_to_football)

        if opt.TANK.is_ball_in_range(5) and opt.TANK.on_west_of(opt.BALL) and (opt.BALL.y >=24.0 or opt.BALL.y <= -24.0):
            KEEP = True         # 进入第一个动作
            LockNumber = 1
            LockSwitch(1)

        if opt.TANK.is_ball_in_range(5) and opt.TANK.on_east_of(opt.BALL) and (opt.BALL.y >=24.0 or opt.BALL.y <=-24.0):
            KEEP = True
            LockNumber = 2
            LockSwitch(2)

        if opt.TANK.face_enemy_door() and opt.TANK.is_ball_in_range(20):
            opt.TANK.do_fire()
    elif KEEP and LockNumber == 1:
        LockSwitch(1)
        vs,hs = Kvs, Khs
    elif KEEP and LockNumber == 2:
        LockSwitch(2)
        vs,hs = Kvs, Khs
    return vs, hs


def lerp(a,b,alpha):        # 线性插值
    return a+(b-a)*alpha


def defence():
    """
    坦克的策略函数，函数内需要实现此坦克的在每一帧的行为策略。
    使用opt库，获得场上比赛状态，根据状态施加你的自定义策略。
    该函数将会在比赛中的每一帧重复调用，直到比赛结束。
    :return: 当前状态下，当前坦克的操控值（前后速度，左右速度）
    """
    vs,hs = 0,0
    target_x = opt.BALL.x
    target_y = opt.BALL.y
    if opt.TANK.face_enemy_door(0) and target_y > -1 and target_y <1:       # 开局射击
        opt.TANK.do_fire() 
    if not opt.TANK.face_my_door(0) and opt.TANK.is_ball_in_range(20, 0.08,0):
        opt.TANK.do_fire()
    
    if target_x > -20 or opt.TANK.is_ball_in_range(8):         # 球在远处，保持位置
        alpha = (opt.BALL.y + 25)/50
        vs,hs = opt.TANK.goto(-50, lerp(opt.MY_DOOR_RIGHT.y,opt.MY_DOOR_LEFT.y,alpha))

        vs += 0.2       # 略微增强撞击力度
    else:
        #vs,hs = opt.TANK.goto(target_x, target_y)
        vs, hs = opt.TANK.chase_ball()

    return vs, hs




def tank1_update():
    """
    坦克1的策略函数，函数内需要实现此坦克的在每一帧的行为策略。
    使用opt库，获得场上比赛状态，根据状态施加你的自定义策略。
    该函数将会在比赛中的每一帧重复调用，直到比赛结束。
    :return: 当前状态下，当前坦克的操控值（前后速度，左右速度）
    """
    
    return attack()


def tank2_update():
    """
    坦克2的策略函数，函数内需要实现此坦克的在每一帧的行为策略。
    使用opt库，获得场上比赛状态，根据状态施加你的自定义策略。
    该函数将会在比赛中的每一帧重复调用，直到比赛结束。
    :return: 当前状态下，当前坦克的操控值（前后速度，左右速度）
    """
    return attack()

def tank3_update():
    """
    坦克3的策略函数，函数内需要实现此坦克的在每一帧的行为策略。
    使用opt库，获得场上比赛状态，根据状态施加你的自定义策略。
    该函数将会在比赛中的每一帧重复调用，直到比赛结束。
    :return: 当前状态下，当前坦克的操控值（前后速度，左右速度）
    """
    return take_enemy()


def tank4_update():
    """
    坦克4的策略函数，函数内需要实现此坦克的在每一帧的行为策略。
    使用opt库，获得场上比赛状态，根据状态施加你的自定义策略。
    该函数将会在比赛中的每一帧重复调用，直到比赛结束。
    :return: 当前状态下，当前坦克的操控值（前后速度，左右速度）
    """
    return take_enemy()


def tank5_update():
    """
    坦克5的策略函数，函数内需要实现此坦克的在每一帧的行为策略。
    使用opt库，获得场上比赛状态，根据状态施加你的自定义策略。
    该函数将会在比赛中的每一帧重复调用，直到比赛结束。
    :return: 当前状态下，当前坦克的操控值（前后速度，左右速度）
    """
    
    return defence()
