from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.core.exceptions import ObjectDoesNotExist

# Create your views here.
from . import models
import hashlib,json
from . import forms
from utils.crypt import CryptUtils


# def md5(p):
#     p=p.encode('utf-8')
#     md5 = hashlib.md5()
#     md5.update(p)
#     return md5.hexdigest()

def require_login(request):
    if request.session.get('user'):
        return HttpResponseRedirect('/user/list_user/')
    form = forms.LoginForm()
    return render(request, 'user/login.html',{"form":form})

def login(request):
    if request.session.get('user'):
        return HttpResponseRedirect('/user/list_user/')
    form = forms.LoginForm(request.POST)
    if form.is_valid():
        request.session['user'] = {'username' : form.cleaned_data['username']}
        return HttpResponseRedirect('/user/list_user/')
    else:
        return render(request, 'user/login.html', {'form' : form})


def list_user(request):
    if request.session.get('user') is None:
        return HttpResponseRedirect('/user/require_login/')
    users = models.User.objects.all()
    return render(request, 'user/list.html', {'users' : users})

def delete_user(request):
    if request.session.get('user') is None:
        return HttpResponseRedirect('/user/require_login/')
    _id = request.GET.get('id', '')
    rt = models.User.objects.filter(id=_id)
    #user = models.User.objects.filter(_id).delete()
    if rt:
        models.User.objects.filter(id=_id).delete()
    return HttpResponseRedirect('/user/list_user/')


def create_user(request):
    if request.session.get('user') is None:
        return HttpResponseRedirect('/user/require_login/')
    form = forms.CreateUserForm()
    return render(request, 'user/create.html',{"form":form})


def save_user(request):
    if request.session.get('user') is None:
        return HttpResponseRedirect('/user/require_login/')
    form = forms.CreateUserForm(request.POST)
    if form.is_valid():
        user = models.User(username=form.cleaned_data['username'], \
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
    uid = request.GET.get('id', '')
    form = None
    try:
        user = models.User.objects.filter(pk=uid)
        user = user.values()[0]
        form = forms.ModifyUserForm(user)
    except ObjectDoesNotExist as e:
        form = ModifyUserForm()

    return render(request, 'user/view.html', {'form' : form})

def modify_user(request):
    if request.session.get('user') is None:
        return HttpResponseRedirect('/user/require_login/')
    
    form = forms.ModifyUserForm(request.POST)
    if form.is_valid():
        user = models.User.objects.get(pk=form.cleaned_data['id'])
        user.username = form.cleaned_data.get('username')
        user.tel = form.cleaned_data.get('tel')
        user.age = form.cleaned_data.get('age')
        user.save()
        return HttpResponseRedirect('/user/list_user/')
    else:
        return render(request, 'user/view.html', {'form' : form})
 

def view_password(request):
    if request.session.get('user') is None:
        return HttpResponseRedirect('/user/require_login/')
    uid = request.GET.get('id', '')
    print(uid,'uid==========')
    try:
        user = models.User.objects.filter(pk=int(uid))
        user = user.values()[0]
        print(user,'---------')
        form = forms.PassForm(user)
    except ObjectDoesNotExist as e:
        form = forms.PassForm()
        print(e)
    return render(request, 'user/view_pass.html', {'form' : form})

def modify_pass(request):
    if request.session.get('user') is None:
        return HttpResponseRedirect('/user/require_login/')
    form = forms.PassForm(request.POST)
    if form.is_valid():
        uid = request.POST.get('id','')
        user = models.User.objects.get(pk=int(uid))
        user.password = CryptUtils.md5(form.cleaned_data.get('confirm_pass'))
        user.save()
        request.session.flush()
        return HttpResponseRedirect('/user/require_login/')
    else:
        return render(request,"user/view_pass.html",{'form':form})

def logout(request):
    request.session.flush()
    return HttpResponseRedirect('/user/require_login/')
