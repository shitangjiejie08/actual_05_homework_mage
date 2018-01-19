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
        return HttpResponseRedirect('/user/list_user/')
    else:
        context = {'error' : '用户名或密码错误', 'username' : username, 'password' : password}
        return render(request, 'user/login.html', context)
def list_user(request):
    if request.session.get('user') is None:
        return HttpResponseRedirect('/user/require_login/')
    users = models.get_uesrs()
    return render(request, 'user/list.html', {'users' : users})
def delete_user(request):
    if request.session.get('user') is None:
        return HttpResponseRedirect('/user/require_login/')
    user_id = request.GET.get('id', '')
    models.delete_user(user_id)
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
    id = request.GET.get('id', '')
    user = models.get_user_by_name(id)
    return render(request, 'user/view.html', user)
def viewpasswd_user(request):
    if request.session.get('user') is None:
        return HttpResponseRedirect('/user/require_login/')
    user_id = request.GET.get('id', '')
    user = models.get_user_by_name(user_id)
    return render(request, 'user/userpasswd.html',user)
def changepasswd_user(request):
    user_id = request.POST.get('id', '')
    old_passwd = request.POST.get('oldpasswd', '')
    new_passwd = request.POST.get('newpasswd', '')
    get_passwd = models.get_userpasswd(user_id)
    user = models.get_user_by_name(user_id)
    if old_passwd == get_passwd:
        models.change_userpasswd(new_passwd,user_id)
        return HttpResponseRedirect('/user/list_user/')
    else:
        user['error'] = '旧密码输入有误，请重新输入'
        return render(request, 'user/userpasswd.html', user)






def modify_user(request):
    if request.session.get('user') is None:
        return HttpResponseRedirect('/user/require_login/')
    user_id = request.POST.get('id', '')
    username = request.POST.get('name','')
    age = request.POST.get('age', '')
    tel = request.POST.get('tel', '')
    rt, error = models.validate_modify_user( age, tel)
    if rt:
        #验证成功
        models.modify_user(user_id, age, tel)
        return HttpResponseRedirect('/user/list_user/')
    else:
        context = {}
        context['error'] = error
        context['name'] = username
        context['age'] = age
        context['tel'] = tel

        return render(request, 'user/view.html', context)
def logout(request):
    request.session.flush()
    return HttpResponseRedirect('/user/require_login/')
