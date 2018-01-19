from django.shortcuts import render

from django.http import HttpResponse, HttpResponseRedirect
from . import models
# Create your views here.


def require_login(request):
    return render(request, 'usermanager/login.html')

def login(request):
    username = request.POST.get('username', '')
    password = request.POST.get('password', '')
    print(username, password)
    rt = models.validate_login(username, password)
    if rt:
        return HttpResponseRedirect('/usermanager/list_user/') 
    else:
        context = {'error': '用户名或密码错误', 'username': username, 'password': password}
        return render(request, 'usermanager/login.html', context)

def list_user(request):
    users = models.load_users(models.path)
    users = list(users.values())
    return render(request, 'usermanager/list.html', {'users': users}) 

def delete_user(request):
    name = request.GET.get('name', '')
    print(name)
    models.delete_user(name)
    return HttpResponseRedirect('/usermanager/list_user/')

def edit_user(request):
    name = request.GET.get('name', '')
    users = models.load_users(models.path)
    edit_user = users[name]
    print(edit_user)
    return render(request, 'usermanager/update.html', {'user':edit_user})


def update(request):
    name = request.POST.get('name', '')
    password = request.POST.get('password', '')
    age = request.POST.get('age', '')
    tel = request.POST.get('tel', '')
    models.modify_user(name, age, tel, password)
    return HttpResponseRedirect('/usermanager/list_user/')

def create_user(request):
    return render(request, 'usermanager/add.html')

def save_user(request):
    name = request.POST.get('name', '')
    password = request.POST.get('password', '')
    age = request.POST.get('age', '')
    tel = request.POST.get('tel', '')
    status,reason = models.validate_add_user(name, age, tel, password)
    if status:
        models.add_user(name, age, tel, password)
        return HttpResponseRedirect('/usermanager/list_user/')
    else:
        cxt = {'name':name, 'age':age, 'tel':tel, 'password':password, 'error':reason}
        return render(request, 'usermanager/add.html', cxt)
