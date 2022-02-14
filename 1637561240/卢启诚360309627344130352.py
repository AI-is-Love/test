import opt
# 赢 赢
def attact_control_speed(angle):
    if 40 < angle <= 135:
        vs, hs = 0.3, -1    
    elif 135 < angle <= 225:
        vs, hs = -1, 0
    elif 225 < angle <= 315:
        vs, hs = 0.3, 1
    else: 
        vs, hs = 1, 0
    return vs, hs
def aattack():
    target_x = opt.BALL.x
    target_y = opt.BALL.y
    if target_x > -40:
        if not opt.TANK.is_ball_in_range(2):
            tank_angle_to_football = opt.TANK.angle_to(target_x, target_y)
            vs, hs = attact_control_speed(tank_angle_to_football)
            if  opt.TANK.observe(20,-20):
                opt.TANK.do_fire()
            else:
                opt.TANK.not_fire()
        else:
            if not opt.TANK.on_east_of(opt.BALL):
                target_x, target_y = opt.BALL.x - 3, opt.BALL.y
        tank_angle_to_football = opt.TANK.angle_to(target_x, target_y)
        vs, hs = attact_control_speed(tank_angle_to_football)
        if  opt.TANK.observe(20,-20):
            opt.TANK.do_fire()
        else:
            opt.TANK.not_fire()
    else:
        vs, hs = opt.TANK.goto(-12.5, 12.5)
        opt.TANK.face_enemy_door()
        if  opt.TANK.observe(20,-20):
            opt.TANK.do_fire()
        else:
            opt.TANK.not_fire()
    return vs, hs   
def battack():
    target_x = opt.BALL.x
    target_y = opt.BALL.y
    if target_x > -40:
        if not opt.TANK.is_ball_in_range(2):
            tank_angle_to_football = opt.TANK.angle_to(target_x, target_y)
            vs, hs = attact_control_speed(tank_angle_to_football)
            if  opt.TANK.observe(20,-20):
                opt.TANK.do_fire()
            else:
                opt.TANK.not_fire()
        else:
            if not opt.TANK.on_east_of(opt.BALL):
                target_x, target_y = opt.BALL.x - 3, opt.BALL.y
        tank_angle_to_football = opt.TANK.angle_to(target_x, target_y)
        vs, hs = attact_control_speed(tank_angle_to_football)
        if  opt.TANK.observe(20,-20):
            opt.TANK.do_fire()
        else:
            opt.TANK.not_fire()
    else:
        vs, hs = opt.TANK.goto(-12.5, -12.5)
        opt.TANK.face_enemy_door()      
        if  opt.TANK.observe(20,-20):
            opt.TANK.do_fire()
        else:
            opt.TANK.not_fire()
    return vs, hs
def tankadefence():
    target_x = opt.BALL.x
    target_y = opt.BALL.y
    if target_x > 35:
        vs, hs = opt.TANK.goto(-37.5, 12.5)
        opt.TANK.face_enemy_door()
        if  opt.TANK.observe(20,-20):
            opt.TANK.do_fire()
        else:
            opt.TANK.not_fire()
    else:
        if opt.BALL.y >= 0:
            vs, hs = opt.TANK.policy1(-48, 2, 1, 1)
            vs, hs = opt.TANK.chase_ball()
            if  opt.TANK.observe(20,-20):
                opt.TANK.do_fire()
            else:
                opt.TANK.not_fire()
        else:
            if not opt.TANK.is_ball_in_range(10):
                vs, hs = opt.TANK.chase_ball()
                if  opt.TANK.observe(20,-20):
                    opt.TANK.do_fire()
                else:
                    opt.TANK.not_fire()
            else:
                vs, hs = opt.TANK.policy1(-48, 1, 1, 1)
                vs, hs = opt.TANK.chase_ball()
                if  opt.TANK.observe(20,-20):
                    opt.TANK.do_fire()
                else:
                    opt.TANK.not_fire()
    return vs, hs

def tankbdefence():
    target_x = opt.BALL.x
    target_y = opt.BALL.y
    if target_x > 35:
        vs, hs = opt.TANK.goto(-37.5, -12.5)
        opt.TANK.face_enemy_door()
        if  opt.TANK.observe(20,-20):
            opt.TANK.do_fire()
        else:
            opt.TANK.not_fire()
    else:
        if opt.BALL.y >= 0:
            
            vs, hs = opt.TANK.policy1(-48, 2, 1, 1)
            
            vs, hs = opt.TANK.chase_ball()
            if  opt.TANK.observe(20,-20):
                opt.TANK.do_fire()
            else:
                opt.TANK.not_fire()
        else:
            
            if not opt.TANK.is_ball_in_range(10):
                
                vs, hs = opt.TANK.chase_ball()
                if  opt.TANK.observe(20,-20):
                    opt.TANK.do_fire()
                else:
                    opt.TANK.not_fire()   
            else:
                
                vs, hs = opt.TANK.policy1(-48, 1, 1, 1)
                
                vs, hs = opt.TANK.chase_ball() 
                if  opt.TANK.observe(20,-20):
                    opt.TANK.do_fire()
                else:
                    opt.TANK.not_fire()
    return vs, hs

