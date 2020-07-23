#股票收益预测数据爬取                                     2020-7-18

import requests
import re
from bs4 import BeautifulSoup

def getHTMLText(url,code='utf-8'):
    r=requests.get(url,headers={'User-Agent':'Mozilla/5.0'})
    r.raise_for_status()
    r.encoding=code
    return r.text
   
stock_list_url='http://data.eastmoney.com/report/stock.jshtml'    #东方财富网
html=getHTMLText(stock_list_url)
code=re.findall(r'\"stockCode\"\:\"\d{6}\"',html) #代码
name=re.findall(r'\"stockName\"\:\".*?\"',html)   #名称
predict=re.findall(r'\"predictThisYearEps\"\:\".*?\"',html)#收益预测

codelist=[]
namelist=[]
predictlist=[]

fpath='C:\\Users\\lenovo\\Desktop\\python练习\\1.网络爬虫与信息提取\\3.re库\\stock.txt'
count=0
for i in range(len(code)):
    
    count+=1
    print('\r当前进度：{:.2f}%'.format(count*100/len(code)),end='')
    
    codelist.append(eval(code[i].split(':')[1]))
    namelist.append(eval(name[i].split(':')[1]))
    predictlist.append(eval(predict[i].split(':')[1]))
    infoDict={}
    infoDict['股票代码']=codelist[i]
    infoDict['股票名称']=namelist[i]
    infoDict['预取收益']=predictlist[i]
    with open(fpath,'a',encoding='utf-8') as f:
        f.write(str(infoDict)+'\n')
    

