from django.shortcuts import render

from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from django.core.exceptions import ObjectDoesNotExist
from django.urls import reverse

from . import models
from .forms import LoginForm, CreateUserForm, ModifyUserForm
from utils.crypt import CryptUtils

import json
# Create your views here.

def require_login(request):
    if request.session.get('user'):
        return HttpResponseRedirect(reverse('user:list_user'))

    form = LoginForm()
    return render(request, 'user/login.html', {'form' : form})


def login(request):

    if request.session.get('user'):
        return HttpResponseRedirect('/user/list_user/')

    form = LoginForm(request.POST)
    if form.is_valid():
        request.session['user'] = {'username' : form.cleaned_data['username']}
        return HttpResponseRedirect('/user/list_user/')
    else:
        return render(request, 'user/login.html', {'form' : form})


def list_user(request):
    if request.session.get('user') is None:
        return HttpResponseRedirect('/user/require_login/')
    users = models.User2.objects.all()
    return render(request, 'user/list.html', {'users' : users})


def delete_user(request):
    if request.session.get('user') is None:
        return HttpResponseRedirect('/user/require_login/')
    _id = request.GET.get('id', '')

    # models.User.delte_by_id(_id)

    # user = models.User(id=_id)
    # user.delete()

    user = models.User.get_by_id(_id)
    print(user)
    if user:
        user.delete()

    return HttpResponseRedirect('/user/list_user/')


def create_user(request):
    if request.session.get('user') is None:
        return HttpResponseRedirect('/user/require_login/')
    form = CreateUserForm()
    return render(request, 'user/create.html', {'form' : form})


def save_user(request):
    if request.session.get('user') is None:
        return HttpResponseRedirect('/user/require_login/')

    form = CreateUserForm(request.POST)
    if form.is_valid():
        user = models.User2(username=form.cleaned_data['username'], \
                            password=CryptUtils.md5(form.cleaned_data['password']), \
                            age=form.cleaned_data['age'], \
                            tel=form.cleaned_data['tel'])
        user.save()
        return HttpResponseRedirect('/user/list_user/')
    else:
        return render(request, 'user/create.html', {'form' : form})



def save_ajax(request):
    if not request.session.get('user'):
        return JsonResponse({'status':403, 'errors':['用户未登录']})

   
    form = CreateUserForm(request.POST)
    print(form)
    if form.is_valid():
        user = models.User2(username=form.cleaned_data['username'], \
                            password=CryptUtils.md5(form.cleaned_data['password']), \
                            age=form.cleaned_data['age'], \
                            tel=form.cleaned_data['tel'])
        user.save()
        return JsonResponse({"status" : 200, "result" : ""})
    else:
        return JsonResponse({'status':400, "result": "", "errors": json.loads(form.errors.as_json())})

def get_ajax(request):
    # if not request.session.get('user'):
    #     return JsonResponse({'status':403, 'errors':['用户未登录']})
    if not request.session.get('user'):
         return JsonResponse({'data':[]})
 
    users = models.User2.objects.all()
    users = [user.as_dict() for user in users]
    print(users)
    return HttpResponse(json.dumps({"data" : users}))


def view_user(request):
    if request.session.get('user') is None:
        return HttpResponseRedirect('/user/require_login/')
    _id = request.GET.get('id', '')
    form = None
    try:
        user = models.User2.objects.get(pk=_id)
        form = ModifyUserForm(user.as_dict())
    except ObjectDoesNotExist as e:
        form = ModifyUserForm()

    return render(request, 'user/view.html', {'form' : form})

def modify_user(request):
    if request.session.get('user') is None:
        return HttpResponseRedirect('/user/require_login/')

    form = ModifyUserForm(request.POST)

    if form.is_valid():
        user = models.User2.objects.get(pk=form.cleaned_data['id'])
        user.username = form.cleaned_data.get('username')
        user.tel = form.cleaned_data.get('tel')
        user.age = form.cleaned_data.get('age')
        user.save()
        return HttpResponseRedirect('/user/list_user/')
    else:
        return render(request, 'user/view.html', {'form' : form})


def logout(request):
    request.session.flush()
    return HttpResponseRedirect('/user/require_login/')
