#函数练习合集                   2020-7-23

#===========================字符集合的并集                     2020-7-3=============================
def strunion(str1,str2):
    set1=set(str1)
    set2=set(str2)
    setunion=set1.union(set2)
    return setunion

str1=input('请输入第一个字符串str1：')
str2=input('请输入第二个字符串str2：')
print('str1与str2合并的集合为：',strunion(str1,str2))


#=================================水仙花数               2020-7-3===================================
#水仙花数指m位数每一位的m次幂之和为其本身的数
def isnarnumber(num):
    m=len(str(num))           #位数
    s=0
    for i in range(m):
        s=int(str(num)[i])**m+s
    if s==num:
        judge=True
    else:
        judge=False
    return(judge)
    
n=int(input('请输入要判断的数n(n>=100)：'))
print(isnarnumber(n))

maxnum=int(input('请输入要判断的区间上界max(max>=100)：'))
print('100-%d之间的水仙花数有：'%(maxnum,))
alist=[]
for i in range(100,maxnum+1):
    if isnarnumber(i)==True:
        alist.append(i)
print(alist)
