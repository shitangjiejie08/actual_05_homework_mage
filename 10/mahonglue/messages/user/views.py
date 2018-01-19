from django.shortcuts import render

from django.http import HttpResponse, HttpResponseRedirect

from . import models
from .forms import LoginForm, CreateForm, ViewForm
from utils import crypt

# Create your views here.

def require_login(request):
    if request.session.get('user'):
        return HttpResponseRedirect('/user/list_user/')

    return render(request, 'user/login.html')


def login(request):

    if request.session.get('user'):
        return HttpResponseRedirect('/user/list_user/')

    if request.method == "POST":
        form = LoginForm(request.POST)
        if form.is_valid():
            cleaned_data = form.cleaned_data #在验证通过之后才有cleaned_data，不然是没有的
            username = cleaned_data.get('username', '')
            password = cleaned_data.get('password', '')
            request.session["user"] = {"username":username}
            return HttpResponseRedirect('/user/list_user/')

    else:
        form = LoginForm()
    return render(request, 'user/login.html', {"form":form})


def list_user(request):
    if request.session.get('user') is None:
        return HttpResponseRedirect('/user/require_login/')
    users = models.User2.objects.all()
    print(users)
    return render(request, 'user/list.html', {'users' : users})


def delete_user(request):
    if request.session.get('user') is None:
        return HttpResponseRedirect('/user/require_login/')
    _id = request.GET.get('id', '')
    user = models.User2.objects.get(id=_id)
    print(user)
    if user:
        user.delete()
    return HttpResponseRedirect('/user/list_user/')


def create_user(request):
    if request.session.get('user') is None:
        return HttpResponseRedirect('/user/require_login/')
    if request.method == "POST":
        form = CreateForm(request.POST)
        if form.is_valid():
            cleaned_data = form.cleaned_data
            username = cleaned_data.get('username', '')
            password = cleaned_data.get('password', '')
            password = crypt.md5(password)
            age = cleaned_data.get('age', '')
            tel = cleaned_data.get('tel', '')
            print(cleaned_data)
            user = models.User2(username=username, password=password, age=age, tel=tel)
            user.save()
            return HttpResponseRedirect('/user/list_user/')
    else:
        form = CreateForm()
        print("家具啊")
    return render(request, 'user/create.html', {"form":form})


def view_user(request):
    if request.session.get('user') is None:
        return HttpResponseRedirect('/user/require_login/')

    if request.method == "POST":
        uid = request.POST.get('id', '')
        print("uid:", uid)
        user = models.User2.objects.get(id=uid)
        print(user)
        form = ViewForm(request.POST)
        if form.is_valid():
            cleaned_data = form.cleaned_data
            username = cleaned_data.get("username","")
            age = cleaned_data.get("age","")
            tel = cleaned_data.get("tel","")
            user.username = username
            user.age = age
            user.tel = tel
            user.save()
            return HttpResponseRedirect('/user/list_user/')
    else:
        uid = request.GET.get('id', '')
        print("uid:", uid)
        user = models.User2.objects.get(id=uid)
        print(user)
        form = ViewForm()
    return render(request, 'user/view.html', {"form":form,"user":user})



def logout(request):
    request.session.flush()
    return HttpResponseRedirect('/user/require_login/')
