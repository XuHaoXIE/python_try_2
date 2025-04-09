#main.py
import hanshu as xxh
import turtle as t
import math

#设置小乌龟窗口的大小
t.setup(width=1000, height=800, startx=350, starty=150)
t.speed(100)
#先画两只写轮眼
#右眼
# 270 < du < 360 , 水平向右的叶子
# jiao = 2 * (360 - du)
xxh.move_pen(0, 50)
my_du = 300
my_jiao = 2 * (360 - my_du)
my_r = 80
yezisize = xxh.yezixian(r = my_r, jiao = my_jiao)
xxh.danyezi(du = my_du, r = my_r, jiao = my_jiao) #画眼睛

xxh.goto_yezi(du = my_du, r = my_r, jiao = my_jiao) #画眼珠子
t.fillcolor('black')
t.begin_fill()
xxh.yuan(40)
t.end_fill()

xxh.yezihua(8, 20, 100, fanwei=360 ,color='red') #画眼珠子内的花纹
t.pensize(3)
t.pencolor('red')
xxh.yezihua(3, 25, 100, fanwei=360 ,color='', ret_2=-1)

#流血效果
xxh.move_pen(180, 40)  #回到眼球的左边
t.pensize(15)
t.setheading(-90)
t.fd(100)
xxh.move_pen(90, 100)
t.pensize(0)
t.pencolor('black')

xxh.move_pen(0, 40)  #回到眼球的中间

#左眼
xxh.move_pen(180, yezisize/2 + 2 * 50) #还得回到原点
# 90 < du < 180, 水平向左的叶子
# jiao = 2 * (180 - du)
my_du = 120
my_jiao = 2 * (180 - my_du)
my_r = 80
xxh.danyezi(du = my_du, r = my_r, jiao = my_jiao) #画眼睛

xxh.goto_yezi(du = my_du, r = my_r, jiao = my_jiao) #画眼珠子
t.fillcolor('black')
t.begin_fill()
xxh.yuan(30)
t.end_fill()

#画花纹
xxh.yezihua(8, 18, 100, fanwei=360 ,color='red')
size = 5
for i in range(0, 121, 30):
    size -= size
    t.pensize(size)
    t.pencolor('blue')
    xxh.yezihua(3, 18, 100, fanwei=360, color='', ret_2=-1, star=i)
t.pencolor('black')

xxh.move_pen(0, yezisize/2 + 50) #回到原点 , 还得多走一半眼睛的长度

xxh.move_pen(90, 100)

#画竖的眼睛
# 0 < du < 90, 垂直向上的叶子
# jiao = 180 - 2 * du
my_du = 45
my_r = 80
my_jiao = 180 - 2 * my_du
yezisize = xxh.yezixian(my_r, my_jiao)
xxh.danyezi(my_du, my_r, my_jiao, color='purple')
xxh.goto_yezi(my_du, my_r, my_jiao)
r=0
while yezisize/2 - r > 0.1:
    xxh.yuan(r)
    r += 5

#去除眼睛外面的曲线
t.fillcolor('white')
t.begin_fill()
t.pencolor('white')
xxh.yuan(yezisize/2, -180, -1, 1)
t.pencolor('black')
t.setheading(my_du)
t.circle(my_r, my_jiao)
t.end_fill()

t.begin_fill()
t.setheading(180 + my_du)
t.circle(my_r, my_jiao)
t.pencolor('white')
t.setheading(0)
t.circle(yezisize/2, -180)
t.end_fill()

t.pencolor('black')
#回到起点
xxh.move_pen(-90, yezisize + 100 + 300)
my_du = 10
my_r = 300
my_jiao = 90 - my_du
xxh.danyezi(my_du, my_r, my_jiao, ret_2=-1)
xxh.danyezi(360 - my_du, my_r, -my_jiao, ret_2=-1)
mt_jiao_rad = math.radians(my_jiao)  #把角度换成弧度
len = my_r * math.sin(mt_jiao_rad)
xxh.move_pen(90, 2*len)
xxh.danyezi(my_du + 180, my_r, my_jiao, ret_2=-1)
xxh.danyezi(360 - (my_du + 180) , my_r, -my_jiao, ret_2=-1)

#画个鼻子嘴巴
t.penup()
t.goto(0, 0)
t.pendown()
t.setheading(-100)
t.fd(150)
t.setheading(30)
t.fd(60)
#嘴巴
t.penup()
t.goto(70, -200)
t.pendown()
t.fillcolor('green')
t.begin_fill()
my_du = 40
my_jiao = -50
my_r = 150
t.setheading(my_du)
t.circle(my_r, my_jiao)
t.setheading(my_du - (-my_jiao/2))     #du - |jiao/2|
xian = xxh.yezixian(my_r, my_jiao)
t.fd(xian)
t.end_fill()
t.done()







