#encoding: utf-8
from django.shortcuts import render
from django.http import HttpResponseRedirect,HttpResponse

# Create your views here.
from . import models
import json

USER_FILE = 'C:\eclipse\workspace\messages\\users.json'
user_info_tpl = '|{0:>20}|{1:>5}|{2:>20}|{3:>20}|'
user_info_header = user_info_tpl.format('name', 'age', 'telephone', 'password')

def index(request):
    return render(request, 'usermanage/index.html')

def get_users():
    fhandler = open(USER_FILE,'rt')
    cxt = fhandler.read()
    fhandler.close()
    return json.loads(cxt)

def find(request):
    return render(request, 'usermanage/find.html')

def find_save(request):
    find_name = request.GET.get('find_name', '')
    users = get_users()

    for user in users:
        if find_name == user['username']:
            find_users = user_info_tpl.format(user['username'], user['age'], user['tel'], '*' * len(user['password']))
            break
        else:
            find_users = "用户不存在"

    return HttpResponse(find_users)
    pass


def add(request):
    return render(request, 'usermanage/add.html')

def add_save(request):
    add_username = request.GET.get('add_username', '')
    add_password = request.GET.get('add_password', '')
    add_age = request.GET.get('add_age', '')
    add_tel = request.GET.get('add_tel', '')
    users = get_users()
    for user in users:
        if add_username == user['username']:
            add_users = "用户已存在，不能添加。"
            break
        else:
            users.append({'username' : add_username, 'password' : add_password, 'age' : add_age, 'tel': add_tel})
            fhandler = open(USER_FILE,'wt')
            fhandler.write(json.dumps(users))
            fhandler.close()
            add_users = "用户添加成功。"
            break
    return HttpResponse(add_users)















