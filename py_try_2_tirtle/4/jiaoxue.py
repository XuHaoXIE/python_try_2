import hanshu as xxh
import turtle as t

#快速上手我自己写的函数
'''
t.speed(0)
my_r = 100
my_jiao = 90
xxh.yezihua(num = 6, r = my_r, jiao = my_jiao, fanwei = 360,
            color='red')
xian = xxh.yezixian(my_r, my_jiao)
xxh.yuan(xian,360)
'''

'''
#随便
my_du = 30
my_jiao = 150
my_r = 80
xxh.danyezi(du = my_du, r = my_r, jiao = my_jiao)
'''


# #特例
# #0 < du < 90, 垂直向上的叶子
# #jiao = 180 - 2 * du
# my_du = 30
# my_jiao = 180 - 2 * my_du
# my_r = 80
# xxh.danyezi(du = my_du, r = my_r, jiao = my_jiao)

# #90 < du < 180, 水平向左的叶子
# #jiao = 2 * (180 - du)
# my_du = 150
# my_jiao = 2 * (180 - my_du)
# my_r = 80
# xxh.danyezi(du = my_du, r = my_r, jiao = my_jiao)

# #180 < du < 270, 垂直向下的叶子
# #jiao = 180 - 2 * (du - 180)
# my_du = 210
# my_jiao = 180 - 2 * (my_du - 180)
# my_r = 80
# xxh.danyezi(du = my_du, r = my_r, jiao = my_jiao, color='')

# #270 < du < 360 , 水平向右的叶子
# #jiao = 2 * (360 - du)
# my_du = 300
# my_jiao = 2 * (360 - my_du)
# my_r = 80
# xxh.danyezi(du = my_du, r = my_r, jiao = my_jiao, color='')

'''
my_du = 240
my_jiao = 180 - 2 * (my_du - 180)
my_r = 80
xxh.danyezi(du = my_du, r = my_r, jiao = my_jiao, color='')
xxh.goto_yezi(du = my_du, r = my_r, jiao = my_jiao)
xxh.yuan(20)
'''

#下面的代码是用来测试我的找叶子中心是否在任何角度都生效
'''
num = 5
r = 80
jiao = 80
fanwei = 360
color = ''
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
for i in range(0, fanwei, jiange):
    if color != '':
        xxh.danyezi(i, r, jiao, color = color)
    elif color == '':
        xxh.danyezi(i, r, jiao)
        xxh.goto_yezi(i, r, jiao)
        xxh.yuan(xxh.yezixian(r, jiao)/2)
        t.penup()
        t.goto(0,0)
        t.pendown()
'''



# xxh.yuan(30, yuan_jiao = 360, ret = 1, up = -1)
# xxh.yuan(30, yuan_jiao = 360, ret = 1, up = 1)

'''
my_du = 60
my_r = 300
my_jiao = 90 - my_du
xxh.danyezi(my_du, my_r, my_jiao, ret_2=-1)
xxh.danyezi(360 - my_du, my_r, -my_jiao, ret_2=-1)
'''

xxh.xiangrikui(3, 50, 120, cir_r=100,fanwei = 360, color = '', ret_1=1,ret_2=1, star = 0, cir_color = 'yellow')

#xxh.xiangrikui(3, 50, 120, cir_r=30,fanwei = 360, color = '', ret_1=1,ret_2=1, star = 0)
t.done()




