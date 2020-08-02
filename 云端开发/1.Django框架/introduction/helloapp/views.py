from django.shortcuts import render
from django.http import HttpResponse
# views.py包含对某个HTTP请求（url）的响应
def hello(request):
    return HttpResponse("Hello World!")
