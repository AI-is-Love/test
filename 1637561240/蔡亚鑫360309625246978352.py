import opt
import math

def get_control_speed(angle):
    """
    :param angle: 坦克与足球夹角，范围为[0,360], 逆时针方向
    :return: [垂直速度，水平速度]
    """
    vs, hs = 0,0
    if 0 <= angle < 20 or 340 <= angle <= 360:
        vs, hs = 1, 0
    elif 20 <= angle < 60:
        vs, hs = 0.6, -0.4
    elif 60 <= angle < 100:
        vs, hs = 0.4, -0.4
    elif 100 <= angle < 140:
        vs, hs = -0.4, -0.4
    elif 140 <= angle < 180:
        vs, hs = -0.6, -0.4
    elif 180 <= angle < 220:
        vs, hs = -0.6, 0.4
    elif 220 <= angle < 260:
        vs, hs = -0.4, 0.4
    elif 260 <= angle < 300:
        vs, hs = 0.4, 0.4
    elif 300 <= angle < 340:
        vs, hs = 0.6, 0.4

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
        # 根据相对角度计算 前后速度（v）和左右速度(h)
        vs, hs = get_control_speed(tank_angle_to_football)
    else:
        # 如果坦克-足球的直线距离较小，微调位置进行进攻
        # 我们提供了根据球门，球和坦克的角度信息，判断是否有利于攻击的函数
        if opt.TANK.on_east_of(opt.BALL):
            # 若不利于进攻，输出需要调整到的目标方位
            target_x, target_y = opt.BALL.x - 4, opt.BALL.y
        vs, hs = get_control_speed(opt.TANK.angle_to(target_x, target_y))
    if opt.TANK.cool_remain == 0:
        opt.TANK.do_fire()
    # print(vs, hs)
    return vs, hs

def defend( target_x, target_y, distance):
    """
    坦克的策略函数，函数内需要实现此坦克的在每一帧的行为策略。
    使用opt库，获得场上比赛状态，根据状态施加你的自定义策略。
    该函数将会在比赛中的每一帧重复调用，直到比赛结束。
    :return: 当前状态下，当前坦克的操控值（前后速度，左右速度）
    """
    if opt.BALL.x < distance:
        vs, hs = attack()
    else:
        if math.sqrt((opt.TANK.x-target_x)**2 + (opt.TANK.y-target_y)**2) < 5:
            if 0.15 >= opt.TANK.r >= -0.15:
                vs, hs = 0,0
            else:
                vs, hs = 0.3,-6
        else:
            tank_angle_to_football = opt.TANK.angle_to(target_x, target_y)
            # 根据相对角度计算 前后速度（v）和左右速度(h)
            vs, hs = get_control_speed(tank_angle_to_football)
    if opt.TANK.cool_remain == 0:
        opt.TANK.do_fire()
    return vs, hs

def tank1_update():
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
    return attack()


def tank4_update():
    bx=opt.ENV.ball.x
    by=opt.ENV.ball.y
    tx=opt.TANK.x
    ty=opt.TANK.y
    vs=0
    hs=0
    c=0
    d=0
    a=0
    b=0
    an=0
    a=abs(tx-bx)
    b=abs(ty-by)
    if a<b:
        c=b
        d=a
    else:
        d=b
        c=a
    an=90.0/c*d
    if d==b:
        an=90.0-an
    e=c*c+d*d
    i=c
    while i*i<e:
        i=i+1
    if i*i > e:
        i=i-0.5
    if i == 0:
        i=1
    hs=an/i*0.748291015625
    vs=0.748291015625
    if tx-bx<0:
        vs=0.748291015625
        vs=vs
    elif tx-bx>0:
        vs=-0.748291015625
        vs=vs
    else:
        vs=0
    if ty-by<0:
        hs=hs
    elif ty-by>0:
        hs=hs-hs-hs
    else:
        hs=0
    if i>40:
        return defend(-30, 10, 15)
    elif i<=31:
        hs=hs
        vs=vs
        if i<=23:
            hs=hs
            vs=vs
        elif i<=15:
            if hs>0:
                hs=1
            else:
                hs=-1
            if vs>0:
                vs=1
            else:
                vs=-1
        if i<=2.3:
            if i>1.5:
                hs=0.001*hs
    else:
        hs=-1*hs
        vs=-1*vs
    tont=0
    if a==0:
        tont=1
    if b==0:
        tont=1
    tont=tont
    if tont == 1:
        vs=1
        hs=0
    if i>5:
        tont=0
    return vs,hs


def tank5_update():
    bx=opt.ENV.ball.x
    by=opt.ENV.ball.y
    tx=opt.TANK.x
    ty=opt.TANK.y
    vs=0
    hs=0
    c=0
    d=0
    a=0
    b=0
    an=0
    a=abs(tx-bx)
    b=abs(ty-by)
    if a<b:
        c=b
        d=a
    else:
        d=b
        c=a
    an=90.0/c*d
    if d==b:
        an=90.0-an
    e=c*c+d*d
    i=c
    while i*i<e:
        i=i+1
    if i*i > e:
        i=i-0.5
    if i == 0:
        i=1
    hs=an/i*0.748291015625
    vs=0.748291015625
    if tx-bx<0:
        vs=0.748291015625
        vs=vs
    elif tx-bx>0:
        vs=-0.748291015625
        vs=vs
    else:
        vs=0
    if ty-by<0:
        hs=hs
    elif ty-by>0:
        hs=hs-hs-hs
    else:
        hs=0
    if i>40:
        return defend(-50, -10,-15)
    elif i<=31:
        hs=hs
        vs=vs
        if i<=23:
            hs=hs
            vs=vs
        elif i<=15:
            if hs>0:
                hs=1
            else:
                hs=-1
            if vs>0:
                vs=1
            else:
                vs=-1
        if i<=2.3:
            if i>1.5:
                hs=0.001*hs
    else:
        hs=-1*hs
        vs=-1*vs
    tont=0
    if a==0:
        tont=1
    if b==0:
        tont=1
    tont=tont
    if tont == 1:
        vs=1
        hs=0
    if i>5:
        tont=0
    return vs,hs
