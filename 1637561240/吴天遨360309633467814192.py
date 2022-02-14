import opt
import math

def get_control_speed():
    """
    :param angle: 坦克与足球夹角，范围为[0,360], 逆时针方向
    :return: 坦克的操控值(类似遥控车手柄)
        vs: 取值范围 [-1,+1]，-1 为最大后退力度，1 为最大前进力度，0 保持不动
        hs: 左转右转控制力度。取值范围 [-1,+1]，-1 为最大左转角度，1 为最大右转角度，0 直行。

    注意！当 vs=0，没有前进动力的时候，hs 无论是什么值，无论转多厉害，坦克都在原地不动，都没有效果。
    """
    # TODO: 以下控制方法只是一个随机控制的 demo，完全是看运气！
    #  请按照你的思考，提出你的速度控制方案
 

    vs, hs = opt.TANK.goto(opt.BALL.x-2,opt.BALL.y+2*opt.BALL.y/(50-opt.BALL.x))
    return vs, hs  # vertical_speed, horizontal_speed
 

def attack():
    if opt.BALL.x<-40:
        vs,hs=opt.TANK.goto(-40,opt.BALL.y+5*opt.BALL.y/abs(opt.BALL.y))
    elif opt.TANK.on_east_of(opt.BALL) or abs(opt.TANK.y-opt.BALL.y)>15 or opt.TANK.x>40:
        vs,hs=opt.TANK.goto(opt.BALL.x-5,opt.BALL.y-4*opt.BALL.y/abs(opt.BALL.y))
    elif not opt.TANK.is_ball_in_range(2):
        vs,hs=get_control_speed()
    else:
        vs,hs=opt.TANK.goto(50,0)
        opt.TANK.do_fire()
    
    return vs, hs

def defend():
    vs,hs=opt.TANK.goto(-48,opt.BALL.y)
    return vs,hs

def gate_defend():
    if abs(opt.BALL.y)>8 or opt.BALL.x>-40:
        vs, hs = opt.TANK.goto(-50, 6*opt.BALL.y/abs(opt.BALL.y))
        opt.TANK.a=0
    else:
        vs, hs = opt.TANK.goto(-50, opt.BALL.y)
    return vs,hs

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
    return defend()


def tank4_update():
    """
    坦克4的策略函数，函数内需要实现此坦克的在每一帧的行为策略。
    使用opt库，获得场上比赛状态，根据状态施加你的自定义策略。
    该函数将会在比赛中的每一帧重复调用，直到比赛结束。
    :return: 当前状态下，当前坦克的操控值（前后速度，左右速度）
    """
    return attack()
    
def tank5_update():
    """
    坦克5的策略函数，函数内需要实现此坦克的在每一帧的行为策略。
    使用opt库，获得场上比赛状态，根据状态施加你的自定义策略。
    该函数将会在比赛中的每一帧重复调用，直到比赛结束。
    :return: 当前状态下，当前坦克的操控值（前后速度，左右速度）
    """
    # 当足球远离坦克的时候，坦克返回坐标(-45,0)进行防守
    return gate_defend()
