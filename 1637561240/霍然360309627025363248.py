import opt
import math
# 赢

def attact_control_speed(angle):
    """
    :param angle: 坦克与足球夹角，范围为[0,360], 逆时针方向
    :return: [垂直速度，水平速度]
    """
    # 45°至135°，足球在坦克左方
    if 40 < angle <= 135:
        vs, hs = 0.3, -1  # vertical_speed, horizontal_speed
    # 135°至225°，足球在坦克后方
    elif 135 < angle <= 225:
        vs, hs = -1, 0
    # 225°至315°，足球在坦克右方
    elif 225 < angle <= 315:
        vs, hs = 0.3, 1
    else:  # 315°至45°，足球在坦克正前方
        vs, hs = 1, 0
    return vs, hs  # vertical_speed, horizontal_speed


def attack():
    """
    坦克的策略函数，函数内需要实现此坦克的在每一帧的行为策略。
    使用opt库，获得场上比赛状态，根据状态施加你的自定义策略。
    该函数将会在比赛中的每一帧重复调用，直到比赛结束。
    :return: 当前状态下，当前坦克的操控值（前后速度，左右速度）
    """
    """
    target_x = opt.BALL.x
    target_y = opt.BALL.y
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
    """
    """大约十分之一秒的时间呼叫运行一次!

    这里面最麻烦的并不是控制逻辑,而是坦克和球的运动姿态难于判断,需要反复尝试中,
    不断的修改代码
    """
    # print("version 2.0")
    [vs, hs] = [0, 0]
    [vs, hs] = goto_right_position()

    return vs, hs


def defence():
    """
    坦克的策略函数，函数内需要实现此坦克的在每一帧的行为策略。
    使用opt库，获得场上比赛状态，根据状态施加你的自定义策略。
    该函数将会在比赛中的每一帧重复调用，直到比赛结束。
    :return: 当前状态下，当前坦克的操控值（前后速度，左右速度）
    """
    # 设定40是一个经验值,当球通过我方半场,我方开始反应,转向加上瞄准,速度提起来,提前量在40比较好
    if opt.BALL.distance_to(-50, 0) < 40:
        [vs, hs, is_right_position] = defend_strategy.goto_right_position()

    else:
        if(opt.TANK.distance_to(-50, 0)<=3):
            tank_angle_to_football = opt.TANK.angle_to(opt.BALL.x, opt.BALL.y)
            [vs,hs] = attact_control_speed(tank_angle_to_football)
            vs = 0.1
        else:
            # 返回球门中间
            [vs, hs] = opt.TANK.goto(-50, 0)
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
    return attack()


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
    return defence()


class defend_strategy:
    @classmethod
    def target_position(self, offset=6, reference_x=50, reference_y=0):
        """计算坦克移动位置点!

        offset, 当前足球的x轴位置,减去offset等于是想象足球的移动量,该数据通过实验取得,大概在1-6之间
        refrence_x,参考点的x轴坐标,这里的参考点指的是球门的位置中心点
        refrence_y,参考点的y轴坐标,这里的参考点指的是球门的位置中心点
        """
        target_x = opt.BALL.x - offset
        if (opt.BALL.x - reference_x) != 0:
            target_y = int(
                opt.BALL.y + (reference_y - opt.BALL.y) * offset / (opt.BALL.x - reference_x)
            )
        else:
            target_y = opt.BALL.y

        #先在y轴上接近球，然后再迎上去
        if(abs(opt.TANK.y-target_y)>=3):
            target_x = opt.TANK.x
        # 假如目标位置超过x轴边界,则把offset加到y轴
        if (target_x > 50) or (target_x < -50):
            target_x = opt.BALL.x
            if opt.BALL.y > 0:
                target_y = opt.BALL.y + offset
            else:
                target_y = opt.BALL.y - offset
            # 假如目标x轴,y轴都超出边界,说明球已经到了角落,先把球撞出来再说吧
        if (target_y > 25) or (target_y < -25):
            target_y = opt.BALL.y
        
        return target_x, target_y

    @classmethod
    def goto_right_position(self, offset=3):
        """坦克移动到争取位置!

        offset: 当前足球的x轴位置,减去offset等于是想象足球的移动量,该数据通过实验取得,大概在1-6之间
        """
        [vs, hs] = [0, 0]
        is_right_position = True
        [target_x, target_y] = target_position(offset, 50, 0)
        if(opt.TANK.distance_to(opt.BALL.x,opt.BALL.y)>10):
            [vs, hs] = opt.TANK.goto(target_x, target_y, 0, 0.8, 0.5)
           #[vs,hs] = opt.TANK.chase_ball()
        else:
            [vs, hs] = opt.TANK.goto(target_x, target_y, 0, 0.8, 0.5)
        if opt.TANK.distance_to(target_x, target_y) < 1:
            is_right_position = True

        return vs, hs, is_right_position


