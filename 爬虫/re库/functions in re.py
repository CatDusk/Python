#Re库主要功能函数                         2020-7-17
import re

match=re.search(r'[1-9]\d{5}','BIT 100081')     #匹配第一个结果
if match:
    print(match.group(0))

match=re.match(r'[1-9]\d{5}','100081BIT')       #从开始位置匹配
if match:
    print(match.group(0))

ls=re.findall(r'[1-9]\d{5}','100081BIT 100084TSU')#列表形式的全部匹配结果
print(ls)

for m in re.finditer(r'[1-9]\d{5}','100081BIT 100084TSU'): #全部匹配结果的迭代体
    if m:
        print(m.group(0))

print(re.split(r'[1-9]\d{5}','100081BIT 100084TSU')) #分割
print(re.split(r'[1-9]\d{5}','100081BIT 100084TSU',maxsplit=1))

print(re.sub(r'[1-9]\d{5}',':zipcode','100081BIT 100084TSU')) #替换

pat=re.compile(r'[1-9]\d{5}')    #正则表达式的编译
rst=pat.search('BIT 100081')
print(rst.group(0))

match=re.search(r'PY.*N','PYANBNCNDN')   #默认贪婪匹配
print(match.group(0))

match=re.search(r'PY.*?N','PYANBNCNDN')   #最小匹配
print(match.group(0))