def goalkeeper():
    
    target_x = opt.BALL.x
    
    target_y = opt.BALL.y
    
    if target_x < -20:
        if target_y <= -8:
         
            vs, hs = opt.TANK.goto(-50, -8)
            if  opt.TANK.observe(20,-20):
                opt.TANK.do_fire()
            else:
                opt.TANK.not_fire()
        elif target_y <= -7:
         
            vs, hs = opt.TANK.goto(-50, -7)
            if  opt.TANK.observe(20,-20):
                opt.TANK.do_fire()
            else:
                opt.TANK.not_fire()
        elif target_y <= -6:
         
            vs, hs = opt.TANK.goto(-50, -6)
            if  opt.TANK.observe(20,-20):
                opt.TANK.do_fire()
            else:
                opt.TANK.not_fire()
        elif target_y <= -5:
         
            vs, hs = opt.TANK.goto(-50, -5)
            if  opt.TANK.observe(20,-20):
                opt.TANK.do_fire()
            else:
                opt.TANK.not_fire()
        elif target_y <= -4:
         
            vs, hs = opt.TANK.goto(-50, -4)
            if  opt.TANK.observe(20,-20):
                opt.TANK.do_fire()
            else:
                opt.TANK.not_fire()
        elif target_y <= -3:
         
            vs, hs = opt.TANK.goto(-50, -3)
            if  opt.TANK.observe(20,-20):
                opt.TANK.do_fire()
            else:
                opt.TANK.not_fire()
        elif target_y <= -2:
         
            vs, hs = opt.TANK.goto(-50, -2)
            if  opt.TANK.observe(20,-20):
                opt.TANK.do_fire()
            else:
                opt.TANK.not_fire()
        elif target_y <= -1:
         
            vs, hs = opt.TANK.goto(-50, -1)
            if  opt.TANK.observe(20,-20):
                opt.TANK.do_fire()
            else:
                opt.TANK.not_fire()         
        elif target_y >= 0:
         
            vs, hs = opt.TANK.goto(-50, 0)
            if  opt.TANK.observe(20,-20):
                opt.TANK.do_fire()
            else:
                opt.TANK.not_fire()
    
        elif target_y >= 1:
         
            vs, hs = opt.TANK.goto(-50, 1)
            if  opt.TANK.observe(20,-20):
                opt.TANK.do_fire()
            else:
                opt.TANK.not_fire()
        elif target_y >= 2:
         
            vs, hs = opt.TANK.goto(-50, 2)
            if  opt.TANK.observe(20,-20):
                opt.TANK.do_fire()
            else:
                opt.TANK.not_fire()
        elif target_y >= 3:
         
            vs, hs = opt.TANK.goto(-50, 3)
            if  opt.TANK.observe(20,-20):
                opt.TANK.do_fire()
            else:
                opt.TANK.not_fire()
        elif target_y >= 4:
         
            vs, hs = opt.TANK.goto(-50, 4)
            if  opt.TANK.observe(20,-20):
                opt.TANK.do_fire()
            else:
                opt.TANK.not_fire()
        elif target_y >= 5:
         
            vs, hs = opt.TANK.goto(-50, 5)
            if  opt.TANK.observe(20,-20):
                opt.TANK.do_fire()
            else:
                opt.TANK.not_fire()
        elif target_y >= 6:
         
            vs, hs = opt.TANK.goto(-50, 6)
            if  opt.TANK.observe(20,-20):
                opt.TANK.do_fire()
            else:
                opt.TANK.not_fire()
        elif target_y >= 7:
         
            vs, hs = opt.TANK.goto(-50, 7)
            if  opt.TANK.observe(20,-20):
                opt.TANK.do_fire()
            else:
                opt.TANK.not_fire()
        else:
         
            vs, hs = opt.TANK.goto(-50, 8)
            if  opt.TANK.observe(20,-20):
                opt.TANK.do_fire()
            else:
                opt.TANK.not_fire()
        
    else:
        
        vs, hs = opt.TANK.goto(-50, 0)
        vs, hs = 0, 0
        if  opt.TANK.observe(20,-20):
            opt.TANK.do_fire()
        else:
            opt.TANK.not_fire()
    return vs, hs

def tank1_update():
   
    return aattack()
    
def tank2_update():
    
    return battack()
    
def tank3_update():
    
    return tankadefence()    
    
def tank4_update():
    
    return tankbdefence()
def tank5_update():

    return goalkeeper()
    