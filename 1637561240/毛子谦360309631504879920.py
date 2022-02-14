import opt
import random

def tank1_update():
    if opt.TANK.x<opt.BALL.x or not opt.TANK.face_my_door():
        return opt.TANK.goto(opt.BALL.x, opt.BALL.y)
    else:
        if opt.TANK.y<opt.BALL.y:
            return opt.TANK.goto(opt.BALL.x, opt.BALL.y+5)
        else:
            return opt.TANK.goto(opt.BALL.x, opt.BALL.y-5)

def tank2_update():
    return opt.TANK.goto(opt.BALL.x, opt.BALL.y)

def tank3_update():
    if opt.TANK.is_stuck(0.22):
        return -1,0
    if (opt.TANK.is_ball_in_range(10) or opt.BALL.x< -15) and not opt.BALL.x>0:
        if opt.TANK.x<opt.BALL.x or not opt.TANK.face_my_door():
            return opt.TANK.goto(opt.BALL.x, opt.BALL.y)
        else:
            if opt.TANK.y < opt.BALL.y:
                return opt.TANK.goto(opt.BALL.x,opt.BALL.y+5)
            else:
                return opt.TANK.goto(opt.BALL.x,opt.BALL.y-5)
    elif opt.BALL.y>0:
        return opt.TANK.goto(min(random.randint(-50,-30),opt.BALL.y),min(opt.BALL.y,8))
    else:
        return opt.TANK.goto(min(random.randint(-50,-30),opt.BALL.y),max(opt.BALL.y,8))
                
def tank4_update():
    if opt.TANK.is_stuck(0.22):
        return -1,0
    if (opt.TANK.is_ball_in_range(10) or opt.BALL.x< -15) and not opt.BALL.x>0:
        if opt.TANK.x<opt.BALL.x or not opt.TANK.face_my_door():
            return opt.TANK.goto(opt.BALL.x, opt.BALL.y)
        else:
            if opt.TANK.y < opt.BALL.y:
                return opt.TANK.goto(opt.BALL.x,opt.BALL.y+5)
            else:
                return opt.TANK.goto(opt.BALL.x,opt.BALL.y-5)
    elif opt.BALL.y>0:
        return opt.TANK.goto(min(random.randint(-50,-30),opt.BALL.y),min(opt.BALL.y,8))
    else:
        return opt.TANK.goto(min(random.randint(-50,-30),opt.BALL.y),max(opt.BALL.y,8))

def tank5_update():
    if opt.TANK.is_stuck(0.22):
        return -1,0
    if (opt.TANK.is_ball_in_range(10) or opt.BALL.x< -15) and not opt.BALL.x>0:
        if opt.TANK.x<opt.BALL.x or not opt.TANK.face_my_door():
            return opt.TANK.goto(opt.BALL.x, opt.BALL.y)
        else:
            if opt.TANK.y < opt.BALL.y:
                return opt.TANK.goto(opt.BALL.x,opt.BALL.y+5)
            else:
                return opt.TANK.goto(opt.BALL.x,opt.BALL.y-5)
    elif opt.BALL.y>0:
        return opt.TANK.goto(min(random.randint(-50,-30),opt.BALL.y),min(opt.BALL.y,8))
    else:
        return opt.TANK.goto(min(random.randint(-50,-30),opt.BALL.y),max(opt.BALL.y,8))
