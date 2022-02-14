import opt
# 输
'''
print("我方左柱的坐标为：",opt.MY_DOOR_LEFT.x,opt.MY_DOOR_LEFT.y)
print("我方右柱的坐标为：",opt.MY_DOOR_RIGHT.x,opt.MY_DOOR_RIGHT.y)
print("敌方左柱的坐标为：",opt.ENEMY_DOOR_LEFT.x,opt.ENEMY_DOOR_LEFT.y)
print("敌方右柱的坐标为：",opt.ENEMY_DOOR_RIGHT.x,opt.ENEMY_DOOR_RIGHT.y)
'''
#获取敌我左右门柱坐标
MY_RIGHTDOORSITE_X=opt.MY_DOOR_RIGHT.x
MY_RIGHTDOORSITE_Y=opt.MY_DOOR_RIGHT.y
MY_LEFTDOORSITE_X=opt.MY_DOOR_LEFT.x
MY_LEFTDOORSITE_Y=opt.MY_DOOR_LEFT.y
ENEMY_RIGHTDOORSITE_X=opt.ENEMY_DOOR_RIGHT.x
ENEMY_RIGHTDOORSITE_Y=opt.ENEMY_DOOR_RIGHT.y
ENEMY_LEFTDOORSITE_X=opt.ENEMY_DOOR_LEFT.x
ENEMY_LEFTDOORSITE_Y=opt.ENEMY_DOOR_LEFT.y
MY_DOORMIDDLESITE_X=(MY_RIGHTDOORSITE_X+MY_LEFTDOORSITE_X)/2
MY_DOORMIDDLESITE_Y=(MY_RIGHTDOORSITE_Y+MY_LEFTDOORSITE_Y)/2
ENEMY_DOORMIDDLESITE_X=50
ENEMY_DOORMIDDLESITE_Y=0

'''
def get_position():
    global tank1_x
    global tank1_y
    global tank2_x
    global tank2_y
    global tank3_x
    global tank3_y
    global tank4_x
    global tank4_y
    tank1_x=opt.my_other_tanks()[0].x
    tank1_y=opt.my_other_tanks()[0].y
    tank2_x=opt.my_other_tanks()[1].x
    tank2_y=opt.my_other_tanks()[1].y
    tank3_x=opt.my_other_tanks()[2].x
    tank3_y=opt.my_other_tanks()[2].y
    tank4_x=opt.my_other_tanks()[3].x
    tank4_y=opt.my_other_tanks()[3].y

    return 0
'''
def attact_control_speed(angle):
    """
    :param angle: 坦克与足球夹角，范围为[0,360], 逆时针方向
    :return: [垂直速度，水平速度]
    """
    if opt.BALL.x>opt.TANK.x +2:
        vs,hs=opt.TANK.chase_ball()
    else:
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


def attack():
    """
    坦克的策略函数，函数内需要实现此坦克的在每一帧的行为策略。
    使用opt库，获得场上比赛状态，根据状态施加你的自定义策略。
    该函数将会在比赛中的每一帧重复调用，直到比赛结束。
    :return: 当前状态下，当前坦克的操控值（前后速度，左右速度）
    """
    target_x = opt.BALL.x
    target_y = opt.BALL.y
    '''
    if opt.TANK.cool_remain==0:
        if tank.distance_to(ball_site_x,ball_site_y)<=3 and \
        opt.TANK.face_enemy_door(5)==True:
            opt.TANK.do_fire()
        elif tank.distance_to(ball_site_x,ball_site_y)>=5 and\
        (ball_site_y-tank_site_y)*50/(ball_site_x-tank_site_x)+((tank_site_y*ball_site_x)-(tank_site_x*ball_site_y))/(ball_site_x-tank_site_x)>=-8 and \
        (ball_site_y-tank_site_y)*50/(ball_site_x-tank_site_x)+((tank_site_y*ball_site_x)-(tank_site_x*ball_site_y))/(ball_site_x-tank_site_x)<=8 and \
        opt.TANK.face_enemy_door(5)==True:
            opt.TANK.do_fire()
    '''
    if target_x<=-40:
        vs,hs=opt.TANK.goto(-30,0)
    if not opt.TANK.is_ball_in_range(2):
         # 如果坦克-足球的直线距离较大，选择追击足球
        tank_angle_to_football = opt.TANK.angle_to(target_x, target_y)
        # 根据相对角度计算 前后速度（v）和左右速度(h)
        vs, hs = attact_control_speed(tank_angle_to_football)
    else:
        # 如果坦克-足球的直线距离较小，微调位置进行进攻
        # 我们提供了根据球门，球和坦克的角度信息，判断是否有利于攻击的函数
        if not opt.TANK.on_east_of(opt.BALL):
            # 若不利于进攻，输出需要调整到的目标方位
            target_x, target_y = opt.BALL.x - 3, opt.BALL.y
            tank_angle_to_football = opt.TANK.angle_to(target_x, target_y)
            vs, hs = attact_control_speed(tank_angle_to_football)
    return vs, hs

