from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect

from . import models

# Create your views here.

def requier_login(request):
    return render(request, 'user/login.html')

def login(request):
    username = request.POST.get('username','')
    password = request.POST.get('password','')
    print(username,password)
    rt = models.validate_login(username, password)
    if rt:
        #return HttpResponse('success')
        return HttpResponseRedirect('/user/list_user/')
    else:
        context = {'error': '用户名或密码错误。', 'username': username, 'password': password}
        return render(request,'user/login.html', context)
    return HttpResponse('login')

def list_user(request):
    users = models.load_users(models.path)
    users = list(users.values())
    return render(request,'user/list.html',{'users': users})

def delete_user(request):
    name = request.GET.get('name','')
    models.delete_user(name)
    return HttpResponseRedirect('/user/list_user/')

def view_user(request):
    name = request.GET.get('name','')
    users = models.find_user(name)[0]
    print(users)
    return render(request,'user/edit.html', {'users': users})
#    users = models.delete_user(name)
#    return render(request, 'user/edit.html', {'users': users})

def modify(request):
    name = request.POST.get('name','')
    password = request.POST.get('password','')
    tel = request.POST.get('tel','')
    age = request.POST.get('age','')
    models.modify_user(name, age, tel, password)
    return HttpResponseRedirect('/user/list_user/')

def create_user(request):
    return render(request, 'user/create.html')

def save_user(request):
    name = request.POST.get('name','')
    password = request.POST.get('password','')
    tel = request.POST.get('tel','')
    age = request.POST.get('age','')
    rt_status, rt_reason = models.validate_add_user(name, age, tel, password)
    print(rt_status,rt_reason)
    if rt_status:
        models.add_user(name, age, tel, password)
        return HttpResponseRedirect('/user/list_user/')
    else:
        context = {'error': rt_reason, 'name': name, 'password': password, 'tel': tel, 'age': age}
        return render(request,'user/create.html', context)





