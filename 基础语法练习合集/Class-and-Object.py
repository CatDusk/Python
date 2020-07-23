#类与对象练习合集                  2020-7-23


#类的定义与调用                                         2020-7-8
from os.path import join                   #os.path.join()函数：多个路径组合后返回

#自定义类——力
class Force:
    def __init__(self,x,y):                     #构造函数，初始化函数，创建对象
        self.x,self.y=x,y

    def show(self):
        print("Force<%s,%s>"%(self.x,self.y))

    def add(self,force2):
        x=self.x+force2.x
        y=self.y+force2.y
        return Force(x,y)

    __add__=add               #+操作符

    def __mul__(self,n):      #*操作符
        x,y=self.x*n,self.y*n
        return Force(x,y)

    def __eq__(self,force2):
        return (self.x==force2.x)and\
               (self.y==force2.y)
    

f1=Force(1,2)
f1.show()

f2=Force(3,4)
f3=f1.add(f2)
f3.show()

f3.z=9                                            #动态增删属性方法
print(f3.z)
del f3.z

f4=f1+f2
f4.show()

f5=f1*2
f5.show()

print(f3==f4)

#自定义类——文件处理
class Fileobject:
    def __inti__(self,filepath='~',filename='text.txt'):
        self.file=open(join(filepath,filename),'r+')         #读写模式打开文件

    def __del__(self):                          #析构器，销毁对象时调用
        self.file.close()
        del self.file

#自定义类——学生成绩
class Student:
    def __init__(self,name,grade):
        self.name,self.grade=name,grade

    def __lt__(self,other):                   #<操作符
        #return self.grade>other.grade         #成绩高的排序时在前
        return self.name<other.name          #姓名首字母排序

    def __str__(self):                        #易读字符串表示
        return '(%s,%d)'%(self.name,self.grade)

    __repr__=__str__                          #正式字符串表示

s=list()
s.append(Student('Bob',70))    
s.append(Student('Tom',80))
s.append(Student('Jack',90))
s.append(Student('Jane',75))
s.append(Student('Smith',85))
print('Original:',s)
s.sort()
print('Sorted:',s)

#类的继承
#汽车类及其继承
class Car:
    def __init__(self,name):
        self.name=name
        self.remain_mile=0

    def fill_fuel(self,miles):           #加油
        self.remain=miles

    def run(self,miles):                 #行驶
        print(self.name,end=': ')
        if self.remain_mile>=miles:
            self.remain_mile -= miles
            print('run %d miles!'%(miles,))
        else:
            print('fuel out!')

class GasCar(Car):
    def __init__(self,name,capacity):
        super().__init__(name)          #调用父类被覆盖的方法
        self.capacity=capacity
        
    def fill_fuel(self,gas):       #加汽油
        self.remain_mile=gas*6.0

class EleCar(Car):
    def fill_fuel(self,power):     #充电
        self.remain_mile=power*3.0

gcar=GasCar('BMW',3)
gcar.fill_fuel(50.0)
gcar.run(200.0)

ecar=EleCar('Tesla')
ecar.fill_fuel(60.0)
ecar.run(200.0)
#EleCar.run(ecar,200)

#人类，教师子类
class People:
    def __init__(self,name,city):
        self.name,self.city=name,city

    def __str__(self):
        return('<%s:%s>'%(self.name,self.city))

    __repr__=__str__

    def moveto(self,newcity):
        self.city=newcity

    def __lt__(self,other):
        return(self.city<other.city)     #按城市首字母排序

people=list()
people.append(People('Tom','Shanghai'))
people.append(People('Jane','Beijing'))
people.append(People('Bob','Shenzhen'))
people.append(People('Jack','Xian'))
print('Original:',people)

people.sort()
print('Sorted:',people)

class Teacher(People):
    def __init__(self,name,city,school):
        super().__init__(name,city)
        self.school=school

    def moveto(self,newschool):
        self.school=newschool
    
    def __str__(self):
        return('<%s:%s,%s>'%(self.name,self.city,self.school))

    __repr__=__str__

    def __lt__(self,other):
        return(self.school<other.school)     #按学校首字母排序

teacher=list()
teacher.append(Teacher('Tom','Shanghai','HIT'))
teacher.append(Teacher('Bob','Beijing','MIT'))
teacher.append(Teacher('Chen','Beijing','PEK'))
print('Original:',teacher)

teacher.sort()
print('Sorted:',teacher)

#继承内置类——list(列表)
class Mylist(list):
    def product(self):                    #增加新方法——累乘
        sum=1
        for i in self:
            sum=sum*i
        return sum

alist=Mylist()
alist.extend([1,2,3,4])
print(alist.product())


















        
        
        

