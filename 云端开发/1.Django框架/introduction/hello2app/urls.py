#本地路由
from django.urls import path
from . import views
urlpatterns = [
    path('',views.hello)
]