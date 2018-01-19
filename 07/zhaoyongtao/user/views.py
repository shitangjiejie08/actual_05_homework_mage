from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect
from . import models
# Create your views here.

def login(request):
    return render(request,'user/login.html')

def auth_login(request):
    username = request.POST.get("login_name")
    password = request.POST.get("login_pass")
    cx = models.validate_login(username,password)
    if cx:
        return HttpResponseRedirect('/user/list/')
    else:
        err_msg = {"error":"用户名或密码错误","username":username,"password":password}
        return render(request,'user/login.html',err_msg)

def user_list(request):
    users = models.load_users()
    users = {"users":users.values()}
    return render(request,"user/list.html",users)


def add(request):
    return render(request,'user/add.html')

def add_save(request):
    username = request.POST.get("add_name")
    age = request.POST.get("add_age")
    tel = request.POST.get("add_tel")
    password = request.POST.get("add_pass")
    status,rt_reason = models.validate_add_user(username,age,tel,password)
    if status:
        models.add_user(username,age,tel,password)
        return HttpResponseRedirect('/user/list/')
    else:
        err_msg = {"error":rt_reason,'username': username, 'password': password, 'tel': tel, 'age': age}
        return render(request,'user/add.html',err_msg)

def edit(request):
    username = request.GET.get("name")
    context = {"username":username}
    return render(request,'user/edit.html',context)
def edit_save(request):
    username = request.POST.get("edit_name")
    age = request.POST.get("edit_age")
    tel = request.POST.get("edit_tel")
    password = request.POST.get("edit_pass")
    status,rt_reason = models.validate_modify_user(username,age,tel,password)
    if status:
        models.modify_user(username,age,tel,password)
        return HttpResponseRedirect('/user/list/')
    else:
        err_msg = {"error":rt_reason,'username': username, 'password': password, 'tel': tel, 'age': age}
        return render(request,'user/edit.html',err_msg)

def delete(request):
    username = request.GET.get("name")
    status,rt_reason = models.validate_delete_user(username)
    if status:
        models.delete_user(username)
        return HttpResponseRedirect('/user/list/')
    else:
        err_msg = {"error":rt_reason,'username': username}
        return render(request,'user/list.html',err_msg)

