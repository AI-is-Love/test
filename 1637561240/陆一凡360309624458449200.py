import opt
# 赢
def attack():
    by = opt.BALL.y
    bx = opt.BALL.x
    tx = opt.TANK.x
    ty = opt.TANK.y
    bvx=opt.BALL.vx
    bvy=opt.BALL.vy

    if judge_wulong(bx,by,tx,ty,bvx,bvy):
        return defend_wulong(bx,by,tx,ty,bvx,bvy)

    if judge_shoot(bx,by,tx,ty,bvx,bvy) and opt.TANK.cool_remain==0:
       print(' i attack fire')
       opt.TANK.do_fire()


    if judge_attaker_in_denfend(bx,by,bvx,bvy):#球在后半场且向后滚动
        if tx<max(0.1,bx-5):   #坦克在球左侧
            if opt.TANK.distance_to(bx,by)>10:
                vs,hs = opt.TANK.goto(bx-5,by)
            else:
                vs,hs = opt.TANK.goto(bx,by)    
            return vs,hs    
        else:  #坦克在球右侧
            if opt.TANK.distance_to(bx,by)>20:
                vs,hs= opt.TANK.goto(-50,0)
            else:
                vs,hs = opt.TANK.goto(max(0.1,bx-30),by)
            return vs,hs

    if judge_attaker_in_center(bx,by,bvx,bvy):#球在前半场且快速后退   
        if opt.TANK.distance_to(bx,by)>20:
            vs,hs= opt.TANK.goto(-50,ty)
            return vs, hs
        

    vs,hs = opt.TANK.goto(bx,by)

    return vs,hs

def deffence1():
    by = opt.BALL.y
    bx = opt.BALL.x
    tx = opt.TANK.x
    ty = opt.TANK.y
    bvx=opt.BALL.vx
    bvy=opt.BALL.vy
    if judge_wulong(bx,by,tx,ty,bvx,bvy):
       return defend_wulong(bx,by,tx,ty,bvx,bvy)

    if judge_shoot(bx,by,tx,ty,bvx,bvy) and opt.TANK.cool_remain==0:
       print(' i defense1 fire')
       opt.TANK.do_fire()
    
    tank = opt.Sprite(0, tx, ty, 1, 1, 0, 1)
    if judge_danger_in_mydoor(bx,by,bvx,bvy):
        if opt.TANK.is_ball_in_range(10000000, tank.angle_to(-50, -10), tank.angle_to(-50, 10)):
            vs, hs = opt.TANK.goto(bx, by)
            vs = -vs
            hs = -hs
            return vs, hs
        else:
            if opt.TANK.is_ball_in_range(2) and  opt.TANK.cool_remain == 0 :
                opt.TANK.do_fire()
            vs, hs = opt.TANK.goto(bx, by)
            return vs, hs

    if (bx <= 0 or  (bx<30 and bvx<-15 ))and -23 <= by <= 23:
        if bx > tx:
            if opt.TANK.distance_to(bx,by)>20:
                time_para=0.3
                vs,hs=far_chase(bx,by,bvx,bvy,tx,ty,time_para)#远距离追球
            else:
                vs, hs = opt.TANK.goto(bx, by)
        else:
            if opt.TANK.is_ball_in_range(2, max(tank.angle_to(-50, -10), tank.angle_to(-50, 10)), min(tank.angle_to(-50, -10), tank.angle_to(-50, 10))):
                print('will wulong')
                vs, hs = opt.TANK.goto(-49, 0)
            else:
                vs, hs = opt.TANK.goto(bx, by)
                if opt.TANK.cool_remain == 0 and opt.TANK.distance_to(bx, by) <= 3:
                    opt.TANK.do_fire()
    else:
        if -8 <= by <= 8:
            vs, hs = opt.TANK.goto(-48, by)
            if opt.TANK.distance_to(-48, by) <= 5:
                vs, hs = 0,0
        elif by > 8:
            vs, hs = opt.TANK.goto(-48, 8)
            if opt.TANK.distance_to(-48, 8) <= 5:
                vs, hs = 0,0
        else:
            vs, hs = opt.TANK.goto(-48, -8)
            if opt.TANK.distance_to(-48, -8) <= 5:
                vs, hs = 0,0
    return vs, hs
    

     

def deffence2():
    by = opt.BALL.y
    bx = opt.BALL.x
    tx = opt.TANK.x
    ty = opt.TANK.y
    bvx=opt.BALL.vx
    bvy=opt.BALL.vy
  
    if judge_wulong(bx,by,tx,ty,bvx,bvy):
        return defend_wulong(bx,by,tx,ty,bvx,bvy)

    if judge_shoot(bx,by,tx,ty,bvx,bvy) and opt.TANK.cool_remain==0:
       print(' i difence2 fire')
       opt.TANK.do_fire()
    
    tank = opt.Sprite(0, tx, ty, 1, 1, 0, 1)
    if judge_danger_in_mydoor(bx,by,bvx,bvy):
        if opt.TANK.is_ball_in_range(2, tank.angle_to(-50, -10), tank.angle_to(-50, 10)):
            vs, hs = opt.TANK.goto(bx, by)
            vs = -vs
            hs = -hs
            print("denfend2 tune back")
            return vs, hs
        else:
            if opt.TANK.is_ball_in_range(2) and  opt.TANK.cool_remain == 0 :
                opt.TANK.do_fire()
            vs, hs = opt.TANK.goto(bx, by)
            return vs, hs

    if judge_safe(bx,by,bvx,bvy):
        if tx>-50:#防止堵在球门里
            vs, hs = opt.TANK.goto(-30, by/1.2)
            if opt.TANK.distance_to(-30, by/1.2) <= 5:
                vs, hs = 0,0
        else:
            vs, hs = opt.TANK.goto(-48, 0)
        return vs, hs

     
    if bx > tx:
        if opt.TANK.is_ball_in_range(20):
            time_para=0.3
            vs, hs = far_chase(bx,by,bvx,bvy,tx,ty,time_para)#远距离追球
        else:
            vs, hs = opt.TANK.goto(bx, by)
        if opt.TANK.cool_remain == 0 and opt.TANK.distance_to(bx, by) <= 2 and judge_shoot_hitball(bx,by,tx,ty,bvx,bvy):
            opt.TANK.do_fire()
            print("denfend2 bx>tx ")


    else:
        if judge_shoot_inmydoor(bx,by,tx,ty,bvx,bvy): #射门的话进自己球门
            vs, hs = opt.TANK.goto(-50, 0)
        else:
            vs, hs = opt.TANK.goto(bx, by)
            if opt.TANK.cool_remain == 0 and opt.TANK.distance_to(bx, by) <= 8 and judge_shoot_hitball(bx,by,tx,ty,bvx,bvy):
                opt.TANK.do_fire()
                print("denfend2 bx<tx")

    return vs, hs
    
    
