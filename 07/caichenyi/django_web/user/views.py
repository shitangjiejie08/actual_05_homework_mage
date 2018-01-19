from django.shortcuts import render
from django.http import HttpResponse

from . import models

# Create your views here.

def index(request):
    return render(request, 'user/login.html')

def login(request):
    name = request.POST.get('name', '')
    password = request.POST.get('password', '')
    users = models.load_users()
    rt_status, rt_reason = models.validate_login(name, password, users)
    if rt_status:
        context = {'users': models.list_users(users)}
        return render(request, 'user/list.html', context)
    else:
        context = {'error': rt_reason, 'name': name, 'password': password}
        return render(request, 'user/login.html', context)

def require_list(request):
    context = {'users': models.list_users(models.load_users())}
    return render(request, 'user/list.html', context)

def list(request):
    field = request.POST.get('list', '')
    print(field)
    context = {'users': models.list_users(models.load_users(), field)}
    return render(request, 'user/list.html', context)

def delete(request):
    name = request.GET.get('name', '')
    models.delete_user(name, models.load_users())
    context = {'users': models.list_users(models.load_users())}
    return render(request, 'user/list.html', context)

def require_edit(request):
    name = request.GET.get('name', '')
    context = {'name': name}
    return render(request, 'user/edit.html', context)

def edit(request):
    name = request.POST.get('name', '')
    password = request.POST.get('password', '')
    age = request.POST.get('age', '')
    tel = request.POST.get('tel', '')
    rt_status, rt_reason = models.validate_modify_user(name, age, tel, password)
    if rt_status:
        models.modify_user(name, age, tel, password, models.load_users())
        context = {'users': models.list_users(models.load_users())}
        return render(request, 'user/list.html', context)
    else:
        context = {'name': name, 'password': password, 'age': age, 'tel': tel, 'error': rt_reason}
        return render(request, 'user/edit.html', context)

def add(request):
    name = request.POST.get('name', '')
    password = request.POST.get('password', '')
    age = request.POST.get('age', '')
    tel = request.POST.get('tel', '')
    if name or password or age or tel:
        rt_status, rt_reason = models.validate_add_user(name, age, tel, password, models.load_users())
        if rt_status:
            models.add_user(name, age, tel, password, models.load_users())
            context = {'users': models.list_users(models.load_users())}
            return render(request, 'user/list.html', context)
        else:
            context = {'name': name, 'password': password, 'age': age, 'tel': tel, 'error': rt_reason}
            return render(request, 'user/add.html', context)
    else:
        return render(request, 'user/add.html')