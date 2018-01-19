from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from . import models
from django.views.decorators.csrf import  csrf_exempt
# Create your views here.


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
        #return HttpResponse('success')
        return HttpResponseRedirect('/UserManagement/list_user/')
    else:
        context = {'error': '用户名或密码错误', 'username':username, 'password':password}
        return render(request, 'UserManagement/login.html', context)


@csrf_exempt
def list_user(request):
    users_file = models.load_users(models.path)
    users_lst = models.list_user('age',users_file)
    users_text = {'users':users_lst}

    print(users_text)
    return render(request, 'UserManagement/list.html', users_text)

@csrf_exempt
def add_user(request):
    users = models.load_users(models.path)
    username = request.POST.get('username', '')
    age = request.POST.get('age', '')
    tel = request.POST.get('tel', '')
    password = request.POST.get('password', '')
    #print(username,age,tel,password)
    #print(users)
    rt_status, rt_reason = models.validate_add_user(name=username, age=age, tel=tel, password=password, users=users)
    if rt_status:
        models.add_user(name=username, age=age, tel=tel, password=password, users=users)
        print(users)
        models.dump_users(models.path,users)
        return HttpResponseRedirect('/UserManagement/list_user/')
    else:
        err_txt = {"error":rt_status}
        return render(request, 'UserManagement/add_user.html',err_txt)



@csrf_exempt
def del_user(request):
    users = models.load_users(models.path)
    name = request.POST.get('username', '')
    rt_status, rt_reason = models.validate_delete_user(name, users)
    if rt_status:
        models.delete_user(name, users)
        models.dump_users(models.path, users)
        return HttpResponseRedirect('/UserManagement/list_user/')
    else:
        err_text = {'error':rt_reason}
        return render(request, 'UserManagement/del_user.html', err_text)



@csrf_exempt
def chg_user(request):
    users = models.load_users(models.path)
    username = request.POST.get('username', '')
    age = request.POST.get('age', '')
    tel = request.POST.get('tel', '')
    password = request.POST.get('password', '')
    rt_status, rt_reason = models.validate_modify_user(name=username, age=age, tel=tel, password=password, users=users)
    if rt_status:
        models.modify_user(name=username, age=age, tel=tel, password=password, users=users)
        models.dump_users(models.path, users)
        return HttpResponseRedirect('/UserManagement/chg_user/')
    else:
        err_text = {'error':rt_reason}
        return render(request, 'UserManagement/chg_user.html', err_text)


# @csrf_exempt
# def find_user(request):
#     users = models.load_users(models.path)
#     username = request.POST.get('username', '')
#     rt_list = find_user(name=username, users=users)
#     if rt_list:
#         print(user_info_header)
#         for user in rt_list:
#             print(user_info_tpl.format(user['name'], user['age'], user['tel'], '*' * len(user['password'])))
#     else:
#         print('没有该用户信息')