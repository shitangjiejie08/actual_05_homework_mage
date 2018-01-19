from django.shortcuts import render, get_object_or_404
from .models import get_message, Users
from django.http import HttpResponseRedirect
from django.urls import reverse

# Create your views here.
def login(request):
    username = request.POST.get("username","")
    password = request.POST.get("password","")
    print(username,password)
    a = 0
    for message in get_message():
        print(message)
        if (message["username"] == username) and (message["password"] == password):
            a = 1
            break

    if a:
        print("哈哈")
        return render(request, "user/index.html")

    else:
        print("呜呜")
        return render(request, "user/login.html")

def index(request):
    return render(request,"user/index.html")

def register(request):
    pass

def messages(request):
    return render(request,"user/messages.html")

def control(request):
    return render(request,"user/control.html")

def add(request):
    return render(request,"user/add.html")
def create(request):
    un = request.POST.get("username","")
    te = request.POST.get("tel","")
    pw = request.POST.get("password","")
    print(un,te,pw)
    u = Users(username=un,tel=te,password=pw)
    u.save()
    print(u.username,u.password,u.tel)
    return HttpResponseRedirect(reverse("user:index"))

def deleter(request):
    return render(request, "user/delete.html")

def delete_user(request):
    un = request.POST.get("username","")
    print(un)
    u = Users.objects.get(username=un)
    print(u)
    u.delete()
    return render(request, "user/control.html")
def update(request):
    return render(request,"user/update.html")

def update_user(request):
    un = request.POST.get("username","")
    un_new = request.POST.get("username_new","")
    te = request.POST.get("tel","")
    pd = request.POST.get("password","")
    u = Users.objects.get(username=un)
    print(un,un_new,te,pd)
    u.username = un_new
    u.tel = te
    u.password = pd
    u.save()
    return render(request,"user/control.html")

def find(request):
    return render(request, "user/find.html")
def find_user(request):
    un = request.POST.get("username","")
    u = Users.objects.get(username=un)
    return render(request,"user/detail.html",{"user":u})

