#百度搜索关键词提交                                2020-7-14
import requests
'''
url='http://www.baidu.com/s'
kv={'wd':'Python'}
try:
    r=requests.get(url,params=kv)
    r.raise_for_status()
    r.encoding=r.apparent_encoding
    print(r.text[:2000])
except:
    print('爬取失败')
'''
#IP地址归属地查询
url='https://www.ip138.com/iplookup.asp?ip='
ip="223.104.15.43&action=2"
try:
    r=requests.get(url+ip,headers={'User-Agent':'Mozilla/5.0'})
    r.raise_for_status()
    r.encoding=r.apparent_encoding
    print(r.text[1000:3000])
except:
    print('爬取失败')
