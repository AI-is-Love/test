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
    if 45 < angle <= 135:
        vs, hs = 0.03, -0.5
    elif 135 < angle <= 225:  
        vs, hs = -1, 0
    elif 225 < angle <= 315:
        vs, hs = 0.03, 0.5
    else:
        if 0 <= angle < 1:
            vs, hs = 1,0.66
        elif 1 <= angle < 2:
            vs,hs = 1,0.64
        elif 2 <= angle < 3:
            vs,hs = 1,0.58
        elif 3 <= angle < 4:
            vs,hs = 1,0.55
        elif 4 <= angle < 5:
            vs,hs = 1,0.5
        elif 5 < angle <= 45:
            vs, hs = 1,0.4
        elif 359 < angle < 360:
            vs, hs = 1,-0.66
        elif 358 <= angle < 359:
            vs,hs = 1,-0.64
        elif 357 <= angle < 358:
            vs,hs = 1,-0.58
        elif 355 <= angle < 356:
            vs,hs = 1,-0.55
        elif 354 <= angle < 355:
            vs,hs = 1,-0.5
        else :
            vs, hs = 1,-0.4
    return vs, hs

def attack():
    target_x = opt.BALL.x
    target_y = opt.BALL.y
    global tank_ball_angle
    tank_ball_angle = opt.TANK.angle_to(opt.BALL.x,opt.BALL.y)
    if opt.TANK.is_stuck(0.25):
        opt.TANK.do_fire()

    if not opt.TANK.is_ball_in_range(4):
        if opt.TANK.on_east_of(opt.BALL):
            target_x, target_y = opt.BALL.x - 1.9, opt.BALL.y - 3
        elif opt.TANK.on_west_of(opt.BALL):
            target_x, target_y = opt.BALL.x - 1.9 , opt.BALL.y + 3
        vs, hs = opt.TANK.goto(target_x, target_y)
    else:
        if opt.TANK.on_east_of(opt.BALL):
            if opt.TANK.y > opt.BALL.y:
                target_x, target_y = opt.BALL.x , opt.BALL.y + 3
            else:
                target_x, target_y = opt.BALL.x , opt.BALL.y - 3
        elif opt.TANK.on_west_of(opt.BALL):
            target_x, target_y = opt.BALL.x - 1 , opt.BALL.y
        vs, hs = attact_control_speed(opt.TANK.angle_to(target_x, target_y))
    return vs, hs

def qiancha():
    if 35 < opt.BALL.x < 50 and -13 < opt.BALL.y <13:
        if opt.TANK.is_stuck(0.25) or (opt.TANK.face_enemy_door() and tank_ball_angle <= 5 and tank_ball_angle >= -5):
            opt.TANK.do_fire()
        if opt.BALL.y > 0:
            vs,hs = opt.TANK.goto(opt.BALL.x,opt.BALL.y-5)
        else:
            vs,hs = opt.TANK.goto(opt.BALL.x,opt.BALL.y+5)
    
    elif 30 <= opt.BALL.x < 46 :
        if opt.BALL.y > 0:
            vs,hs = opt.TANK.goto(opt.BALL.x-12.5,-6)
        else:
            vs,hs = opt.TANK.goto(opt.BALL.x-12.5,6)
    elif (46 < opt.BALL.x < 50 and 0 < opt.BALL.y < 25) or (0 < opt.BALL.x < 50 and 22 < opt.BALL.y < 25) :
        
        vs,hs = opt.TANK.goto(opt.BALL.x-3,-6)

    elif (46 < opt.BALL.x < 50 and -25 < opt.BALL.y < 0) or (0 < opt.BALL.x < 50 and -22 > opt.BALL.y > -25) :

        vs,hs = opt.TANK.goto(opt.BALL.x-3,6)
    elif -15 <= opt.BALL.x < 30 :
        if opt.BALL.y > 0:
            vs,hs = opt.TANK.goto(opt.BALL.x + 3,-6)
        else:
            vs,hs = opt.TANK.goto(opt.BALL.x + 3,6)
    else:
        vs,hs = opt.TANK.goto(10,opt.BALL.y/2)

    return vs,hs

