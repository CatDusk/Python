from django.shortcuts import render
from django.http import HttpResponse,JsonResponse,FileResponse 
import time
import os
# Create your views here.
datalist = []
fpath='D:\\desktemp\\python练习\\2.云端开发\\1.Django框架\\Cloudms\\msgapp\\msgdata.txt'
def msgproc(request):
    if request.method == "POST":
        userA = request.POST.get("userA", None)
        userB = request.POST.get("userB", None)
        msg = request.POST.get("msg", None)
        with open(fpath,'a+') as f:
            f.write("{}--{}--{}--{}--\n".format(userB,userA,msg,time.strftime("%Y-%m-%d %H:%M:%S")))
    if request.method == "GET":
        userC = request.GET.get("userC", None)
        if userC != None:
            with open(fpath, "r") as f:
                cnt = 0
                for line in f:
                    linedata = line.split('--')
                    if linedata[0] == userC:
                        cnt = cnt + 1
                        d = {"userA": linedata[1], "msg": linedata[2], "time": linedata[3]}
                        datalist.append(d)
                    if cnt >= 10:
                        break
    return render(request,"MsgSingleWeb.html",{"data":datalist})   
def homeproc(request):
    '''
    return HttpResponse("<h1>这是首页，具体功能请访问<a href='./msggate'>这里</a></h1>")
    '''
    '''
    response = HttpResponse()
    response.write("<h1>这是首页，具体功能请访问<a href='./msggate'>这里</a></h1>")
    return response
    '''
    '''
    response = JsonResponse({'key': 'value1'})
    return response
    '''
    
    cwd=os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    response = FileResponse(open(cwd + "/msgapp/templates/logo.png", "rb"))
    response['Content-Type']='application/octet-stream'
    response['Content-Disposition'] = 'attachment;filename=\'logo.png\''
    return response
    