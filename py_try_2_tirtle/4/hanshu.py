#hanshu.py
import turtle as t
import math

#这个是函数库，用来装我自定义的函数的

#danyezi
#用来画单个闭合的叶子。r和jiao决定了单个叶子的大小
#du决定了叶子的位置（方向）。
#特例
    #0 < du < 90, 垂直向上的叶子
    #jiao = 180 - 2 * du

    #90 < du < 180, 水平向左的叶子
    #jiao = 2 * (180 - du)

    #180 < du < 270, 垂直向下的叶子
    #jiao = 180 - 2 * (du - 180)

    #270 < du < 360 , 水平向右的叶子
    #jiao = 2 * (360 - du)

def danyezi(du , r, jiao, color = '', ret_1 = 1, ret_2 = 1):
    if color != '':
        t.fillcolor(color)
        t.begin_fill()
        t.setheading(du)
        # r和jiao 决定了单个叶子的大小
        t.circle(r, jiao)
        # 叶子反方向闭合
        t.setheading(180 + du)
        t.circle(r, jiao)
        t.end_fill()
    elif color == '':
        if ret_1 == 1:
            t.setheading(du)
            # r和jiao 决定了单个叶子的大小
            t.circle(r, jiao)
        elif ret_1 == -1:
            t.penup()
            t.setheading(du)
            # r和jiao 决定了单个叶子的大小
            t.circle(r, jiao)
            t.pendown()
        if ret_2 == 1:
            # 叶子反方向闭合
            t.setheading(180 + du)
            t.circle(r, jiao)
        elif ret_2 == -1:
            # 叶子不闭合
            t.penup()
            t.setheading(180 + du)
            t.circle(r, jiao)
            t.pendown()



#yezihua
#num 代表叶子的数量， r和jiao 决定了单个叶子的大小, fanwei默认为360，代表叶子/
#出现在一圈，也可以传入180,代表叶子出现在半圈内。！注意范围只能填360 or 180./
# color选填，代表给叶子填充颜色
def yezihua(num, r, jiao, fanwei = 360, color = '', ret_1=1,ret_2=1, star = 0):
    #fanwei 只能填360 或 180
    if fanwei != 360 and fanwei != 180:
        print('fanwei can only be 360 and 180')
        exit(10086)
    #jiao建议小于180，不然就不是叶子了
    if jiao > 180:
        pass
    if jiao <= 0:
        print('jiao 不能小于等于0！')
        exit(10087)
    jiange = int(fanwei/num)
    for i in range(star, fanwei + star, jiange):
        if color != '':
            danyezi(i, r, jiao, color = color)
        elif color == '':
            danyezi(i, r, jiao, ret_1 = ret_1, ret_2 = ret_2)

#使用此函数可轻松获得叶子的弦长，用于画和叶子顶端完全重合的圆，或者通过\
#弦长可以轻松判断圆在叶子的里外
def yezixian(r, jiao):
    #注意的是r和jiao其实就是yezihua函数的r和jiao，用于控制叶子大小的
    # c = (a**2 + b**2 -2*a*b*cos(rad))**(1/2)   余弦公式
    #jiao 是度数，需要把他转换为弧度，才可以用cos函数
    jiao_rad = math.radians(jiao)
    xian = (r**2 + r**2 -2*r*r*math.cos(jiao_rad))**(1/2)
    return xian

#以当前点为圆心，画半径为yuan_r，逆时针（正方向）度数为yuan_jiao的圆（残次圆）
def yuan(yuan_r, yuan_jiao = 360, ret = 1, up = -1):
    #用相对走，而非绝对坐标goto（0,yuan_r）,因为我需要以当前点为圆心
    t.penup()
    if up == -1:   #从下面开始画圆
        t.setheading(-90)
        t.fd(yuan_r)
        t.setheading(0)
    else:
        t.setheading(90)   #从上面开始画圆
        t.fd(yuan_r)
        t.setheading(180)
    t.pendown()
    t.circle(yuan_r, yuan_jiao)
    if ret == 1:
        # 回到原来的地点
        t.penup()
        if up == -1:
            t.setheading(90)
        else:
            t.setheading(-90)
        t.fd(yuan_r)
        t.setheading(0)
        t.pendown()



#立即走向叶子中心
def goto_yezi(du, r, jiao):
    if du > 180:
        set_du = jiao/2 - (360 - du)
    elif 0 <= du <= 180:
        set_du = jiao/2 + du
    t.penup()
    t.setheading(set_du)
    xian = yezixian(r, jiao)
    t.fd(xian/2)
    t.pendown()

#移动画笔
def move_pen(du, distan):
    t.penup()
    t.setheading(du)
    t.fd(distan)
    t.pendown()

def zhexian(cishu, in_jiao, out_jiao, in_len, out_len = ''):
    if out_len == '':
        out_len = in_len
    for i in range(cishu):
        t.right(180 - in_jiao)
        t.fd(in_len)
        t.left(180 - out_jiao)
        t.fd(out_len)

#画中间带圆的花瓣
def xiangrikui(num, r, jiao, cir_r,fanwei = 360, color = '', ret_1=1,ret_2=1, star = 0, cir_color=''):
    #fanwei 只能填360 或 180
    if fanwei != 360 and fanwei != 180:
        print('fanwei can only be 360 and 180')
        exit(10086)
    #jiao建议小于180，不然就不是叶子了
    if jiao > 180:
        pass
    if jiao <= 0:
        print('jiao 不能小于等于0！')
        exit(10087)
    jiange = int(fanwei/num)
    for i in range(star, fanwei + star, jiange):
        if color != '':
            danyezi(i, r, jiao, color=color)
            t.setheading(90 + jiao / 2 + i)
            t.circle(cir_r, jiange)
        elif color == '':
            danyezi(i, r, jiao, ret_1 = ret_1, ret_2 = ret_2)
            t.setheading(90 + jiao / 2 + i)
            t.circle(cir_r, jiange)
    if cir_color != '':
        t.fillcolor(cir_color)
        t.begin_fill()
        t.circle(cir_r)
        t.end_fill()


     
