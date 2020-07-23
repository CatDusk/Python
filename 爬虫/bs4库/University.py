#中国大学排名定向爬取                   2020-7-16
import bs4
import requests
from bs4 import BeautifulSoup

def getHTMLText(url):                 #爬取链接
    try:
        r=requests.get(url,timeout=10)
        r.raise_for_status()
        r.encoding=r.apparent_encoding
        return r.text
    except:
        print('爬取失败')

def fillUnivList(ulist,html):         #提取数据存储至列表
    soup=BeautifulSoup(html,'html.parser')
    for tr in soup.find('tbody').children:
        if isinstance(tr,bs4.element.Tag):
            tds=tr('td')
            ulist.append([tds[0].string,tds[1].string,tds[4].string])
    return(ulist)
        
def printUnivList(ulist,num):         #输出num所大学排名
    print('{0:^10}\t{1:{3}^30}\t{2:^10}\n'.format('排名','学校名称','总分',chr(12288)))    #中文空格填充学校名称栏
    for i in range(num):
        print('{0:^10}\t{1:{3}^30}\t{2:^10}'.format(ulist[i][0],ulist[i][1],ulist[i][2],chr(12288)))

def main():
    url='http://www.zuihaodaxue.com/zuihaodaxuepaiming-zongbang-2020.html'
    html=getHTMLText(url)
    uinfo=[]
    fillUnivList(uinfo,html)
    num=20
    printUnivList(uinfo,num)

main()
    
