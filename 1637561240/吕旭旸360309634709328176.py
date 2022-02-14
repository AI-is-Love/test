import opt
# 赢
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
    if 40 < angle <= 135:
        vs, hs = 1, -0.8
    elif 135 < angle <= 225:
        vs, hs = -1, 0
    elif 225 < angle <= 315:
        vs, hs = 1, 0.8
    else:
        if 315 < angle <= 340:
            vs,hs = 1,0.5
        elif 340 < angle <= 350:
            vs,hs = 1,0.4
        elif 350 < angle <= 355:
            vs,hs = 1,0.3
        elif 355 < angle <= 360:
            vs,hs = 1,-0.2
        elif 20 < angle <= 25:
            vs,hs = 1,-0.5
        elif 10 < angle <= 20:
            vs,hs = 1,-0.4
        elif 5 < angle <= 10:
            vs,hs = 1,-0.3
        elif 0 < angle <= 5:
            vs,hs = 1,-0.2
        else:
            vs,hs = 1,0
  

    return vs, hs

def attack_st():
    if opt.BALL.x < 0:
        return opt.TANK.chase_ball()
    if not opt.TANK.is_ball_in_range(20) and opt.BALL.x > opt.TANK.x and opt.BALL.x > 0:
        return opt.TANK.goto(opt.BALL.x,0)
    else:
        if opt.BALL.x > 48 and -10 <= opt.BALL.y <= 10:
            return opt.TANK.goto(opt.BALL.x, opt.BALL.y)
        else:
            return opt.TANK.goto(40, 0)

def attack():
    target_x = opt.BALL.x
    target_y = opt.BALL.y
    if not opt.TANK.is_ball_in_range(15):
        vs,hs = opt.TANK.chase_ball()
    else:
        if opt.TANK.x > opt.BALL.x:
            if opt.TANK.y > opt.BALL.y:
                vs,hs = opt.TANK.goto(opt.BALL.x -3, opt.BALL.y - 3)
            else:
                vs,hs = opt.TANK.goto(opt.BALL.x -3, opt.BALL.y + 3)
            tank_ball_angle = opt.TANK.angle_to(opt.BALL.x,opt.BALL.y)
            if opt.TANK.face_enemy_door() and tank_ball_angle <= 5 and tank_ball_angle >= -5:
                opt.TANK.do_fire()
            return vs,hs
        else:
            if ( opt.TANK.face_enemy_door() ) and (opt.BALL.y >= opt.ENEMY_DOOR_LEFT.y and opt.BALL.y <= opt.TANK.y) or (opt.BALL.y <= opt.ENEMY_DOOR_RIGHT.y and opt.BALL.y >= opt.TANK.y):
                opt.TANK.do_fire()
            tank_angle_to_football = opt.TANK.angle_to(target_x, target_y)
            vs, hs = attact_control_speed(tank_angle_to_football)
    return vs, hs


def defence_1():
    if opt.TANK.is_ball_in_range(20):
        if opt.TANK.face_enemy_door() and opt.TANK.x < opt.BALL.x:
            if -3 <= opt.TANK.angle_to(opt.BALL.x,opt.BALL.y) <= 3:
                opt.TANK.do_fire() 
            return opt.TANK.goto(opt.BALL.x - 2,opt.BALL.y)
        else:
            if opt.TANK.y > opt.BALL.y:
                return opt.TANK.goto(opt.BALL.x - 3, opt.BALL.y - 6)
            else:
                return opt.TANK.goto(opt.BALL.x - 3, opt.BALL.y + 6)
        return vs, hs
    else:
        return 0,0


def defence_2():

    if opt.TANK.is_ball_in_range(15):
        if opt.TANK.face_enemy_door() and opt.TANK.x < opt.BALL.x:
            if -3 <= opt.TANK.angle_to(opt.BALL.x,opt.BALL.y) <= 3:
                opt.TANK.do_fire() 
            return opt.TANK.goto(opt.BALL.x - 2,opt.BALL.y)
        else:
            if opt.TANK.y > opt.BALL.y:
                return opt.TANK.goto(opt.BALL.x - 3, opt.BALL.y - 6)
            else:
                return opt.TANK.goto(opt.BALL.x - 3, opt.BALL.y + 6)
        return vs, hs
    else:
        return 0,0

def tank1_update():
    global tank1_x
    tank1_x = opt.TANK.x
    if opt.TANK.is_stuck(0.25):
        return -1,0
    if opt.BALL.x < 10:
        if opt.BALL.y >= 0 and opt.BALL.y <= 8:
            return opt.TANK.goto(0,-1)
        elif opt.BALL.y <= 0 and opt.BALL.y >= -8:
            return opt.TANK.goto(0,1)
        else:
            return opt.TANK.goto(0,opt.BALL.y + 2 if opt.BALL.y > 0 else opt.BALL.y - 2)
    else:
        if opt.TANK.is_ball_in_range(50) and opt.TANK.x < opt.BALL.x and opt.TANK.face_enemy_door():
            if not opt.TANK.is_ball_in_range(15):
                return opt.TANK.chase_ball()
            else:
                opt.TANK.do_fire()
                return fix_shoot_angle(opt.BALL.x ,opt.BALL.y)
        else:
            if opt.TANK.x > opt.BALL.x:
                return opt.TANK.goto(opt.BALL.x - 3 ,opt.BALL.y - 2 if opt.BALL.y > 0 else opt.BALL.y + 2)
            else:
                return opt.TANK.chase_ball()


def tank2_update():
    global tank2_x
    tank2_x = opt.TANK.x
    if opt.TANK.is_stuck(0.25) and opt.TANK.face_my_door(7):
        return -1,0
    if opt.BALL.x > 0:
        if opt.TANK.is_ball_in_range(50) and opt.TANK.x < opt.BALL.x and opt.TANK.face_enemy_door():
            if not opt.TANK.is_ball_in_range(15):
                return opt.TANK.chase_ball()
            else:
                opt.TANK.do_fire()
                return fix_shoot_angle(opt.BALL.x ,opt.BALL.y)
        else:
            if opt.TANK.x > opt.BALL.x:
                return opt.TANK.goto(opt.BALL.x - 3 ,opt.BALL.y - 2 if opt.BALL.y > 0 else opt.BALL.y + 2)
            else:
                return opt.TANK.chase_ball()
    else:
        return attack()


def tank3_update():
    global tank1_x
    global tank2_x
    if opt.TANK.is_stuck(0.25):
        return -1,0
    return attack_st()


def tank4_update():
    if opt.TANK.x > -10:
        return opt.TANK.goto(-40,0)
    if opt.BALL.x > 10 or opt.TANK.x > 10 or not opt.TANK.is_ball_in_range(40): 
        if opt.TANK.x < -38.5:
            if opt.TANK.face_enemy_door():
                return 0,0
            else:
                return 0.3,0.8
        return opt.TANK.goto(-40, 0)
    if opt.TANK.is_stuck(0.25) and opt.TANK.x >= -50:
        return -1,0
    return defence_1()


def tank5_update():
    if opt.TANK.x > -38 or opt.TANK.y <= -16 or opt.TANK.y >= 16:
        return opt.TANK.goto(-49,0)
    if opt.BALL.x > 0 or opt.TANK.x > 0 or not opt.TANK.is_ball_in_range(40): 
        if opt.TANK.x < -49.5:
            if opt.TANK.face_enemy_door() and opt.TANK.x > -50:
                return 0,0
            else:
                return 0.3,0.8
        return opt.TANK.goto(-49, 0)
    if opt.TANK.is_stuck(0.25) and opt.TANK.x >= -50:
        return -1,0

    return defence_2()
