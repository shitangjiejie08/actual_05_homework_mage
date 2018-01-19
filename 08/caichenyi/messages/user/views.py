from django.shortcuts import render

from django.http import HttpResponse, HttpResponseRedirect

from . import models

# Create your views here.

def require_login(request):
    return render(request, 'user/login.html')


def login(request):
    username = request.POST.get('username', '')
    password = request.POST.get('password', '')
    rt = models.validate_login(username, password)
    if rt:
        request.session['user'] = rt
        #return HttpResponse('success')
        return HttpResponseRedirect('/user/list_user/')
    else:
        context = {'error': '用户名或密码错误', 'username': username, 'password': password}
        return render(request, 'user/login.html', context)


def list_user(request):
    if request.session.get('user') is None:
        return HttpResponseRedirect('/user/require_login/')
    users = models.get_users()
    return render(request, 'user/list.html', {'users': users})


def delete_user(request):
    if request.session.get('user') is None:
        return HttpResponseRedirect('/user/require_login/')
    _id = request.GET.get('id', '')
    models.delete_user(_id)
    return HttpResponseRedirect('/user/list_user/')


def create_user(request):
    if request.session.get('user') is None:
        return HttpResponseRedirect('/user/require_login/')
    return render(request, 'user/create.html')


def save_user(request):
    if request.session.get('user') is None:
        return HttpResponseRedirect('/user/require_login/')
    username = request.POST.get('username', '')
    password = request.POST.get('password', '')
    age = request.POST.get('age', '')
    tel = request.POST.get('tel', '')

    rt, error = models.validate_add_user(username, age, tel, password)
    if rt:
        #验证成功
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


def view_user(request):
    if request.session.get('user') is None:
        return HttpResponseRedirect('/user/require_login/')
    # username = request.GET.get('name', '')
    # user = models.get_user_by_name(username)
    # return render(request, 'user/view.html', user)
    _id = request.GET.get('id', '')
    return render(request, 'user/view.html', {'id': _id})

def modify_user(request):
    if request.session.get('user') is None:
        return HttpResponseRedirect('/user/require_login/')
    _id = request.POST.get('id', '')
    password = request.POST.get('password', '')
    age = request.POST.get('age', '')
    tel = request.POST.get('tel', '')
    rt, error = models.validate_modify_user(_id, age, tel, password)
    if rt:
        #验证成功
        models.modify_user(_id, age, tel, password)
        return HttpResponseRedirect('/user/list_user/')
    else:
        context = {}
        context['error'] = error
        context['id'] = _id
        context['password'] = password
        context['age'] = age
        context['tel'] = tel
        return render(request, 'user/view.html', context)


def logout(request):
    request.session.flush()
    return HttpResponseRedirect('/user/require_login/')

def view_modify_passwd(request):
    if request.session.get('user') is None:
        return HttpResponseRedirect('/user/require_login/')
    _id = request.GET.get('id', '')
    return render(request, 'user/modify_passwd.html', {'id': _id})

def modify_passwd(request):
    _id = request.POST.get('id', '')
    old_password = request.POST.get('old_password', '')
    new_password = request.POST.get('new_password', '')
    rt, error = models.validate_modify_passwd(_id, old_password, new_password)
    if rt:
        models.modify_passwd(_id, new_password)
        return HttpResponseRedirect('/user/list_user/')
    else:
        return render(request, 'user/modify_passwd.html', {'id': _id, 'error': error})