class StateMachine:
    """用来做状态机的全局变量!"""

    state = int(0)
    target_x = -99  # 不可能存在的数
    target_y = -99
    in_position = True
    attack_state = int(0)


def target_position(offset=6, reference_x=50, reference_y=0):
    """计算坦克移动位置点!

    offset, 当前足球的x轴位置,减去offset等于是想象足球的移动量,该数据通过实验取得,大概在1-6之间
    refrence_x,参考点的x轴坐标,这里的参考点指的是球门的位置中心点
    refrence_y,参考点的y轴坐标,这里的参考点指的是球门的位置中心点
    """
    
    if opt.TANK.x < opt.BALL.x:  # TANK 在球的西边
        # 因为地方的球门位置处,x轴为50,所以球的位置无论如何都不应该超过50
        reference_x = 55
        target_x = round(opt.BALL.x - offset, 2)
        if (opt.BALL.x - reference_x) != 0:
            target_y = int(
                opt.BALL.y
                + (reference_y - opt.BALL.y) * offset / (opt.BALL.x - reference_x)
            )

        else:
            target_y = int(opt.BALL.y)

        # 假如目标位置超过x轴边界,则把offset加到y轴
        if (target_x > 50) or (target_x < -50):
            target_x = opt.BALL.x
            if opt.BALL.y > 0:
                target_y = int(opt.BALL.y + offset)
            else:
                target_y = int(opt.BALL.y - offset)
        # 假如目标x轴,y轴都超出边界,说明球已经到了角落,先把球撞出来再说吧
        if (target_y > 25) or (target_y < -25):
            target_y = opt.BALL.y
    else:  # tank在球的东边
        if(abs(opt.TANK.y - opt.BALL.y)>3):
            [target_x, target_y] = [opt.BALL.x - offset, opt.TANK.y]
       
        elif(opt.TANK.y>0):
            [target_x, target_y] = [opt.TANK.x, opt.TANK.y-5]
        else:
            [target_x, target_y] = [opt.TANK.x, opt.TANK.y+5]
    return target_x, target_y


def stuck_process():
    """坦克堵死后的处理方式!

    堵死后,如果让坦克追球,坦克就会做出追球的举动.但如果马上放手不管,坦克就又会返回原地堵死.
    所以,如果坦克堵死后.会在2秒钟的时间内做出追球的动作,然后再返回正常的控制逻辑
    """
    [vs, hs] = [0, 0]
    if opt.TANK.cool_remain == 0:
        v_tank_degree = opt.TANK.angle_to(opt.BALL.x, opt.BALL.y)
        if (
            v_tank_degree < 5
            or v_tank_degree > 355
            and opt.TANK.distance_to(opt.BALL.x, opt.BALL.y) < 40
        ):
            if opt.TANK.cool_remain == 0 and opt.TANK.face_enemy_door() == True:
                opt.TANK.do_fire()
        else:#有子弹先打球,后打敌人坦克
            tanks = opt.enemy_tanks()
            for tank in tanks:
                v_tank_degree = opt.TANK.angle_to(tank.x, tank.y)
                if (
                    v_tank_degree < 5
                    or v_tank_degree > 355
                    and opt.TANK.distance_to(tank.x, tank.y) < 10
                ):
                    if opt.TANK.cool_remain == 0 and opt.TANK.face_enemy_door(7) >=0:
                        opt.TANK.do_fire()
            
    if opt.TANK.x < opt.BALL.x:  # TANK 在球的西边    
        [vs, hs] = opt.TANK.chase_ball()#坦克在球的西边,又堵住了去路,这是没错的,反正是去顶球
    else:#坦克在球的东边,这时候一旦堵住,有可能是顶住球了.
        [target_x, target_y] = target_position()
        angle = opt.TANK.angle_to(target_x, target_y)
        [vs,hs] = attact_control_speed(angle)
    return [vs, hs]