'''
if opt.BALL.x>opt.TANK.x +2:
        vs,hs=opt.TANK.chase_ball()
    else:
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

'''

def defence(x,y):
    """
    坦克的策略函数，函数内需要实现此坦克的在每一帧的行为策略。
    使用opt库，获得场上比赛状态，根据状态施加你的自定义策略。
    该函数将会在比赛中的每一帧重复调用，直到比赛结束。
    :return: 当前状态下，当前坦克的操控值（前后速度，左右速度）
    """
    ball_site_x=opt.BALL.x
    ball_site_y=opt.BALL.y
    tank_site_x=opt.TANK.x
    tank_site_y=opt.TANK.y
    observed_sprites = opt.TANK.observe(0.02, -0.02, True)
    t=0
    for s in observed_sprites:
        if type(s) == type(opt.BALL):
            t=1
    emergency_distance1=((ball_site_x+50)**2+(ball_site_y-8)**2)**(1/2)#获取球离我方左门柱的距离
    emergency_distance2=((ball_site_x+50)**2+(ball_site_y+8)**2)**(1/2)#获取球离我方右门柱的距离
    if emergency_distance1<=15 and (number==3 or number==2):
        vs, hs = opt.TANK.goto(ball_site_x, ball_site_y)
    elif emergency_distance2<=15 and (number==5 or number==4):
        vs, hs = opt.TANK.goto(ball_site_x, ball_site_y)
    # elif (MY_DOORMIDDLESITE_X<=tank_site_x+1 and MY_DOORMIDDLESITE_X>=tank_site_x-2) and \
    # (MY_DOORMIDDLESITE_Y<=tank_site_y+2 and MY_DOORMIDDLESITE_Y>=tank_site_y-2):
    #     vs,hs=0,0
    elif number==5:
        vs,hs=opt.TANK.goto(MY_DOORMIDDLESITE_X,MY_DOORMIDDLESITE_Y-2)
    elif number==4:
        vs,hs=opt.TANK.goto(MY_DOORMIDDLESITE_X,MY_DOORMIDDLESITE_Y-5)
    elif number==3:
        vs,hs=opt.TANK.goto(MY_DOORMIDDLESITE_X,MY_DOORMIDDLESITE_Y+2)
    elif number==2:
        vs,hs=opt.TANK.goto(MY_DOORMIDDLESITE_X,MY_DOORMIDDLESITE_Y+5)
    t=0


    '''
    get_position()
    print("1号坦克的坐标：",tank1_x,tank1_y)
    print("2号坦克的坐标：",tank2_x,tank2_y)
    print("3号坦克的坐标：",tank3_x,tank3_y)
    print("4号坦克的坐标：",tank4_x,tank4_y)
    '''
    return vs, hs
   


