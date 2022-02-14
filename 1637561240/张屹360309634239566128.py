import opt

def fix_shoot_angle(ball_x,ball_y):
    if ball_x >= 0 and ball_x < 25:
        if ball_y >= -8 and ball_y <= 8:
            return opt.TANK.goto(ball_x - 2, ball_y)
        elif ball_y >= -16 and ball_y <-8:
            return opt.TANK.goto(ball_x - 2, ball_y - 2)
        elif ball_y >= -25 and ball_y <-16:
            return opt.TANK.goto(ball_x - 2, ball_y - 4)
        elif ball_y > 8 and ball_y <=20:
           return opt.TANK.goto(ball_x - 2, ball_y + 2)
        elif ball_y > 16 and ball_y <=25:
            return opt.TANK.goto(ball_x - 2, ball_y + 4)
        else:
            return 0,0
    else:
        return opt.TANK.chase_ball()

def attact_control_speed(angle):
    """
    :param angle: 坦克与足球夹角，范围为[0,360], 逆时针方向
    :return: [垂直速度，水平速度]
    """
    # 45°至135°，足球在坦克左方
    if 0.1< angle<=1:
        vs, hs =1,-0.58
    elif 0.03< angle<=0.1:
        vs, hs =0.85,-0.05
    elif 1< angle<=2:
        vs, hs =1,-0.45
    elif 2< angle<=3:
        vs, hs =1,-0.43
    elif 3< angle<4:
        vs, hs =1,-0.41
    elif 4< angle<5:
        vs, hs =1,-0.4
    elif 45< angle<90:
        vs, hs =0.2,-0.52
    elif 356<= angle <357:
        vs, hs =1,0.3
    elif 357<= angle <358:
        vs, hs =1,0.45
    elif 358<= angle <359.9:
        vs, hs =1,0.58
    elif 359.9 < angle < 359.97:
        vs, hs = 0.85,0.05
    elif 315<= angle <350:
        vs ,hs =1,0.52
    else:
        vs, hs = 0.85,0
  

    return vs, hs  # vertical_speed, horizontal_speed

def attack1():
    """
    攻击策略 （待优化）
    """
    if opt.TANK.face_enemy_door():
        opt.TANK.do_fire()
    target_x = opt.BALL.x
    target_y = opt.BALL.y
    if opt.TANK.is_stuck(0.3):
        vs,hs=-1,0
    while opt.TANK.face_my_door(7):
        vs,hs=-1,0.1
        return vs,hs
        if not opt.TANK.face_my_door:
            break
    if not opt.TANK.is_ball_in_range(15):
        # 如果坦克-足球的直线距离较大，选择追击足球
        #tank_angle_to_football = opt.TANK.angle_to(target_x, target_y)
        # 根据相对角度计算 前后速度（v）和左右速度(h)
        #vs, hs = attact_control_speed(tank_angle_to_football)
        vs,hs = opt.TANK.chase_ball()
    else:
        # 如果坦克-足球的直线距离较小，微调位置进行进攻
        # 我们提供了根据球门，球和坦克的角度信息，判断是否有利于攻击的函数
        if opt.TANK.on_east_of(opt.BALL):
            # 若不利于进攻，输出需要调整到的目标方位
            if opt.TANK.on_north_of(opt.BALL):
                vs,hs = opt.TANK.goto(opt.BALL.x -4, opt.BALL.y - 1)
            else:
                vs,hs = opt.TANK.goto(opt.BALL.x -4, opt.BALL.y + 1)
            tank_ball_angle = opt.TANK.angle_to(opt.BALL.x,opt.BALL.y)
            if opt.TANK.face_enemy_door() and tank_ball_angle <= 5 and tank_ball_angle >= -5:
                opt.TANK.do_fire()
            return vs,hs
        tank_angle_to_football = opt.TANK.angle_to(target_x, target_y)
        vs, hs = attact_control_speed(tank_angle_to_football)
    return vs, hs

def defence_1():
    """
    后卫行为函数 
    """ 
    if opt.TANK.x < -40 and opt.TANK.face_my_door() and not opt.TANK.is_ball_in_range(18):
        vs,hs = 0.1,0.5

    if opt.TANK.is_ball_in_range(30):
        vs,hs = opt.TANK.goto(opt.BALL.x - 3, opt.BALL.y)
        if not opt.TANK.face_enemy_door(5)and opt.TANK.angle_to(opt.BALL.x,opt.BALL.y) >= -3 and opt.TANK.angle_to(opt.BALL.x,opt.BALL.y) <= 3:
            opt.TANK.do_fire() 
    else:
        vs,hs=0,0
    return vs,hs 

