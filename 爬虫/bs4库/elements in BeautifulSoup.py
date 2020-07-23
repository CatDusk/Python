#BeautifulSoup类的基本元素                        2020-7-15

from bs4 import BeautifulSoup
import requests

r=requests.get('http://python123.io/ws/demo.html')
demo=r.text

soup=BeautifulSoup(demo,'html.parser')
#print(soup.prettify())                              #HTML格式化

print(soup.title)                                    #soup.tag查看标签
print(soup.a.name)         #查看标签名字
print(soup.a.attrs)        #查看标签属性，字典
print(soup.a.string)       #查看标签字符串和注释，根据类型判断
print(type(soup.a.string))

print(soup.body.contents)  #子节点列表
for child in soup.body.children:    #子节点迭代器
    print(child)

for child in soup.body.descendants: #子孙节点迭代器
    print(child)

print(soup.html.parent)     #父节点，最高层为其本身，soup为空
for parent in soup.a.parents: #先辈节点迭代器
    #print(parent.name)
    
    if parent is None:
        print(parent)
    else:
        print(parent.name)
    

print(soup.a.next_sibling)   #下一个节点
print(soup.a.previous_sibling)#上一个节点

for sibling in soup.a.next_siblings:#所有后续节点
    print(sibling)

for sibling in soup.a.previous_siblings:#所有前续节点
    print(sibling)