def tank1_update():
    """
    坦克1的策略函数，函数内需要实现此坦克的在每一帧的行为策略。
    使用opt库，获得场上比赛状态，根据状态施加你的自定义策略。
    该函数将会在比赛中的每一帧重复调用，直到比赛结束。
    :return: 当前状态下，当前坦克的操控值（前后速度，左右速度）
    """
    number=1
    ball_site_x=opt.BALL.x
    ball_site_y=opt.BALL.y
    tank_site_x=opt.TANK.x
    tank_site_y=opt.TANK.y
    tank=opt.Sprite(1,tank_site_x,tank_site_y,0,0,0,0)
    tank.x, tank.y,tank.r=tank_site_x,tank_site_y,0
    ball=opt.Sprite(0,ball_site_x,ball_site_y,0,0,0,0)
    tank_angle=tank.radian_to(0,0)
    ball_angle=ball.radian_to(0,0)
    tank_angle_to_football = opt.TANK.angle_to(ball_site_x,ball_site_y)
    #print("一号坦克和足球的夹角为：",tank_angle_to_football)
    '''
    if opt.TANK.cool_remain==0 and \
    tank.distance_to(ball_site_x, ball_site_y)<=3 and \
    opt.TANK.face_enemy_door(5)==True:
        opt.TANK.do_fire()
    '''
    observed_sprites = opt.TANK.observe(0.02, -0.02, True)
    t=0
    for s in observed_sprites:
        if type(s) == type(opt.BALL):
            t=1
    if opt.TANK.cool_remain==0:
        if tank.distance_to(ball_site_x,ball_site_y)<=3 and \
        opt.TANK.face_enemy_door(5)==True and \
        t==1:
            opt.TANK.do_fire()
        elif tank.distance_to(ball_site_x,ball_site_y)>=5 and\
        (ball_site_y-tank_site_y)*50/(ball_site_x-tank_site_x)+((tank_site_y*ball_site_x)-(tank_site_x*ball_site_y))/(ball_site_x-tank_site_x)>=-8 and \
        (ball_site_y-tank_site_y)*50/(ball_site_x-tank_site_x)+((tank_site_y*ball_site_x)-(tank_site_x*ball_site_y))/(ball_site_x-tank_site_x)<=8 and \
        opt.TANK.face_enemy_door(5)==True and \
        t==1:
            opt.TANK.do_fire()

    # print(type(opt.TANK.observe(0.5, -0.5, True)[-1])==type(opt.BALL))

    return attack()


def tank2_update():
    """
    坦克2的策略函数，函数内需要实现此坦克的在每一帧的行为策略。
    使用opt库，获得场上比赛状态，根据状态施加你的自定义策略。
    该函数将会在比赛中的每一帧重复调用，直到比赛结束。
    :return: 当前状态下，当前坦克的操控值（前后速度，左右速度）
    """
    global number
    number=2
    ball_site_x=opt.BALL.x
    ball_site_y=opt.BALL.y
    tank_site_x=opt.TANK.x
    tank_site_y=opt.TANK.y
    tank=opt.Sprite(2,tank_site_x,tank_site_y,0,0,0,0)
    tank.x, tank.y,tank.r=tank_site_x,tank_site_y,0
    ball=opt.Sprite(0,ball_site_x,ball_site_y,0,0,0,0)
    tank_angle=tank.radian_to(0,0)
    ball_angle=ball.radian_to(0,0)
    '''
    if opt.TANK.cool_remain==0 and \
    tank.distance_to(ball_site_x, ball_site_y)<=3 and \
    opt.TANK.face_enemy_door(5)==True:
        opt.TANK.do_fire()
    '''
    observed_sprites = opt.TANK.observe(0.05, -0.05, True)
    t=0
    for s in observed_sprites:
        if type(s) == type(opt.BALL):
            t=1
    if opt.TANK.cool_remain==0:
        if tank.distance_to(ball_site_x,ball_site_y)<=3 and \
        opt.TANK.face_enemy_door(5)==True and \
        t==1:
            opt.TANK.do_fire()
        elif tank.distance_to(ball_site_x,ball_site_y)>=5 and\
        (ball_site_y-tank_site_y)*50/(ball_site_x-tank_site_x)+((tank_site_y*ball_site_x)-(tank_site_x*ball_site_y))/(ball_site_x-tank_site_x)>=-8 and \
        (ball_site_y-tank_site_y)*50/(ball_site_x-tank_site_x)+((tank_site_y*ball_site_x)-(tank_site_x*ball_site_y))/(ball_site_x-tank_site_x)<=8 and \
        opt.TANK.face_enemy_door(5)==True and \
        t==1:
            opt.TANK.do_fire()

    return defence(-45,0)


