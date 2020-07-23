#淘宝商品比价定向爬虫               2020-7-17
import requests
import re

def getHTMLText(url):    #爬取页面
    try:
        cookie='cna=bN/MFFou12ACAdvZ9kaBJ2vF; tracknick=sunny%5Cu90ED%5Cu5CF0; tg=0; \
        _cc_=V32FPkk%2Fhw%3D%3D; thw=cn; enc=axiSkb0BSRc%2Bhxf0V0If25kLLL3jilPokLrFH%2F8mspefZUxduoSxpARpgbGbrCM%2FzVXkKXxvR8Tha9FPvYW3ag%3D%3D; \
        hng=CN%7Czh-CN%7CCNY%7C156; miid=476219161994620075; t=60362a2b003cbad7fbf3089b64f34c63; _m_h5_tk=ac246c1b90286747a0d99d3c60adea70_1594982499453;\
        _m_h5_tk_enc=c08635a08167f635457d39cf855dde5c; cookie2=177c6b26a1b81bad98a8ad7d01b1f3f4;v=0; _tb_token_=fe9e3e8e5ee38; alitrackid=www.taobao.com; \
        lastalitrackid=www.taobao.com; JSESSIONID=E4434BD46F8967256B7261B62C7006EA; isg=BGlpRdlrEolanC2MGUEQ6l5leBXDNl1okOaCNAte2tCP0onkU4NgOFvDkHZkyvWg; \
        l=eBI23BPcv2MeDCQKBOfwhurza77OpIRAguPzaNbMiOCP93fp5cZlWZkbJCY9CnGVh6DvR3ow4YKMBeYBq3K-nxv92j-lawMmn'
        header={'user-agent':'Mozilla/5.0','cookie':cookie}
        r=requests.get(url,headers=header)
        r.raise_for_status()
        r.encoding=r.apparent_encoding
        return r.text
    except:
        print('爬取失败')

def parsePage(ilt,html):   #解析页面
    try:
        plt=re.findall(r'\"view_price\"\:\"[\d\.]*\"',html)
        tlt=re.findall(r'\"raw_title\"\:\".*?\"',html)

        for i in range(len(plt)):
            price=eval(plt[i].split(':')[1])
            title=eval(tlt[i].split(':')[1])
            ilt.append([price,title])
    except:
        print('解析失败')

def printGoodsList(ilt):   #打印输出
    tplt='{:4}\t{:8}\t{:16}\n'
    print(tplt.format('序号','价格','商品名称'))
    count=0
    for g in ilt:
        count+=1
        print(tplt.format(count,g[0],g[1]))

def main():
    goods='书包'
    depth=2   #爬取页数
    start_url='https://s.taobao.com/search?q='+goods
    infoList=[]
    for i in range(depth):
        try:
            html=getHTMLText(start_url+'&s='+str(i*44))
            parsePage(infoList,html)
        except:
            continue
    printGoodsList(infoList)
    
main()
    






        
        
