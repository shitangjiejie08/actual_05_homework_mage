from django.shortcuts import render

from django.http import HttpResponse, HttpResponseRedirect

from . import models
from pymysql.cursors import DictCursor
import  hashlib

def require_login(request):
    return render(request, 'user/login.html')


def login(request):

    username = request.POST.get('username', '')
    password = models.md5(request.POST.get('password', ''))

    rt = models.validate_login(username, password)
    if rt:
        request.session['user'] = rt
        return HttpResponseRedirect('/user/list_user/')
    context = {'error' : '用户名或密码错误', 'username' : username, 'password' : password}
    return render(request, 'user/login.html', context)

def list_user(request):
    if request.session.get('user') is None:
        return HttpResponseRedirect('/user/require_login/')
    rt = models.list_user()
    context={'info':rt, 'user': request.session.get('user').get('username')}


    return  render(request, 'user/list.html', context)


def delete_user(request):
    userid = request.GET.get('userid', '')
    print(userid)
    models.delete_user(userid)
    return  HttpResponseRedirect('/user/list_user/')



def add_user(request):
    if request.session.get('user') is None:
        return HttpResponseRedirect('/user/require_login/')

    if request.method == "GET":
        return render(request, 'user/add.html')

    username = request.POST.get('username', '')
    age = request.POST.get('age', '')
    tel = request.POST.get('tel', '')
    password = models.md(request.POST.get('password', ''))
    print(username, age, tel, password)

    rt_status, error = models.validate_add_user(username, age, tel, password)
    if rt_status:
        models.add_user(username, age, tel, password)
        return HttpResponseRedirect('/user/list_user/')
    else:
        context = {}
        context['error'] = error
        context['username'] = username
        context['password'] = password
        context['age'] = age
        context['tel'] = tel
        return render(request, 'user/create.html', context)


def modify_user(request):
    if request.session.get('user') is None:
        return HttpResponseRedirect('/user/require_login/')

    if request.method == "GET":
        userid= request.GET.get('userid', '')
        return render(request, 'user/modify.html', {'userid':userid})
    userid = request.POST.get('userid', '')
    age = request.POST.get('age', '')
    tel = request.POST.get('tel', '')


    rt_status, error =models.validate_modify_user(userid, age)
    if rt_status:
        models.modify_user(userid, age, tel)
        return HttpResponseRedirect('/user/list_user/')
    else:
        context = {}
        context['error'] = error

        context['age'] = age
        context['tel'] = tel
        return render(request, 'user/modify.html', context)

def modify_user_password(request):
    if request.session.get('user') is None:
        return HttpResponseRedirect('/user/require_login/')

    if request.method == "GET":
        userid= request.GET.get('userid', '')
        return render(request, 'user/modify_password.html', {'userid':userid})
    userid = request.POST.get('userid', '')

    password = models.md5(request.POST.get('password', ''))
    old_password = models.md5(request.POST.get('old_password', ''))
    print(userid, password, old_password)

    rt_status, error =models.validate_modify_user_password(userid, password, old_password)
    if rt_status:
        models.modify_user_password(userid,password)
        return HttpResponseRedirect('/user/list_user/')
    else:
        context = {}
        context['error'] = error
        context['userid'] = userid
        return render(request, 'user/modify_password.html', context)


def logout(request):
    request.session.flush()
    return HttpResponseRedirect('/user/require_login/')


