from django.shortcuts import render
from django.http import HttpResponse

from . import models

# Create your views here.

def __validateLogin__(name, password, users):
    for user in users.values():
        if user['name'] == name and user['password'] == password:
            return True
    return False

def __validateInput__(name, password, age, tel, users, action):
    if action == 'add':
        if len(name) < 0 or len(name) > 8:
            return False, '用户名必须在0到8个字符之间'
        if not (age.isdigit() and int(age) > 0 and int(age) < 100):
            return False, '年龄必须是1到100的整数'
        if name in users:
            return False, '添加用户失败, 失败原因: 用户名已存在'
        return True, ''
    elif action == 'modify':
        if name not in users:
            return False, '更新用户失败, 错误原因: 用户名不存在'
        if len(password) < 8:
            return False, '密码长度必须大于等于8个字符'
        if not (age.isdigit() and int(age) > 0 and int(age) < 100):
            return False, '年龄必须是1到100的整数'
        return True, ''

def __validateDelete__(name, users):
    user = users.get(name)
    if user:
        return True
    else:
        return False

def __validateModify__(name, age, tel, password, users):
    if name not in users:
        return False, '更新用户失败, 错误原因: 用户名不存在'
    if len(password) < 8:
        return False, '密码长度必须大于等于8个字符'
    if not (age.isdigit() and int(age) > 0 and int(age) < 100):
        return False, '年龄必须是1到100的整数'
    return True, ''

def __inputInfo__(request, action):
    name = request.POST.get('name', '')
    password = request.POST.get('password', '')
    if action == 'input':
        age = request.POST.get('age', '')
        tel = request.POST.get('tel', '')
        return name, password, age, tel
    elif action == 'login':
        return name, password
    elif action == 'delete' or action == 'find':
        return name
    elif action == 'list_mode':
        list_mode = request.POST.get('list_mode', '')
        return list_mode

def index(request):
    context = {"users": models.get_users()}
    return render(request, 'users_manage/index.html', context)

def login(request):
    name, password = __inputInfo__(request, 'login')
    users = models.get_users()
    if name and password:
        if __validateLogin__(name, password, users):
            return render(request, 'users_manage/home.html')
        else:
            context = {'error': '用户验证失败'}
            return render(request, 'users_manage/login.html', context)
    else:
        context = {'name': name, 'password': password, 'error': '用户或密码不能为空'} if name or password else {}
        return render(request, 'users_manage/login.html', context)

def home(request):
    return render(request, 'users_manage/home.html')

def add(request):
    name, password, age, tel = __inputInfo__(request, 'input')
    users = models.get_users()
    if name and password and age and tel:
        rt_status, rt_reason = __validateInput__(name, password, age, tel, users, 'add')
        if rt_status:
            users[name] = {'name': name, 'password': password, 'age': age, 'tel': tel}
            models.save_users(users)
            context = {'result': '用户添加成功，请继续操作'}
            return render(request, 'users_manage/home.html', context)
        else:
            context = {'name': name, 'password': password, 'age': age, 'tel': tel, 'action': 'add', 'action_show': '添加', 'error': rt_reason}
            return render(request, 'users_manage/input.html', context)
    else:
        context = {'name': name, 'password': password, 'age': age, 'tel': tel, 'action': 'add', 'action_show': '添加', 'error': '输入的信息不能为空'} if (name or password or age or tel) else {'action': 'add', 'action_show': '添加'}
        return render(request, 'users_manage/input.html', context)

def delete(request):
    name = __inputInfo__(request, 'delete')
    users = models.get_users()
    if name:
        if __validateDelete__(name, users):
            users.pop(name, None)
            models.save_users(users)
            context = {'result': '用户删除成功，请继续操作'}
            return render(request, 'users_manage/home.html', context)
        else:
            context = {'action': 'delete', 'action_show': '删除', 'error': '没有该用户'}
            return render(request, 'users_manage/input.html', context)
    else:
        context = {'action': 'delete', 'action_show': '删除', 'error': '输入的信息不能为空'} if name else {'action': 'delete', 'action_show': '删除'}
        return render(request, 'users_manage/input.html', context)

def modify(request):
    name, password, age, tel = __inputInfo__(request, 'input')
    users = models.get_users()
    if name and password and age and tel:
        rt_status, rt_reason = __validateInput__(name, password, age, tel, users, 'modify')
        if rt_status:
            users[name] = {'name': name, 'password': password, 'age': age, 'tel': tel}
            models.save_users(users)
            context = {'result': '用户修改成功，请继续操作'}
            return render(request, 'users_manage/home.html', context)
        else:
            context = {'name': name, 'password': password, 'age': age, 'tel': tel, 'action': 'modify', 'action_show': '修改', 'error': rt_reason}
            return render(request, 'users_manage/input.html', context)
    else:
        context = {'name': name, 'password': password, 'age': age, 'tel': tel, 'action': 'modify', 'action_show': '修改', 'error': '输入的信息不能为空'} if (name or password or age or tel) else {'action': 'modify', 'action_show': '修改'}
        return render(request, 'users_manage/input.html', context)

def list(request):
    action = __inputInfo__(request, 'list_mode')
    users = models.get_users()
    if action:
        context = {'list_mode': action, 'users': models.list_users(users, action)}
        return render(request, 'users_manage/list.html', context)
    else:
        context = {'action': 'list', 'action_show': '排序'}
        return render(request, 'users_manage/input.html', context)

def find(request):
    action = __inputInfo__(request, 'find')
    users = models.get_users()
    if action:
        context = {'list_mode': action, 'users': models.find_users(users, action)}
        return render(request, 'users_manage/list.html', context)
    else:
        context = {'action': 'find', 'action_show': '查找'}
        return render(request, 'users_manage/input.html', context)