#coding=gbk
#画菱形
import turtle as t
'''
t.setup(width=0.5, height=0.75, startx = 0.3, starty = 100)
t.goto(100,100)
t.goto(100,-100)
t.goto(-100,-100)
t.goto(-100,100)
t.goto(0,0)
t.seth(45)
t.fd(100 * 2**(1/2) )
t.seth(-90)
t.fd(200)
t.seth(180)
t.fd(200)
t.seth(90)
t.fd(200)
t.seth(-45)
t.fd(100 * 2**(1/2) )
t.done()
'''
'''
#画毛毛虫
t.setup(650,350,200,200)
t.penup()
t.fd(-250)
t.pendown()
t.pensize(25)
t.seth(-40)
for i in range(4):
    t.pencolor('yellow')
    t.circle(40,80)
    t.pencolor('gold')
    t.circle(-40,80)
t.circle(40,80/2)
t.fd(40)
t.circle(32,180)
t.fd(40*2/3)
t.done()
'''

#画爱心
'''
t.pensize(0)
t.fillcolor('red')
t.begin_fill()
t.seth(10)
t.circle(80,80)
t.seth(90)
t.circle(80/2,180)
t.seth(90)
t.circle(80/2,180)
t.circle(80,100)
t.end_fill()
t.done()'''





#画花
t.speed(0)
t.goto(0,-200)

t.goto(0,-150)
t.setheading(20)
t.fillcolor('green')
t.begin_fill()
t.right(30)
t.circle(120,60)
t.left(120)
t.circle(120,60)
t.end_fill()

t.goto(0,-130)
t.seth(-200)
#t.setheading(-200)
t.fillcolor('green')
t.begin_fill()
t.right(30)
t.circle(120,60)
t.left(120)
t.circle(120,60)
t.end_fill()

t.goto(0,20)
t.setheading(0)
#t.seth(90)
t.fillcolor('yellow')
for r in range(20, 361, 20):
    t.begin_fill()
    t.circle(40, 20)
    t.right(120)
    t.circle(120,60)
    t.left(120)
    t.circle(120,60)
    t.setheading(r)
    t.end_fill()
    
t.goto(0,0)
t.fillcolor('orange')
t.seth(0)
t.begin_fill()
t.circle(60)
t.end_fill()
t.done()



