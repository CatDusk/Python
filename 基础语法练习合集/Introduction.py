#Python入门练习合集                  2020-7-23

#==========================================hello world              2020-6-19=====================================================
print("Hello world!")

#======================================================随机菜单    2020-6-19======================================================
import random               #导入随机数模块
menu=["coffee","tea","cola"]
print("Menu:",menu)
name=input("Your name please:")
drink=random.choice(menu)   #返回列表的一个随机项
print("Hello",name,"! Enjoy your ",drink)

#========================================输入年月日，判断该天为该年的第几天            2020-6-19==================================
import datetime           #导入模块
'''
datetime模块定义了5个类，分别是
1.datetime.date：表示日期的类
2.datetime.datetime：表示日期时间的类
3.datetime.time：表示时间的类
4.datetime.timedelta：表示时间间隔，即两个时间点的间隔
5.datetime.tzinfo：时区的相关信息

from datetime import date
from datetime import datetime
from datetime import time
from datetime import timedelta
from datetime import tzinfo
from datetime import * #不知道用啥 全部导入就可以
'''
dtstr=input("Enter the datatime:(20170228):")   #input输入字符串类型 
dt=datetime.datetime.strptime(dtstr,"%Y%m%d")   #字符串转换为日期格式
#print(dt)
'''
datetime.datetime.now()：返回当前系统时间
datetime.datetime.strftime()：由日期格式转化为字符串格式
datetime.datetime.strptime():由字符串格式转化为日期格式

time.strptime(string[, format])
string -- 时间字符串
format -- 格式化字符串

python中时间日期格式化符号：
%y 两位数的年份表示（00-99）
%Y 四位数的年份表示（000-9999）
%m 月份（01-12）
%d 月内中的一天（0-31）
%H 24小时制小时数（0-23）
%I 12小时制小时数（01-12）
%M 分钟数（00-59）
%S 秒（00-59）
%a 本地简化星期名称
%A 本地完整星期名称
%b 本地简化的月份名称
%B 本地完整的月份名称
%c 本地相应的日期表示和时间表示
%j 年内的一天（001-366）
%p 本地A.M.或P.M.的等价符
%U 一年中的星期数（00-53）星期天为星期的开始
%w 星期（0-6），星期天为 0，星期一为 1，以此类推。
%W 一年中的星期数（00-53）星期一为星期的开始
%x 本地相应的日期表示
%X 本地相应的时间表示
%Z 当前时区的名称
%% %号本身

'''
another_dtstr=dtstr[:4]+'0101'  #该年第一天
'''
计数从0开始,（matlab是1）最后一个是-1
s[i:j] 表示获取a[i]到a[j-1]
s[:-1]去掉最后一个字符
s[:-n]去掉最后n个字符
s[-2:]取最后两个字符
s[i:j:k]这种格式呢，i,j与上面的一样，但k表示步长，默认为1
s[::-1]是从最后一个元素到第一个元素复制一遍（反向）
'''
another_dt=datetime.datetime.strptime(another_dtstr,"%Y%m%d")
print(int((dt - another_dt).days)+1)      #.days为其属性


#======================================================猜数游戏        2020-6-19====================================
import random

secret=random.randint(1,100)
print('''猜数游戏!我想了一个1—100的整数，你最多可以猜6次，看看能猜出来吗？''')
tries=1
while tries<=6:
    guess=int(input("1-100的整数，第%d次猜，请输入："%(tries)))
    if guess == secret:
        print("恭喜答对了！你只猜了%d次！\n就是这个：%d！"%(tries,secret))
        break
    elif guess>secret:
        print("不好意思，你的数大了一点儿！")
    else:
        print("不好意思，你的数小了一点儿！")
    tries+=1
else:
    print("哎呀！怎么也没猜中！再见！")

