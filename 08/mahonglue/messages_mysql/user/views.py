from django.shortcuts import render

from django.http import HttpResponse, HttpResponseRedirect

from user import models

import hashlib
# Create your views here.

def require_login(request):
    return render(request, 'user/login.html')


def login(request):

    username = request.POST.get('username', '')
    password = request.POST.get('password', '')
    md5 = hashlib.md5()
    md5.update(password.encode("utf8"))
    pwd = md5.hexdigest()
    print(username, password)
    # print(dir(models))
    rt = models.validate_login(username, pwd)
    if rt:
        #return HttpResponse('success')
        request.session["user"] = rt
        return HttpResponseRedirect('/user/list_user/')
    else:
        context = {'error' : '用户名或密码错误', 'username' : username, 'password' : password}
        return render(request, 'user/login.html', context)



def list_user(request):
    if request.session.get("user") is None:
        return HttpResponseRedirect("/user/require_login/")
    users = models.get_users()
    return render(request, 'user/list.html', {'users' : users})


def delete_user(request):
    if request.session.get("user") is None:
        return HttpResponseRedirect("/user/require_login/")
    uid = request.GET.get('id', '')
    print(uid)
    models.delete_user(uid)
    return HttpResponseRedirect('/user/list_user/')


def create_user(request):
    if request.session.get("user") is None:
        return render(request,'user/login.html')
        # return render(request, 'user/create.html')
    # return HttpResponseRedirect("/user/require_login/")
    return render(request,"user/create.html")



def save_user(request):
    if request.session.get("user") is None:
        return HttpResponseRedirect("/user/require_login/")
    username = request.POST.get('username', '')
    password = request.POST.get('password', '')
    print(request.POST.get("password",""))
    md5 = hashlib.md5()
    md5.update(password.encode("utf8"))
    pwd = md5.hexdigest()
    print(pwd)
    age = request.POST.get('age', '')
    tel = request.POST.get('tel', '')

    rt, error = models.validate_add_user(username, age, tel, pwd)
    if rt:
        #验证成功
        models.add_user(username, age, tel, pwd)
        return HttpResponseRedirect('/user/list_user/')
    else:
        context = {}
        context['error'] = error
        context['username'] = username
        context['password'] = password
        context['age'] = age
        context['tel'] = tel

        return render(request, 'user/create.html', context)


def view_user(request):
    if request.session.get("user") is None:
        return HttpResponseRedirect("/user/require_login/")
    username = request.GET.get('name', '')
    # user = models.get_user_by_name(username)
    user = models.get_user(request.GET.get("id"))
    print(user)
    return render(request, 'user/view.html', user)

def modify_user(request):
    if request.session.get("user") is None:
        return HttpResponseRedirect("/user/require_login/")
    username = request.POST.get('username', '')
    # password = request.POST.get('password', '')
    age = request.POST.get('age', '')
    tel = request.POST.get('tel', '')
    id = request.POST.get('id', '')
    rt, error = models.validate_modify_user(age, tel)
    if rt:
        #验证成功
        models.modify_user(id, age, tel)
        return HttpResponseRedirect('/user/list_user/')
    else:
        context = {}
        context['error'] = error
        context['name'] = username
        context['password'] = password
        context['age'] = age
        context['tel'] = tel

        return render(request, 'user/view.html', context)

def password_user(request):
    if request.session.get("user") is None:
        return HttpResponseRedirect("/user/require_login/")
    username = request.GET.get('name', '')
    # user = models.get_user_by_name(username)
    user = models.get_user(request.GET.get("id"))
    print(user)
    return render(request, 'user/modify_password.html', user)

def modify_password(request):
    if request.session.get("user") is None:
        return HttpResponseRedirect("/user/require_login/")
    id = request.POST.get("id","")
    userinfo = models.get_user(id)
    password_old = request.POST.get("password_old")
    password_new = request.POST.get("password_new")
    print(password_old,password_new)
    md5 = hashlib.md5()
    md5.update(password_old.encode("utf8"))
    password = md5.hexdigest()

    md5 = hashlib.md5()
    md5.update(password_new.encode("utf8"))
    passwordNew = md5.hexdigest()
    context_error = {"username":userinfo["username"],"id":userinfo["id"]}
    print("password",password)
    print("id",id)
    print('userinfo',userinfo)
    # print("userinfo",userinfo,userinfo["password"])

    if password == userinfo["password"]:
        rt,error = models.validate_modify_password(password_new)
        if rt:
            models.modify_password(id,passwordNew)
            return HttpResponseRedirect('/user/list_user/')
        else:
            context_error['error'] = error
            return render(request, 'user/modify_password.html', context_error)
    else:
        context_error.update({"error":"旧密码不正确"})
        print(context_error)
        return render(request, 'user/modify_password.html', context_error)

def logout(request):
    request.session.flush()
    return HttpResponseRedirect('/user/require_login/')
