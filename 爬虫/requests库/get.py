#亚马逊商品页面                                  2020-7-14
import requests
import os
'''
try:
    url="https://www.amazon.cn"
    r=requests.get(url,headers={'User-Agent':'Mozilla/5.0'})
    r.raise_for_status()
    r.encoding=r.apparent_encoding
    #print(r.request.headers)
    print(r.text[:5000])       #前5000个字节
except:
    print('爬取失败')
'''
#网络图片爬取和存储
url='http://pic-bucket.ws.126.net/photo/0001/2020-07-14/FHG2I1MB00AP0001NOS.jpg'
root="C:\\Users\\lenovo\\Desktop\python练习\\1.网络爬虫与信息提取\\1.request库\\"
path=root+url.split('/')[-1]
try:
    if not os.path.exists(root):    #根目录不存在则新建
        os.mkdir(root)
    if not os.path.exists(path):    #文件不存在则存储
        r=requests.get(url)
        with open(path,'wb') as f:
            f.write(r.content)
            f.close
            print('文件保存成功')
    else:
        print('文件已存在')
except:
    print('爬取失败')