def tank3_update():
    """
    坦克3的策略函数，函数内需要实现此坦克的在每一帧的行为策略。
    使用opt库，获得场上比赛状态，根据状态施加你的自定义策略。
    该函数将会在比赛中的每一帧重复调用，直到比赛结束。
    :return: 当前状态下，当前坦克的操控值（前后速度，左右速度）
    """
    global number
    number=3
    ball_site_x=opt.BALL.x
    ball_site_y=opt.BALL.y
    tank_site_x=opt.TANK.x
    tank_site_y=opt.TANK.y
    tank=opt.Sprite(3,tank_site_x,tank_site_y,0,0,0,0)
    tank.x, tank.y,tank.r=tank_site_x,tank_site_y,0
    ball=opt.Sprite(0,ball_site_x,ball_site_y,0,0,0,0)
    tank_angle=tank.radian_to(0,0)
    ball_angle=ball.radian_to(0,0)
    '''
    if opt.TANK.cool_remain==0 and \
    tank.distance_to(ball_site_x, ball_site_y)<=3 and \
    opt.TANK.face_enemy_door(5)==True:
        opt.TANK.do_fire()
    '''
    observed_sprites = opt.TANK.observe(0.05, -0.05, True)
    t=0
    for s in observed_sprites:
        if type(s) == type(opt.BALL):
            t=1
    if opt.TANK.cool_remain==0:
        if tank.distance_to(ball_site_x,ball_site_y)<=3 and \
        opt.TANK.face_enemy_door(5)==True and \
        t==1:
            opt.TANK.do_fire()
        elif tank.distance_to(ball_site_x,ball_site_y)>=5 and\
        (ball_site_y-tank_site_y)*50/(ball_site_x-tank_site_x)+((tank_site_y*ball_site_x)-(tank_site_x*ball_site_y))/(ball_site_x-tank_site_x)>=-8 and \
        (ball_site_y-tank_site_y)*50/(ball_site_x-tank_site_x)+((tank_site_y*ball_site_x)-(tank_site_x*ball_site_y))/(ball_site_x-tank_site_x)<=8 and \
        opt.TANK.face_enemy_door(5)==True and \
        t==1:
            opt.TANK.do_fire()

    return defence(-50,8)


def tank4_update():
    """
    坦克4的策略函数，函数内需要实现此坦克的在每一帧的行为策略。
    使用opt库，获得场上比赛状态，根据状态施加你的自定义策略。
    该函数将会在比赛中的每一帧重复调用，直到比赛结束。
    :return: 当前状态下，当前坦克的操控值（前后速度，左右速度） 
    """
    global number
    number=4
    ball_site_x=opt.BALL.x
    ball_site_y=opt.BALL.y
    tank_site_x=opt.TANK.x
    tank_site_y=opt.TANK.y
    tank=opt.Sprite(4,tank_site_x,tank_site_y,0,0,0,0)
    tank.x, tank.y,tank.r=tank_site_x,tank_site_y,0
    ball=opt.Sprite(0,ball_site_x,ball_site_y,0,0,0,0)
    tank_angle=tank.radian_to(0,0)
    ball_angle=ball.radian_to(0,0)
    #print(tank_angle,ball_angle)
    '''
    if opt.TANK.cool_remain==0 and \
    tank.distance_to(ball_site_x, ball_site_y)<=3 and \
    opt.TANK.face_enemy_door(5)==True:
            opt.TANK.do_fire()
    '''
    observed_sprites = opt.TANK.observe(0.05, -0.05, True)
    t=0
    for s in observed_sprites:
        if type(s) == type(opt.BALL):
            t=1
    if opt.TANK.cool_remain==0:
        if tank.distance_to(ball_site_x,ball_site_y)<=3 and \
        opt.TANK.face_enemy_door(5)==True and \
        t==1:
            opt.TANK.do_fire()
        elif tank.distance_to(ball_site_x,ball_site_y)>=5 and\
        (ball_site_y-tank_site_y)*50/(ball_site_x-tank_site_x)+((tank_site_y*ball_site_x)-(tank_site_x*ball_site_y))/(ball_site_x-tank_site_x)>=-8 and \
        (ball_site_y-tank_site_y)*50/(ball_site_x-tank_site_x)+((tank_site_y*ball_site_x)-(tank_site_x*ball_site_y))/(ball_site_x-tank_site_x)<=8 and \
        opt.TANK.face_enemy_door(5)==True and \
        t==1:
            opt.TANK.do_fire()
    



    return defence(-50,-8)


