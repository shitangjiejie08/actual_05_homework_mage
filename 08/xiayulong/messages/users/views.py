from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect
from .models import *
# Create your views here.


def require_login(request):
    return render(request,"users/require_login.html")

def login(request):
    username = request.POST.get("username")
    password = request.POST.get("password")
    if auth_user_v2(username,password):
        request.session['user'] = username
        return HttpResponseRedirect("/users/list_users/")
    else:
        context = { "error": "用户名或密码错误", "username":username, "password":password}
        return render(request,"users/require_login.html",context)

def list_users(request):
    if request.session.get("user") is None:
        return HttpResponseRedirect("/users/require_login/")
    users = show_users()
    context = {"users":users}
    return render(request,"users/list_users.html",context)

def delete_users(request):
    if request.session.get("user") is None:
        return HttpResponseRedirect("/users/require_login/")
    name = request.GET.get("name")
    print(request.session.get("user") != name)
    if request.session.get("user") == name:
        info = 'Suiciding is not allowed!'
    else:
        del_user(name)
    return HttpResponseRedirect("/users/list_users/")

def view_users(request):
    name = request.GET.get("name")
    context = find_user_v2(name)
    print("xxxxxx")
    return render(request,"users/view_user.html",context)

def view_users_passwd(request):
    name = request.GET.get("name")
    context = find_user_v2(name)
    return render(request,"users/view_user_passwd.html",context)

def modify(request):
    name = request.POST.get("name")
    tel = request.POST.get("tel")
    age = request.POST.get("age")
    if tel == '' and age == '':
        return HttpResponseRedirect("/users/list_users/")
    #if password != '' and len(password) < 8:
    #    return render(request, "users/view_user.html",{"name":name,"info":"密码少于8位"})
    user_info = {}
    user_info["name"] = name
    #if password != '':
    #    user["passwd"] = password
    if tel != '':
        user_info["tel"] = tel
    if age != '':
        user_info["age"] = age
    update_user_v2(user_info)
    return HttpResponseRedirect("/users/list_users/")

def modify_passwd(request):
    name = request.POST.get("name")
    old_passwd = request.POST.get("old_password")
    new_passwd = request.POST.get("new_password")
    confirm_new_passwd = request.POST.get("confirm_new_password")
    if new_passwd != confirm_new_passwd :
        # return render(request,"users/view_user_passwd",{ "name": name, "info": "新密码两次输入不一致！"})
        info = "新密码两次输入不一致！"
        print(info)
        #return HttpResponseRedirect("/users/modify_passwd/?name="+name)
        return HttpResponseRedirect("/users/view_users_passwd/?name="+name)
    if auth_user_v2(name,old_passwd) == False:
        info = "旧密码不正确"
        print(info)
        return HttpResponseRedirect("/users/view_users_passwd/?name="+name)
    else:
        user_info = dict(zip(("name","old_passwd","new_passwd"),(name,old_passwd,new_passwd)))
        update_user_passwd(user_info)
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
    if name in users:
        return render(request,"users/edit_user_info.html",{"info":"用户已存在"})
    user_info = {"name":name,"tel":tel,"age":age,"passwd":password}
    add_user_v2(user_info)
    return HttpResponseRedirect("/users/list_users/")

def logout(request):
    request.session.flush()
    return HttpResponseRedirect("/users/require_login/") 