def tank1_update():
    return attack()


def tank2_update():
    return attack()


def tank3_update():
    return attack()


def tank4_update():
    return deffence2()


def tank5_update():
    return deffence1()   


def judge_safe(bx,by,bvx,bvy):

# 安全
    if bx>0 and bvx>0:
        return 1
    if bx>35:
        return 1
    if bx>-10 and bvx>10:
        return 1
    if bx>-20 and bvx>20:
        return 1
    return 0

def judge_danger_in_mydoor(bx,by,bvx,bvy):
#球在边线且滚向球门
    if bx <= -45 and -23 <= by <= 23:
        if bvy*by<0 :
            return 1
    return 0

def judge_shoot(bx,by,tx,ty,bvx,bvy):
#必须射门了
    alpha1=opt.TANK.angle_to(50,8) #上球门角度
    distance_door=opt.TANK.distance_to(50,0)
    distance_ball=opt.TANK.distance_to(bx,by)
    alpha2=opt.TANK.angle_to(50,-8) #下球门角度
    if abs(alpha1-alpha2)<180:
        d_alpha=abs(alpha1-alpha2)
    else:
        d_alpha=360-abs(alpha1-alpha2)
   # d_alpha=opt.r2a(15/distance_door)
    d_beta=opt.r2a(opt.BALL.radius/distance_ball) # ball 夹角 /2
    #print('debeta',d_beta)
    beta=opt.TANK.angle_to(bx,by) #球对坦克朝向的角度
    if beta<d_beta or beta>360-d_beta: # face BALL
        if alpha1< d_alpha/1.2: # face door
            return 1
    return 0

def judge_attaker_in_denfend(bx,by,bvx,bvy):#球在后半场且向后滚动
    if bx<0 and bvx<-10:
        return 1
    if bx<-20 and bvx<-2:
        return 1
    if bx<-40 and bvx<0:
        return 1
      

    return 0

def judge_attaker_in_center(bx,by,bvx,bvy):#球在前半场且快速后退
    if bx>0 and bvx<-18:
        return 1
    return 0

def far_chase(bx,by,bvx,bvy,tx,ty,time_para):#远距离追球
    xtemp=bx+bvx*time_para
    ytemp=by+bvy*time_para
    vs,hs=opt.TANK.goto(xtemp, ytemp)
    return vs,hs 

def judge_shoot_inmydoor(bx,by,tx,ty,bvx,bvy):
#必须射门了
    alpha1=opt.TANK.angle_to(-50,8) #上球门角度
    distance_door=opt.TANK.distance_to(-50,0)
    distance_ball=opt.TANK.distance_to(bx,by)
    alpha2=opt.TANK.angle_to(-50,-8) #下球门角度
    if abs(alpha1-alpha2)<180:
        d_alpha=abs(alpha1-alpha2)
    else:
        d_alpha=360-abs(alpha1-alpha2)
   # d_alpha=opt.r2a(15/distance_door)
    d_beta=opt.r2a(opt.BALL.radius/distance_ball) # ball 夹角 /2
    #print('debeta',d_beta)
    beta=opt.TANK.angle_to(bx,by) #球对坦克朝向的角度
    if beta<d_beta or beta>360-d_beta: # face BALL
        if alpha2< d_alpha/0.8: # face door
            return 1
    return 0


def judge_shoot_hitball(bx,by,tx,ty,bvx,bvy):

    distance_ball=opt.TANK.distance_to(bx,by)
    d_beta=opt.r2a(opt.BALL.radius/distance_ball) # ball 夹角 /2
    #print('debeta',d_beta)
    beta=opt.TANK.angle_to(bx,by) #球对坦克朝向的角度
    if beta<d_beta or beta>360-d_beta: # face BALL
        return 1
    return 0

def judge_wulong(bx,by,tx,ty,bvx,bvy):
    if bx<-30 and -20<by<20: #球在禁区
        if opt.TANK.distance_to(bx,by)<25: #距离小于xx
            if judge_shoot_hitball(bx,by,tx,ty,bvx,bvy): #坦克面向球
                if judge_shoot_inmydoor(bx,by,tx,ty,bvx,bvy):#射门会进自己球门
                    return 1
    return 0

def defend_wulong( bx,by,tx,ty,bvx,bvy):
    vs,hs=opt.TANK.goto(bx, by)
    vs=-vs
    hs=-hs
    print("wulong", vs,hs)
    return vs,hs