def defence_2():
    """
    守门员行为函数
    """
    if opt.TANK.is_stuck(0.3):
        vs,hs=-1,0
    if opt.TANK.x < -48 and opt.TANK.face_my_door() and not opt.TANK.is_ball_in_range(18):
        vs,hs = 0.1,0.5
    if opt.TANK.is_ball_in_range(20):
        vs,hs = opt.TANK.goto(opt.BALL.x - 3 , opt.BALL.y)
        if not opt.TANK.face_my_door() and opt.TANK.angle_to(opt.BALL.x,opt.BALL.y) >= -3 and opt.TANK.angle_to(opt.BALL.x,opt.BALL.y) <= 3:
            opt.TANK.do_fire() 
    else:
        vs,hs = 0,0
    return vs,hs 

def tank1_update():
    """
    前锋，不参与防守，拥有自己的进攻策略
    """
    if opt.TANK.face_enemy_door():
        opt.TANK.do_fire()
    if opt.TANK.is_stuck(0.3):
        vs,hs=-1,0
        return vs,hs
    while opt.TANK.face_my_door(7):
        vs,hs=-1,0.1
        return vs,hs
        if not opt.TANK.face_my_door:
            break
    if opt.BALL.x < 0: # 如果球在本方半场，则前锋需要到（0,10）静候球进攻到敌方半场
        return opt.TANK.goto(0,0)
    else:
        # 只有不面对本方半场且球在前锋坦克右侧时
        if opt.TANK.is_ball_in_range(50) and not opt.TANK.on_east_of(opt.BALL) and opt.TANK.face_enemy_door():
            # 未到一定距离之内时，选择用追球函数，自动追球。
            if not opt.TANK.is_ball_in_range(15):
                return opt.TANK.chase_ball()
            else: # 到达一定距离之内，先开火，之后根据与球之间的位置关系进行带球或追球
                return fix_shoot_angle(opt.BALL.x ,opt.BALL.y)
        else: # 若执行这个else，说明可能球在前锋的左侧，或者前锋正面对我方球门，需要先跑到球的左侧。
            if opt.TANK.on_east_of(opt.BALL):
                return opt.TANK.goto(opt.BALL.x - 10, opt.BALL.y + 5)
            else:
                return opt.TANK.chase_ball()

def tank2_update():
    """
    球在敌方半场，执行前锋坦克1的行为，球在我方半场，执行attack()的行为
    """
    if opt.BALL.x > 0:
        # 只有不面对本方半场且球在前锋坦克右侧时
        if opt.TANK.is_ball_in_range(50) and not opt.TANK.on_east_of(opt.BALL) and opt.TANK.face_enemy_door():
            # 未到一定距离之内时，选择用追球函数，自动追球。
            if not opt.TANK.is_ball_in_range(15):
                return opt.TANK.chase_ball()
            else: # 到达一定距离之内，先开火，之后根据与球之间的位置关系进行带球或追球
                return fix_shoot_angle(opt.BALL.x ,opt.BALL.y)
        else: # 若执行这个else，说明可能球在前锋的左侧，或者前锋正面对我方球门，需要先跑到球的左侧。
            if opt.TANK.on_east_of(opt.BALL):
                return opt.TANK.goto(opt.BALL.x - 10, opt.BALL.y + 5)
            else:
                return opt.TANK.chase_ball()
    else:
        return attack1()
def tank3_update():
    """
    坦克3只执行attack行为
    """
    
    return attack1()

def tank4_update():
    """
    后卫
    """
    vs,hs=opt.TANK.goto(-30, opt.BALL.y)
    return vs,hs
    
    
    

def tank5_update():
    """
    守门员
    """
    a=opt.BALL.x
    b=opt.BALL.y 
    if opt.TANK.is_stuck(0.3):
        vs,hs=-1,0
        return vs,hs
    if opt.TANK.is_ball_in_range(15):
        if opt.TANK.cool_remain==0:
            if -7<=b<=7:
                vs,hs= opt.TANK.goto(-50, opt.BALL.y)
                opt.TANK.do_fire()
                return vs,hs
                 
            elif b>7:
                vs,hs= opt.TANK.goto(-50, 7)
                opt.TANK.do_fire()
                return vs,hs
               
            else:
                vs,hs= opt.TANK.goto(-50, -7)
                opt.TANK.do_fire()
                return vs,hs
        else:
            if -7<=b<=7:
                vs,hs= opt.TANK.goto(-50, opt.BALL.y)
                return vs,hs
                 
            elif b>7:
                vs,hs= opt.TANK.goto(-50, 7)
                return vs,hs
               
            else:
                vs,hs= opt.TANK.goto(-50, -7)
                return vs,hs
    else:
        if -7<b<7:
            vs,hs= opt.TANK.goto(-50, opt.BALL.y)
            return vs,hs
                 
        elif b>7:
            vs,hs= opt.TANK.goto(-50, 7)
            return vs,hs
               
        else:
            vs,hs= opt.TANK.goto(-50, -7)
            return vs,hs
    