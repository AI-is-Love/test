import opt
# 输
def get_control_speed(): 
    vs,hs=opt.TANK.chase_ball()
    return vs,hs
def attack_enemy1():   
    vs,hs = get_control_speed()
    if opt.TANK.cool_remain==0 and isline():
        opt.TANK.do_fire()
    return vs,hs
def attack_enemy2():        
    vs,hs = opt.TANK.goto(47,5)
    if abs(opt.BALL.y-5)<1:
        vs,hs=opt.TANK.chase_ball()
    if opt.TANK.cool_remain==0 and isline():
        opt.TANK.do_fire()
    return vs,hs
def attack_my(x,y):
    vs,hs=opt.TANK.goto(x,y)
    return vs,hs
def isline():
    k=(opt.BALL.y-opt.TANK.y)/(opt.BALL.x-opt.TANK.x)
    b=opt.BALL.y-k*opt.BALL.x
    if abs((k*50)+b)<7 and opt.TANK.face_enemy_door():
        return True
    else:
        return False
def goalkeeper(x,y):
    if opt.BALL.x<-20 and -20<opt.BALL.y<20:
        vs,hs=opt.TANK.chase_ball()
    else:
        vs,hs=opt.TANK.goto(x,y)
    if opt.TANK.cool_remain==0 and isline():
        opt.TANK.do_fire()
    return vs, hs
def tank1_update():
    if opt.BALL.x<-30:   
        return attack_my(-25,opt.TANK.y)
    else:
        return attack_enemy1()
    return vs,hs
def tank2_update():
    if opt.BALL.x<-30:   
        return attack_my(-25,opt.TANK.y)
    else:
        return attack_enemy1()
    return vs,hs
def tank3_update():
    if opt.BALL.x<-30:   
        return attack_my(-25,opt.TANK.y)
    else:
        return attack_enemy1()
def tank4_update():
    if opt.BALL.x<-30:   
        return goalkeeper(-42,0)
    else:
        return attack_enemy2()
def tank5_update():
    return goalkeeper(-52,0)