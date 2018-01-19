from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from . import models
from django.views.decorators.csrf import  csrf_exempt
# Create your views here.

@csrf_exempt
def require_login(request):
    return render(request, 'UserManagement/login.html')


@csrf_exempt
def login(request):
    print(request.POST)
    username = request.POST.get('username', '')
    password = request.POST.get('password', '')
    print(username,password)
    rt = models.validate_login(username, password)
    print(rt)
    if rt:
        request.session['user'] = rt         ##### session
        #return HttpResponse('success')
        return HttpResponseRedirect('/UserManagement/list_user/')
    else:
        context = {'error': '用户名或密码错误', 'username':username, 'password':password}
        return render(request, 'UserManagement/login.html', context)


@csrf_exempt
def list_user(request):
    if request.session.get('user') is None:
        return HttpResponseRedirect('/UserManagement/require_login/')
    else:

        users_lst = models.get_users()
        users_text = {'users':users_lst}
        print(users_text)
        return render(request, 'UserManagement/list.html', users_text)

@csrf_exempt
def add_user(request):
    if request.session.get('user') is None:
        return HttpResponseRedirect('/UserManagement/require_login/')
    else:
        return render(request, 'UserManagement/add_user.html')



def add_user_save(request):
    if request.session.get('user') is None:
        return HttpResponseRedirect('/UserManagement/require_login/')
    else:
        username = request.POST.get('username', '')
        age = request.POST.get('age', '')
        tel = request.POST.get('tel', '')
        passwd = request.POST.get('password', '')
        # print(username,age,tel,password)
        # print(users)
        rt_status, rt_reason = models.validate_add_user(name=username, age=age)
        print('11111111111111111111111111')
        if rt_status:
            print('222222222222222222')
            models.add_user(username=username, age=age, tel=tel, passwd=passwd)
            return HttpResponseRedirect('/UserManagement/list_user/')
        else:
            err_txt = {"error": rt_reason, "username": username, "age": age, "tel": tel, "password": passwd}
        return render(request, 'UserManagement/add_user.html', err_txt)

@csrf_exempt
def del_user(request):
    if request.session.get('user') is None:
        return HttpResponseRedirect('/UserManagement/require_login/')
    else:
        return render(request, 'UserManagement/del_user.html')

@csrf_exempt
def del_user_save(request):
    if request.session.get('user') is None:
        return HttpResponseRedirect('/UserManagement/require_login/')
    else:
        username = request.POST.get('username', '')
        rt_status, rt_reason = models.validate_delete_user(username)
        if rt_status:
            models.delete_user(username)
            return HttpResponseRedirect('/UserManagement/list_user/')
        else:
            err_text = {"error": rt_reason, "username": username}
            return render(request, 'UserManagement/del_user.html', err_text)



@csrf_exempt
def chg_user(request):
    if request.session.get('user') is None:
        return HttpResponseRedirect('/UserManagement/require_login/')
    else:
        return render(request, 'UserManagement/chg_user.html')


@csrf_exempt
def chg_user_save(request):
    if request.session.get('user') is None:
        return HttpResponseRedirect('/UserManagement/require_login/')
    else:

        users = models.load_users(models.path)
        username = request.POST.get('username', '')
        age = request.POST.get('age', '')
        tel = request.POST.get('tel', '')
        password = request.POST.get('password', '')
        rt_status, rt_reason = models.validate_modify_user(name=username, age=age, tel=tel, password=password, users=users)
        if rt_status:
            models.modify_user(name=username, age=age, tel=tel, password=password, users=users)
            models.dump_users(models.path, users)
            return HttpResponseRedirect('/UserManagement/list_user/')
        else:
            err_text = {"error": rt_reason, "username": username, "age": age, "tel": tel, "password": password}
            return render(request, 'UserManagement/chg_user.html', err_text)


@csrf_exempt
def find_user(request):
    if request.session.get('user') is None:
        return HttpResponseRedirect('/UserManagement/require_login/')
    else:
        username = request.POST.get('username', '')
        users_list = models.list_user(username,users)

@csrf_exempt
def logout(request):
    if request.session.get('user') is None:
        return HttpResponseRedirect('/UserManagement/require_login/')
    else:

        request.session.flush()
        return HttpResponseRedirect('/UserManagement/require_login')
