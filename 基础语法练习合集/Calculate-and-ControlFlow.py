#计算与控制流练习合集                2020-7-23

#=========================计算1+2！+3！+.....+n！                      2020-6-30===================================
import math
n=int(input('请输入n：'))
sum=0
for i in range(1,n+1):
    j=i
    fact=1
    for j in range(1,j+1):         #阶乘计算
        fact=fact*j
    sum=sum+fact
print("计算结果为：",sum)
'''
#调用阶乘函数
sum=0
for i in range(1,n+1):
    sum=sum+math.factorial(i)
print("计算结果为：",sum)
'''
#==========================================3x+1验证               2020-6-30========================================
#任意整数，奇数*3+1，偶数/2，在这两个操作下最终结果都会掉到4 2 1循环之中
for i in range(1,10000):                #验证从1到9999的整数
    n=i
    step=0                              #调到4 2 1循环中的步数
    while n!=1:
        if n%2==0:                      #偶数/2，%为取余，//为取整，/为真除
            n=n/2
        else:
            n=n*3+1                     #奇数*3+1
        step+=1
    else:
        print(i,"Traped!",step,"steps")
#强制中断程序：CTRL+C

#===========================================计算y年m月有几天                  #2020-6-30=============================
year=input('请输入年份：')
month=int(input('请输入月份：'))
adict={1:31,3:31,4:30,5:31,6:30,7:31,8:31,9:30,10:31,11:30,12:31}

if year[-2:]=='00':            #闰年判定
    if int(year)%400==0:
        adict[2]=29
    else:
        adict[2]=28
        
else:
    if int(year)%4==0:
        adict[2]=29
    else:
        adict[2]=28

days=adict[month]
print('%d年%d月有%d天'%(int(year),month,days))


#==========================================字符串循环移位    2020-6-30================================================
astr=input('请输入一个字符串s：')
n=int(input('请输入移动的位数n:'))
rstr=astr[:len(astr)-n]
lstr=astr[len(astr)-n:]
bstr=lstr+rstr
print('s向右移动n位结果为：',bstr)

#==============================英文数字字符串转阿拉伯数字字符串                    2020-6-30==========================
str_En=input("请输入英文数字字符串(如one-four-five)：")
adict={'zero':'0','one':'1','two':'2','three':'3',
       'four':'4','five':'5','six':'6','seven':'7',
       'eight':'8','nine':'9'}
Enlist=str_En.split('-')

for i in range(len(Enlist)):
    Enlist[i]=adict[Enlist[i]]

str_Ar=''.join(Enlist)
print("转换为阿拉伯数字字符串为：",str_Ar)