def tank5_update():
    """
    坦克5的策略函数，函数内需要实现此坦克的在每一帧的行为策略。
    使用opt库，获得场上比赛状态，根据状态施加你的自定义策略。
    该函数将会在比赛中的每一帧重复调用，直到比赛结束。
    :return: 当前状态下，当前坦克的操控值（前后速度，左右速度）
    """
    ball_site_x=opt.BALL.x
    ball_site_y=opt.BALL.y
    tank_site_x=opt.TANK.x
    tank_site_y=opt.TANK.y
    tank=opt.Sprite(4,tank_site_x,tank_site_y,0,0,0,0)
    #tank.x, tank.y,tank.r=tank_site_x,tank_site_y,0
    global number
    number=5
    observed_sprites = opt.TANK.observe(0.05, -0.05, True)
    t=0
    for s in observed_sprites:
        if type(s) == type(opt.BALL):
            t=1
    if opt.TANK.cool_remain==0:
        if tank.distance_to(ball_site_x,ball_site_y)<=3 and \
        opt.TANK.face_enemy_door(0)==True and \
        t==1:
            opt.TANK.do_fire()
        elif tank.distance_to(ball_site_x,ball_site_y)>=5 and\
        (ball_site_y-tank_site_y)*50/(ball_site_x-tank_site_x)+((tank_site_y*ball_site_x)-(tank_site_x*ball_site_y))/(ball_site_x-tank_site_x)>=-8 and \
        (ball_site_y-tank_site_y)*50/(ball_site_x-tank_site_x)+((tank_site_y*ball_site_x)-(tank_site_x*ball_site_y))/(ball_site_x-tank_site_x)<=8 and \
        opt.TANK.face_enemy_door(5)==True and \
        t==1:
            opt.TANK.do_fire()
    print(opt.Bullet.angle)
    
    '''
    if opt.TANK.cool_remain==0 and  tank.distance_to(ball_site_x, ball_site_y)<=3:
            opt.TANK.do_fire()
    '''

    
    return defence(-50,0)




'''
ball_site_x=opt.BALL.x
ball_site_y=opt.BALL.y
tank_site_x=opt.TANK.x
tank_site_y=opt.TANK.y
#判断球与坦克一直线且直线朝向敌方球门条件
(ball_site_y-tank1_y)*50/(ball_site_x-tank1_x)+((tank1_y*ball_site_x)-(tank1_x*ball_site_y))/(ball_site_x-tank1_x)>=-8 and \
(ball_site_y-tank1_y)*50/(ball_site_x-tank1_x)+((tank1_y*ball_site_x)-(tank1_x*ball_site_y))/(ball_site_x-tank1_x)<=8
'''

#如果坦克和球的距离较大
#y=.....根据对方球门中点的坐标和球的坐标构建一次函数y1
#根据函数y1和坦克坐标构建垂直于y1的函数y2
#联立y1和y2求出交点



