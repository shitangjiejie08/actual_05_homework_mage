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
    print(cx)
    if cx:
        request.session['user'] = cx
        return HttpResponseRedirect('/user/list/')
    else:
        err_msg = {"error":"用户名或密码错误","username":username,"password":password}
        return render(request,'user/login.html',err_msg)

def user_list(request):
    if request.session.get('user') is None:
        return HttpResponseRedirect('/user/login/')
    users = models.load_users()
    users = {"users":users}
    return render(request,"user/list.html",users)

def add(request):
    return render(request,'user/add.html')

def add_save(request):
    if request.session.get('user') is None:
        return HttpResponseRedirect('/user/login/')
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
    if request.session.get('user') is None:
        return HttpResponseRedirect('/user/login/')
    uid = request.GET.get("uid")
    userinfo = models.get_user_info(uid)[0]
    context = {"users":userinfo}
    return render(request,'user/edit.html',context)

def edit_save(request):
    if request.session.get('user') is None:
        return HttpResponseRedirect('/user/login/')
    uid = request.POST.get("uid")
    age = request.POST.get("edit_age")
    tel = request.POST.get("edit_tel")
    models.modify_user(age,tel,uid)
    return HttpResponseRedirect('/user/list/')

def delete(request):
    if request.session.get('user') is None:
        return HttpResponseRedirect('/user/login/')
    uid = request.GET.get("uid")
    models.delete_user(uid)
    return HttpResponseRedirect('/user/list/')

#  跳转到修改密码页面，并让用户输入旧密码验证
def edit_pass(request):
    if request.session.get('user') is None:
        return HttpResponseRedirect('/user/login/')
    uid = request.GET.get("uid")
    return render(request,'user/edit_pass.html',{"uid":uid})

def edit_pass_save(request):
    uid = request.session.get('user')[0]['id']
    old_pass = request.POST.get("old_pass")
    new_pass = request.POST.get("new_pass")
    confirm_pass = request.POST.get("confirm_pass")
    userinfo = models.get_user_info(uid)
    print(uid,request.session.get('user')[0],'views============')
    status,msg = models.validate_old_pass(old_pass,uid)
    if status:
        status,msg = models.validate_pass(new_pass,confirm_pass)
        if status:
           #两次密码输入不一致
           models.edit_pass(new_pass,uid) 
           #修改密码成功!
           request.session.flush()
           return HttpResponseRedirect("/user/login/") 
        else:
           return render(request,'user/edit_pass.html',{"error":msg})
    else:
        err_msg = {"error":msg}
        return render(request,'user/edit_pass.html',err_msg)

def logout(request):
    request.session.flush()
    return HttpResponseRedirect("/user/login/") 