def control_parameters_setup(vt, dt, vb, db):
    """实时返回设定控制参数

    vt:坦克速度
    dt:坦克与敌人球门的角度
    vb:球速
    db:球与坦克的角度,逆时针旋转.
    offset: 球运动的时候,坦克追上去不能追球现在的位置,需要预估一个提前量,offset即球当前x值补偿的提前量
    distance:依据坦克与足球的距离,设定了两种控制策略,离球远,大油门跟上,离球进,速度要慢,坦克位置调整要精细
    in_range_throttle:坦克与球足够近后,设定的最大油门,(0-1)
    in_range_angle_acceleration:坦克与球足够近后,设定最大的角度调整力度(0-1)
    out_range_throttle:坦克与球很远,设定的最大油门(0-1)
    out_range_angle_acceleration:坦克与球很远,设定最大的角度调整力度(0-1)
    """
    # offset,缩写为os,主要是怕返回时,语句太长,看的眼晕
    os = 0
    # distance
    ds = 2
    # in_range_throttle
    irt = 0.7
    # in_range_angle_acceleration
    iraa = 0.4
    # out_range_throttle
    ort = 1
    # out_range_angle_acceleration
    oraa = 0.3

    if opt.TANK.x < opt.BALL.x:  # TANK 在球的西边
        if vb == 0:  # 假如球静止不动
            [os, ds, irt, iraa, ort, oraa] = [-1, 2, 0.7, 0.4, 1, 0.5]
        elif vb <= 10:  # 球速小于10
            [os, ds, irt, iraa, ort, oraa] = [1, 3, 0.6, 0.4, 0.8, 0.5]
        else:
            [os, ds, irt, iraa, ort, oraa] = [2, 3, 0.9, 0.3, 1, 0.4]
    else:  # TANK 在球的东边
        if vb == 0:  # 假如球静止不动
            [os, ds, irt, iraa, ort, oraa] = [-1, 2, 0.7, 0.4, 1, 0.5]
        elif vb <= 10:  # 球速小于10
            [os, ds, irt, iraa, ort, oraa] = [5, 2, 0.6, 0.4, 0.8, 0.5]
        else:
            [os, ds, irt, iraa, ort, oraa] = [7, 4, 1, 0.3, 1, 0.4]
        
    return [os, ds, irt, iraa, ort, oraa]


def goto_right_position():
    """坦克在球的西边的处理方式!

    vt:坦克速度
    dt:坦克与敌人球门的角度
    vb:球速
    db:球与坦克的角度,逆时针旋转.
    预判球的运动轨迹,让坦克向提前量出发.
    从球门的正中心,坐标点为(50,0),到预估坦克和球相遇时球的坐标,画一条直线,坦克沿这条直线
    撞球,将球撞入球门
    """
    [vt, dt, vb, db] = calc_speed()
    enemy_door_x = 50
    enemy_door_y = 0
    [vs, hs] = [0, 0]
    if(opt.TANK.is_stuck(2)):
        [vs,hs] = stuck_process()
    else:

        
        [os, ds, irt, iraa, ort, oraa] = control_parameters_setup(vt, dt, vb, db)
        offset = os
        distance = ds
        in_range_throttle = irt
        in_range_angle_acceleration = iraa
        out_range_throttle = ort
        out_range_angle_acceleration = oraa

        # target_x,target_y 坦克的移动目标
        [target_x, target_y] = target_position(offset, enemy_door_x, enemy_door_y)
        if opt.TANK.is_ball_in_range(distance):
            [vs, hs] = opt.TANK.goto(
                target_x,
                target_y,
                0,
                in_range_throttle,
                in_range_angle_acceleration,
            )
            if StateMachine.state >= 20:
                vs = 0  # 追球跑一阵子,然后减速,来开距离后再追,否则无法从斜后方攻击球身
                #print("stopped")
                StateMachine.state = 0
            else:
                StateMachine.state = StateMachine.state + 1
        else:
            [vs, hs] = opt.TANK.goto(
                target_x,
                target_y,
                0,
                out_range_throttle,
                out_range_angle_acceleration,
            )

    return [vs, hs]


def calc_speed():
    """返回坦克和足球的速度,角度!

    计算坦克和足球的速度,可以用来判读足球和坦克处于运动还是静止状态.但是角度好像没什么用处
    .比方说,即便知道了坦克和足球的夹角,这个夹角本来是用来计算绕开障碍物路径的.但是有什么用处?
    进一个球只给3秒钟的时间,调个头,再稳定下来,就得好几秒.
    """
    [v_tank, v_tank_degree, v_ball, v_ball_degree] = [0, 0, 0, 0]
    vx = opt.TANK.vx
    vy = opt.TANK.vy
    v_tank = math.sqrt(math.pow(vx, 2) + math.pow(vy, 2))
    v_tank_degree = opt.relative_angle(opt.TANK.x, opt.TANK.y, 0, 50, 0)  # 50,0 是对方球门

    vx = opt.BALL.vx
    vy = opt.BALL.vy
    v_ball = math.sqrt(math.pow(vx, 2) + math.pow(vy, 2))
    v_ball_degree = opt.relative_angle(
        opt.TANK.x, opt.TANK.y, 0, opt.BALL.x, opt.BALL.y
    )  # 50,0 是对方球门
    return [v_tank, v_tank_degree, v_ball, v_ball_degree]
