import opt
# 赢 输

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
    #  225°至315°，足球在坦克右方
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
    
    door_x = (opt.ENEMY_DOOR_LEFT.x + opt.ENEMY_DOOR_RIGHT.x) / 2
    door_y = (opt.ENEMY_DOOR_LEFT.y + opt.ENEMY_DOOR_RIGHT.y) / 2
    
    if opt.distance(opt.BALL.x, opt.BALL.y, opt.TANK.x, opt.TANK.y) < 3 :
        vs,hs = opt.TANK.goto(door_x, door_y)
    else :
        vs,hs = opt.TANK.goto(opt.BALL.x, opt.BALL.y)
        
    return vs,hs 
def defence():
    """
    坦克的策略函数，函数内需要实现此坦克的在每一帧的行为策略。
    使用opt库，获得场上比赛状态，根据状态施加你的自定义策略。
    该函数将会在比赛中的每一帧重复调用，直到比赛结束。
    :return: 当前状态下，当前坦克的操控值（前后速度，左右速度）
    """
    target_x = opt.BALL.x
    target_y = opt.BALL.y
    vs,hs=opt.TANK.goto(-50,target_y)
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
    
    return defence()


def tank4_update():
    """
    坦克4的策略函数，函数内需要实现此坦克的在每一帧的行为策略。
    使用opt库，获得场上比赛状态，根据状态施加你的自定义策略。
    该函数将会在比赛中的每一帧重复调用，直到比赛结束。
    :return: 当前状态下，当前坦克的操控值（前后速度，左右速度）
    """
    
    return defence()


def tank5_update():
    """
    坦克5的策略函数，函数内需要实现此坦克的在每一帧的行为策略。
    使用opt库，获得场上比赛状态，根据状态施加你的自定义策略。
    该函数将会在比赛中的每一帧重复调用，直到比赛结束。
    :return: 当前状态下，当前坦克的操控值（前后速度，左右速度）
    """
    return defence()

    



