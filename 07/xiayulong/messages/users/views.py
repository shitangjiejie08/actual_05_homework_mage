from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect
from .models import *
# Create your views here.


def require_login(request):
    return render(request,"users/require_login.html")

def login(request):
    username = request.POST.get("username")
    password = request.POST.get("password")
    users = {}
    users = init_users("/data/code/users.txt")
    if auth_user_v2(username,password,users):
        return HttpResponseRedirect("/users/list_users/")
    else:
        context = { "error": "用户名或密码错误", "username":username, "password":password}
        return render(request,"users/require_login.html",context)

def list_users(request):
    users = {}
    users = init_users("/data/code/users.txt")
    context = {"users":users}
    return render(request,"users/list_users.html",context)

def delete_users(request):
    users = {}
    users = init_users("/data/code/users.txt")
    name = request.GET.get("name")
    del_user(name,users)
    save_json("/data/code/users.txt",users)
    return HttpResponseRedirect("/users/list_users/")

def view_users(request):
    users = {}
    users = init_users("/data/code/users.txt")
    name = request.GET.get("name")
    context = users[name]
    print("xxxxxx")
    return render(request,"users/view_user.html",context)

def modify(request):
    name = request.POST.get("name")
    password = request.POST.get("passwd")
    tel = request.POST.get("tel")
    age = request.POST.get("age")
    print(name,password,tel,age)
    if password == '' and tel == '' and age == '':
        return HttpResponseRedirect("/users/list_users/")
    if password != '' and len(password) < 8:
        return render(request, "users/view_user.html",{"name":name,"info":"密码少于8位"})
    users = {}
    users = init_users("/data/code/users.txt")
    if password != '':
        users[name]["passwd"] = password
    if tel != '':
        users[name]["tel"] = tel
    if age != '':
        users[name]["age"] = age
    save_json("/data/code/users.txt",users)
    return HttpResponseRedirect("/users/list_users/")

def edit_user_info(request):
    return render(request,"users/edit_user_info.html")

def create_users(request):
    name = request.POST.get("username")
    password = request.POST.get("passwd")
    tel = request.POST.get("tel")
    age = request.POST.get("age")
    if password == '' and tel == '' and age == '':
        return render(request,"users/edit_user_info.html",{"info":"信息不能为空"})
    users = {}
    users = init_users("/data/code/users.txt")
    if name in users:
        return render(request,"users/edit_user_info.html",{"info":"用户已存在"})
    users[name] = {"name":name,"tel":tel,"age":age,"passwd":password}
    save_json("/data/code/users.txt",users)
    return HttpResponseRedirect("/users/list_users/")