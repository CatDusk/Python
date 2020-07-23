#requests库的基本方法与Response对象的基本属性                2020-7-13
import requests

#-------------------Response对象的属性------------------------
r=requests.get('http://www.baidu.com')
print('状态码：',r.status_code)
print('头信息：',r.headers)
r.encoding=r.apparent_encoding                #头信息推测的编码换成内容推测编码
print('内容：\n',r.text)

#-------------------爬取网页的通用代码框架--------------------
def getHTMLText(url):
    try:
        r=requests.get(url,timeout=30)
        r.raise_for_status()    #状态不是200时，返回一个HTTPError的异常
        r.encoding=r.apparent_encoding
        return r.text
    except:
        return '产生异常'


if __name__=='__main__':
    url='http://www.baidu.com'
    print(getHTMLText(url))

#---------------------requests库的基本方法--------------------
#.head()方法：获得资源的头部信息
r=requests.head('http://www.baidu.com')
print(r.headers)
print(r.text)                 #空

#.post()方法：向资源附加新数据
payload={'key1':'value1','key2':'value2'}
r=requests.post('http://httpbin.org/post',data=payload)  #字典数据附加后编码为form(表单)
print(r.text)

r=requests.post('http://httpbin.org/post',data='ABC')    #字符串数据编码为data
print(r.text)

#.request()方法，有13个可选控制参数，7种请求方式
#params参数：字典或字节序列，增加到url中
kv={'key1':'value1','key2':'value2'}
r=requests.request('GET','http://python123.io/ws',params=kv)
print(r.url)
#Out:https://python123.io/ws?key1=value1&key2=value2

#data参数：字典、字节序列或文件对象，作为Request的内容
kv={'key1':'value1','key2':'value2'}
r=requests.request('POST','http://python123.io/ws',data=kv)
body='主体内容'
r=requests.request('POST','http://python123.io/ws',data=body)

#json参数：JSON格式的数据，作为Request的内容
kv={'key1':'value1'}
r=requests.request('POST','http://python123.io/ws',json=kv)

#headers参数：字典，HTTP定制头
hd={'user-agent':'Chrome/10'}
r=requests.request('POST','http://python123.io/ws',headers=hd)  #模拟浏览器发起访问

#files参数：字典，传输文件
fs={'file':open('text.txt','rb')}
r=requests.request('POST','http://python123.io/ws',files=fs)

#timeout参数：设定超时时间，单位为秒
r=requests.request('GET','http://www.baidu.com',timeout=10)

#proxies：字典，设定访问代理器，可增加登录认证
pxs={'http':'http://user:pass@10.10.10.1:1234'
     'https':'https://10.10.10.1；4321'}
r=requests.request('GET','http://www.baidu.com',proxies=pxs)


#其他：cookies参数、auth参数（HTTP认证）、allow_redirects（重定向开关）、stream（获取内容立即下载开关）、verify（认证SSl证书开关）、cert（本地SSL证书路径）








