# encoding: utf-8
# Author: Cai Chenyi

import json

def user_load(path):
    '''
    加载用户信息。将用户信息加载到字典users{}中
    '''
    with open(path, 'rt') as fhandler:
        return json.loads(fhandler.read())


def user_login(num):
    '''
    用户认证登入。返回Truefa，则登入成功；返回False，则登入失败
    '''
    for i in range(num):
        name = input('请输入用户名:')
        password = input('请输入密码:')
        for user in users.values():
            if user['name'] == name and user['password'] == password:
                return True
    return False

def user_add():
    '''
    添加用户信息
    '''
    user_txt = input('请输入用户信息(用户名:密码:年龄:电话):')
    name, password, age, tel = user_txt.split(':')
    if name in users:
        print('用户存在')
    else:
        users[name] = {'name': name, 'password': password, 'age': age, 'tel': tel}

def user_delete():
    '''
    删除用户信息
    '''
    name = input('请输入你要删除的用户名:')
    if users.pop(name, None):
        print('删除成功')
    else:
        print('删除用户失败, 失败原因: 用户名不存在')

def user_update():
    '''
    更新用户信息
    '''
    user_txt = input('请输入用户信息(用户名:密码:年龄:电话):')
    name, password, age, tel = user_txt.split(':')
    if name in users:
        users[name] = {'name': name, 'password': password, 'age': age, 'tel': tel}
    else:
        print('更新用户失败, 错误原因: 用户名不存在')

def user_find():
    '''
    查询用户信息
    '''
    name = input('请输入你要查询的用户名:')
    is_exists = False
    print(user_info_header)
    for user in users.values():
        if user['name'].find(name) != -1:
            print(user_info_tpl.format(user['name'], '*' * len(user['password']), user['age'], user['tel']))
            is_exists = True
    if not is_exists:
        print('没有该用户信息')

def user_list():
    '''
    罗列所有用户信息
    '''
    list_action = input('请输入排序规则(name,age,tel)：')
    user_list = sorted(list(users.values()), key=lambda x: x[list_action])
    for user in user_list:
        print(user_info_tpl.format(user['name'], '*' * len(user['password']), user['age'], user['tel']))

def user_exit(path):
    '''
    退出系统
    '''
    with open(path, 'wt') as fhandler:
        fhandler.write(json.dumps(users))

path = 'users.txt'
user_info_tpl = '|{0:>20}|{1:>20}|{2:>5}|{3:>20}|'
user_info_header = user_info_tpl.format('name', 'password', 'age', 'tel')

users = user_load(path)

if user_login(3):
    while True:
        action = input('please input(find/list/add/delete/update/exit):')
        if action == 'add':
            user_add()
        elif action == 'delete':
            user_delete()
        elif action == 'update':
            user_update()
        elif action == 'find':
            user_find()
        elif action == 'list':
            user_list()
        elif action == 'exit':
            user_exit(path)
            exit()
        else:
            print('命令错误。')
else:
    print('超过认证次数，认证失败。')
