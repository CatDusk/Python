#高级特性与模块应用练习合集                          2020-7-23

#======================================例外处理                             2020-7-12======================

try:
    print('try...')
    #r=10/'xyz'
    #r=10/0
    r=10/2
    print('result:',r)
except TypeError as e:
    print('TypeError:',e)
except ZeroDivisionError as e:
    print('ZeroDivisionError:',e)
else:
    print('no error!')
finally:
    print('finally...')
print('END')

#输入两个数作商
try:
    a=int(input('请输入被除数a：'))
    b=int(input('请输入除数b：'))
    result=a/b
    print('a/b=',result)
except ZeroDivisionError as e:
    print('Error:除数不可以为0！')
except ValueError as e:
    print('Error:只能输入数值！')
else:
    print('No error!')
finally:
    print('END')

#==========================================生成器                              2020-7-12===========================
import math

#生成器推导式
agen=(x*x for x in range(10))
for n in agen:
    print(n)


#生成器函数
print('偶数')
def even_number(max):                    #产生偶数
    n=0
    while n<max:
        yield n                          #协同程序
        n+=2

for i in even_number(10):
    print(i)
  
#勾股数
num=((i,j,k) for i in range(1,100) for j in range(i,100) for k in range(1,100) if i*i+j*j==k*k)
for i in num:
    print(i)

#斐波那契数列
def fib(max):
    alist=[1,1]
    for i in range(2,max):
        alist.append(alist[i-1]+alist[i-2])
        yield alist[i]
print('1\n1\n')
for i in fib(80):
    print(i)

#=============================图形用户界面（GUI）                    2020-7-6===============================
import easygui as g
import sys
while 1:
    g.msgbox('嗨，欢迎进入GUI的小游戏！','互动小游戏')
    msg='你希望学习到什么知识呢？'
    title='互动小游戏'
    choices=['琴棋书画','四书五经','层序编写','逆向分析']
    choice=g.choicebox(msg,title,choices)
    g.msgbox('你的选择是：'+str(choice),'结果')
    
    msg='你希望重新开始小游戏吗？'
    title='请选择'
    if g.ccbox(msg,title):              #ccbox根据选择continue或cancel返回整型1或0
        pass
    else:
        sys.exit(0)

#====================================计时与文件处理                2020-7-7==================================
import time
import random
import math
#程序计时
'''
for n in range(700,1001):
    s=0
    time.sleep(0.1)
    t1=time.time()
    for i in range(n):
        s=s+math.factorial(i+1)
    t2=time.time()
    print('n=%d时程序执行时间为'%(n,),t2-t1)
'''

#文件处理
f=open('text.txt','wt')                 #写
f.writelines(['hello!\n','how are you?\n','I\'m fine,thank you.And you?\n','Fine,too.\n'])
f.close()

with open('text.txt','rt')as myfile:    #读,上下文管理器
    re=myfile.readlines()
    print(re)
    print('随机挑选一行输出：',random.choice(re))

#=========================================海龟作图                     2020-7-6===============================
import turtle

#多边形
p=turtle.Pen()
p.pencolor('blue')
p.pensize(5)

p.left(90)
p.up()
p.backward(100)
p.down()
p.right(90)

for i in range(6):          #边数与转角乘积为360
    p.forward(100)
    p.right(60)

#五角星
p.left(90)
p.up()
p.forward(100)
p.down()
p.right(90)

for i in range(5):
    p.forward(100)
    p.right(144)

#二叉树
p.left(90)
p.up()
p.forward(50)
p.down()
p.color('green')

def tree(branchLen,t):
    if branchLen>5:
        t.forward(branchLen)
        t.right(20)
        tree(branchLen-15,t)
        t.left(40)
        tree(branchLen-15,t)
        t.right(20)
        t.backward(branchLen)

tree(75,p)

#分形树练习
import turtle

p=turtle.Pen()
turtle.bgcolor('orange')
p.pencolor('brown')
p.pensize(5)
p.speed(0)
p.left(90)
p.up()
p.backward(300)
p.down()                   #上

#土
p.right(90)                #右
p.begin_fill()
p.color('brown')
for i in range(2):
    p.forward(1000)
    p.right(90)
    p.forward(10)
    p.right(90)
    p.forward(1000)
p.end_fill()
p.left(90)

#树
def tree(branchLen,t):
    if branchLen>5:
        t.pencolor('brown')
        t.pensize(branchLen/10)
        t.forward(branchLen)
        t.right(25)
        tree(branchLen-15,t)
        t.left(50)
        tree(branchLen-15,t)
        t.right(25)
        t.backward(branchLen)
    else:
        
        t.pensize(1)
        t.right(90)
        t.begin_fill()
        t.color('green')
        t.circle(5)
        t.end_fill()
        t.left(90)
        t.color('brown')

tree(125,p)

p.up()
p.forward(50)
p.left(90)
p.forward(600)
p.down()
p.color('black')
p.write('分形树,Python 3.8.2',font=('Arail',20,'bold'))
p.hideturtle()

#=================================图像处理                                               2020-7-12===========================

from PIL import Image,ImageFilter,ImageFont,ImageDraw

im=Image.open('im.jpeg')

im.thumbnail((200,200),Image.ANTIALIAS)   #缩略图
im.save('im_thumb','jpeg')
im.show()

im3=im.filter(ImageFilter.BLUR)           #模糊
im3.save('im_blur','jpeg')
im3.show()

font=ImageFont.truetype('simsun.ttc',100)  #宋体
draw=ImageDraw.Draw(im)      #创建可绘图对象
draw.text((100,10),'Hello World',(255,0,0),font=font)  #添加文字
im.save('im_text','jpeg')
im.show()


#=====================================验证码                              2020-7-12==========================
from PIL import Image,ImageDraw,ImageFont,ImageFilter
import random

def rndChar():
    return chr(random.randint(65,90))    #随机字母
    #return str(random.randint(0,9))

def rndColor():                          #背景随机颜色
    return (random.randint(100,255),\
            random.randint(100,255),\
            random.randint(100,255))

def rndColor2():                         #文字随机颜色
    return (random.randint(0,64),\
            random.randint(0,64),\
            random.randint(0,64))

width=60*4                               #每个字母60*60的空间
height=60
image=Image.new('RGB',(width,height),(255,255,255))#创建背景
#font=ImageFont.truetype('Arial.ttf',36)  #字体对象
font=ImageFont.truetype('simsun.ttc',36)
draw=ImageDraw.Draw(image)               #Draw对象

for x in range(width):
    for y in range(height):
        draw.point((x,y),fill=rndColor())  #填充像素

for t in range(4):                       #文字输出
    draw.text((60*t+10,10),rndChar(),font=font,fill=rndColor2())

image=image.filter(ImageFilter.BLUR)
image.show()
image.save('code','jpeg')


