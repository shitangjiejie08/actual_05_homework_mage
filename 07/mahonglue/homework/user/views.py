from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from . import models
from django.urls import reverse

# Create your views here.
def require_login(request):
    return render(request,"user/login.html")

def login(request):
    username = request.POST.get("username","")
    password = request.POST.get("password","")
    print(request.POST)
    rt = models.validate_login(username,password)
    if rt:
        return HttpResponseRedirect(reverse("user:list_user"))
    else:
        content = {"error":"用户名或密码错误","username": username,"password":password}
        return render(request,"user/login.html",content)

def list_user(request):
    user_info = models.list_user()
    content={"user_info":user_info}
    return render(request,'user/list.html',content)

def delete_user(request,name):
    #print(request.GET)
    print("哈哈")
    print(name)
    pass