def houwei():
    if opt.TANK.is_stuck(0.25) or (opt.TANK.face_enemy_door() and tank_ball_angle <= 5 and tank_ball_angle >= -5):
        opt.TANK.do_fire()
    if opt.distance(opt.TANK.x, opt.TANK.y, opt.BALL.x, opt.BALL.y) >= 30:
        if x3-30 > 15:
            vs,hs = opt.TANK.goto(-20,opt.BALL.y)
        else:
            vs,hs = opt.TANK.goto(x3-30,opt.BALL.y)
        return vs,hs
    elif opt.TANK.is_ball_in_range(10) and not opt.TANK.face_my_door(-0.05) and opt.BALL.x < 0:
        return attack()
    else:
        vs,hs = opt.TANK.goto(-37.5,opt.BALL.y)
        return vs,hs

def houwei1():
    if opt.TANK.is_stuck(0.25) or (opt.TANK.face_enemy_door() and tank_ball_angle <= 5 and tank_ball_angle >= -5):
        opt.TANK.do_fire()
    if opt.distance(opt.TANK.x, opt.TANK.y, opt.BALL.x, opt.BALL.y) >= 30:
        if x3-20 > 15:
            vs,hs = opt.TANK.goto(5,opt.BALL.y)
        else:
            vs,hs = opt.TANK.goto(x3-20,opt.BALL.y/2)
        return vs,hs
    elif opt.TANK.is_ball_in_range(10) and not opt.TANK.face_my_door() and opt.BALL.x < 0:
        return attack()
    else:
        vs,hs = opt.TANK.goto(-30,opt.BALL.y)
        return vs,hs

def defence():
    target_x = opt.BALL.x
    target_y = opt.BALL.y

    if opt.TANK.is_ball_in_range(15) or opt.TANK.is_stuck(0.25):
        opt.TANK.do_fire() 

    if -50 < target_x < -32.5 and -22 < target_y <22:
        if opt.TANK.on_west_of(opt.BALL):
            if opt.TANK.on_north_of(opt.BALL):
                vs,hs = opt.TANK.goto(target_x-1,target_y)
            if opt.TANK.on_south_of(opt.BALL):
                vs,hs = opt.TANK.goto(target_x-1,target_y)
        elif opt.TANK.on_east_of(opt.BALL):
            target_x, target_y = opt.BALL.x - 1 , opt.BALL.y

            vs, hs = opt.TANK.goto(-50, target_y)
    elif (-50 < target_x < -48 and -25 < target_y < 0) or (-50 < target_x < 0 and -25 < target_y < -23):
        vs ,hs = opt.TANK.goto(-49, -8)
    elif (-50 < target_x < -48 and 0 < target_y < 25) or (-50 < target_x < 0 and 23 < target_y < 25):
        vs ,hs = opt.TANK.goto(-49, 8)

    else:
        if -50 <= opt.TANK.x < -48 and -1 < opt.TANK.y < 1 :
            vs,hs = 0,0
        else:
            vs ,hs = opt.TANK.goto(-50, 0)
    return vs, hs

def tank1_update():
    if opt.BALL.x >-20:  
        return attack()
    else:
        vs,hs = opt.TANK.goto(0, 0)
        return vs,hs

def tank2_update():
    if opt.score()[0] - opt.score()[1] >= 3:
        return houwei1()
    if not opt.TANK.face_my_door(7.9) and opt.TANK.x > -30:
        return attack()
    else:
        return houwei1()

def tank3_update():
    global x3
    x3 = opt.TANK.x
    return qiancha()

def tank4_update():
    return houwei()

def tank5_update():
    return defence()
