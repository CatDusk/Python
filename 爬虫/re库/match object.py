#match对象                         2020-7-17
import re

#属性
m=re.search(r'[1-9]\d{5}','BIT100081 TSU100084')

print('m.re:',m.re)
print('m.string:',m.string)
print('m.pos:',m.pos)  #搜索文本的开始位置
print('m.endpos:',m.endpos) #搜索文本的结束位置

#方法
print('.group(0):',m.group(0))
print('.start():',m.start()) #匹配字符串在原始字符串的开始位置
print('.end():',m.end())
print('.span():',m.span())
