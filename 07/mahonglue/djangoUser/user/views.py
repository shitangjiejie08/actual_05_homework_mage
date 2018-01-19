from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect
from django.urls import reverse
from .models import User

# Create your views here.

def index(request):
    return render(request,"user/index.html")
def login(request):
    users_name = User.objects.values_list("username", flat=True)#返回所有的username的值即<QuerySet ['mhl', 'jdk']>，但是如果有两个字段即a = User.objects.values_list("username","age")，那么就不能加flat=True，直接返回<QuerySet [('mhl', 23), ('jdk', 26)]>
    print(users_name)
    user = request.POST.get("user","")
    password = request.POST.get("pwd","")
    lgin = request.POST.get("lg","")
    regist = request.POST.get("regist","")
    if lgin:
        if user in users_name:
            u = User.objects.get(username=user)
            p = u.password
            if p == password:
                return render(request,"user/index.html",{"user":user,"password":password})
            else:
                return render(request, "user/login.html", {"user": user, "password": password,"error":"密码不正确"})
        else:
            return render(request, "user/login.html", {"user": user, "password": password, "error": "用户名不正确"})
    elif regist:
        return render(request,"user/register.html")
    else:
        return render(request,"user/login.html")

def regist(request):
    user = request.POST.get("user","")
    password = request.POST.get("pwd","")
    tel = request.POST.get("tel","")
    age = request.POST.get("age","")
    User.objects.create(username=user,password=password,tel=tel,age=age)
    return render(request,"user/login.html")

def list(request):
    users = User.objects.all()
    return render(request,"user/list.html",{"users":users})
def edit_before(request):
    user = request.GET
    print(user["username"])
    return render(request, "user/edit.html",{"user":user})
def edit(request,user):
    print("============")
    print(user)
    tel = request.POST.get("tel","")
    age = request.POST.get("age","")
    users = User.objects.all()
    u = User.objects.get(username=user)
    u.tel = tel
    u.age = int(age)
    u.save()
    print(u)
    return render(request,"user/list.html",{"users":users})
def add(request):
    return render(request,"user/login.html")
def delete(request,user):
    u = User.objects.get(username=user)
    u.delete()
    users = User.objects.all()
    return render(request, "user/list.html", {"users": users})