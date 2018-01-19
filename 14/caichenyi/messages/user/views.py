from django.shortcuts import render

from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from django.core.exceptions import ObjectDoesNotExist
from django.urls import reverse

from . import models
from .forms import LoginForm, CreateUserForm, ModifyUserForm, PasswordForm
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
        return HttpResponseRedirect(reverse('user:require_login'))
    _id = request.GET.get('id', '')
    user = None
    try:
        uid = request.GET.get('id', 0)
        user = models.User2.objects.get(pk=_id)
        user.delete()
    except ObjectDoesNotExist as e:
        pass
    return HttpResponseRedirect(reverse('user:list_user'))
    # if request.session.get('user') is None:
    #     return HttpResponseRedirect('/user/require_login/')
    # _id = request.GET.get('id', '')
    #
    # # models.User.delte_by_id(_id)
    #
    # # user = models.User(id=_id)
    # # user.delete()
    #
    # user = models.User.get_by_id(_id)
    # print(user)
    # if user:
    #     user.delete()
    #
    # return HttpResponseRedirect('/user/list_user/')


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


def modify_password(request):
    if request.session.get('user') is None:
        return JsonResponse({'status': 403, 'errors': ['用户未登录']})

    form = PasswordForm(request.POST)
    if form.is_valid():
        user = models.User2.objects.get(pk=form.cleaned_data['id'])
        user.password = form.cleaned_data['password']
        user.save()
        return JsonResponse({"status": 200, "result": ""})
    else:
        return JsonResponse({'status': 400, "result": "", "errors": json.loads(form.errors.as_json())})

    form = None
    if request.method == 'GET':
        try:
            _id = request.GET.get('id', 0)
            user = models.User2.objects.get(pk=_id)
            form = PasswordForm(initial={'password': '', 'id': _id})
        except ObjectDoesNotExist as e:
            form = PasswordForm()
    else:
        form = PasswordForm(request.POST)
        if form.is_valid():
            user = models.User2.objects.get(pk=form.cleaned_data['id'])
            user.password = form.cleaned_data['password']
            user.save()
            return HttpResponseRedirect(reverse('user:list_user'))

    return render(request, 'user/password.html', {'form': form})


def modify_user(request):
    if request.session.get('user') is None:
        return JsonResponse({'status': 403, 'errors': ['用户未登录']})

    form = ModifyUserForm(request.POST)
    if form.is_valid():
        user = models.User2.objects.get(pk=form.cleaned_data['id'])
        user.username = form.cleaned_data.get('username')
        user.tel = form.cleaned_data.get('tel')
        user.age = form.cleaned_data.get('age')
        user.save()
        return JsonResponse({"status": 200, "result": ""})
    else:
        return JsonResponse({'status': 400, "result": "", "errors": json.loads(form.errors.as_json())})
    # if request.session.get('user') is None:
    #     return HttpResponseRedirect('/user/require_login/')
    #
    # form = ModifyUserForm(request.POST)
    #
    # if form.is_valid():
    #     user = models.User2.objects.get(pk=form.cleaned_data['id'])
    #     user.username = form.cleaned_data.get('username')
    #     user.tel = form.cleaned_data.get('tel')
    #     user.age = form.cleaned_data.get('age')
    #     user.save()
    #     return HttpResponseRedirect('/user/list_user/')
    # else:
    #     return render(request, 'user/view.html', {'form' : form})


def logout(request):
    request.session.flush()
    return HttpResponseRedirect('/user/require_login/')

def get_ajax(request):
    if not request.session.get('user'):
         return JsonResponse({'data':[]})
    users = models.User2.objects.all()
    users = [message.as_dict() for message in users]
    return HttpResponse(json.dumps({"data" : users}))


def save_ajax(request):
    if not request.session.get('user'):
        return JsonResponse({'status': 403, 'errors': ['用户未登录']})

    form = CreateUserForm(request.POST)
    if form.is_valid():
        if form.cleaned_data['password'] == form.cleaned_data['other_password']:
            user = models.User2(username=form.cleaned_data['username'], \
                password=CryptUtils.md5(form.cleaned_data['password']), \
                age=form.cleaned_data['age'], \
                tel=form.cleaned_data['tel'])
            user.save()
            return JsonResponse({"status": 200, "result": ""})
    else:
        return JsonResponse({'status': 400, "result": "", "errors": json.loads(form.errors.as_json())})