#=========================================================归并排序                2020-6-19==========================
'''
归并排序（MERGE-SORT）是建立在归并操作上的一种有效的排序算法,将已有序的子序列合并，得到完全有序的序列；
即先使每个子序列有序，再使子序列段间有序。若将两个有序表合并成一个有序表，称为二路归并。

归并操作(merge)，也叫归并算法，指的是将两个顺序序列合并成一个顺序序列的方法。
如　设有数列{6，202，100，301，38，8，1}
初始状态：6,202,100,301,38,8,1
第一次归并后：{6,202},{100,301},{8,38},{1}，比较次数：3；
第二次归并后：{6,100,202,301}，{1,8,38}，比较次数：4；
第三次归并后：{1,6,8,38,100,202,301},比较次数：4；
总的比较次数为：3+4+4=11；
逆序数为14；

归并操作的工作原理如下：
第一步：申请空间，使其大小为两个已经排序序列之和，该空间用来存放合并后的序列
第二步：设定两个指针，最初位置分别为两个已经排序序列的起始位置
第三步：比较两个指针所指向的元素，选择相对小的元素放入到合并空间，并移动指针到下一位置
重复步骤3直到某一指针超出序列尾
将另一序列剩下的所有元素直接复制到合并序列尾
'''
import random

def merge_sort(data_list):
    '''
    def functionname( parameters ):
       function_suite
       return [expression]
    '''
    if len(data_list) <= 1:               #列表只有一个数时，直接返回这个数，<=小于等于 - 返回x是否小于等于y
        return data_list
    middle =int(len(data_list)/2)         #计算序列中间的索引，int向下取整
    left=merge_sort(data_list[:middle])   #左右两个序列分别排序
    right=merge_sort(data_list[middle:])
    merged=[]
    while left and right:                 #左右两个序列都有值时
        merged.append(left.pop(0) if left[0]<=right[0] else right.pop(0))#添加左右两个序列中的较小者，并在左右序列中相应移除
        #list.append(obj),在列表末尾添加新的对象。list.pop() 函数用于移除列表中的一个元素（默认最后一个元素），并且返回该元素的值。
    merged.extend(right if right else left)  #比较结束后将多出来的序列整体补充到排序结果中
    #list.extend(seq)在列表末尾一次性追加另一个序列中的多个值（用新列表扩展原来的列表）
    return merged
'''
while 判断条件(condition)：
    执行语句(statements)……
continue 用于跳过该次循环，break 则是用于退出循环
'''
'''
在程序设计中，and称为逻辑与运算，也称布尔运算；
1.and是在布尔上下文中从左到右计算表达式的值；
2.0、''、[]、()、{}、None、False在布尔上下文中为假；其它任何东西都为真；
3.如果布尔上下文中的某个值为假，则返回第一个假值；
4.所有值都为真，则返回最后一个真值。
'''
data_list=[random.randint(1,100) for _ in range(50)]#ranint() 方法返回指定范围的整数
print(merge_sort(data_list))

#============================================输入一行字符，统计字符中的字母、空格、数字、其他字符的数目 2020-6-19=================================
import string

s=input('input a string:')
letter=0
space=0
digit=0
other=0

for c in s:
    if c.isalpha():
        letter+=1    #+=1是对原本的实例做加1运算
    elif c.isspace():
        space+=1
    elif c.isdigit():#S.isdigit()返回的是布尔值：True False,S中至少有一个字符且如果S中的所有字符都是数字，那么返回结果就是True；否则，就返回False
        digit+=1
    else:
        other+=1
'''
Python for循环可以遍历任何序列的项目，如一个列表或者一个字符串。

for iterating_var in sequence:
   statements(s)

也可以通过序列索引迭代
for i in range(start, stop，step)：#起始、终止和步长
range（3）即：从0到3，不包含3，即0,1,2
for i in range () 就是给i依次赋值

在 python 中，for … else 表示这样的意思，for 中的语句和普通的没有区别，
else 中的语句会在循环正常执行完（即 for 不是通过 break 跳出而中断的）的情况下执行
   
'''
print('There are %d letters,%d spaces,%d digits \
and %d other characters in your string.'\
      %(letter,space,digit,other))
        






