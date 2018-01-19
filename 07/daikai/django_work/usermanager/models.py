from django.db import models

# Create your models here.
#encoding: utf-8

import json

path = 'users.txt'

user_info_tpl = '|{0:>20}|{1:>5}|{2:>20}|{3:>20}|'
user_info_header = user_info_tpl.format('name', 'age', 'telephone', 'password')

def load_users(path):
    fhandler = open(path, 'rt')
    users = json.loads(fhandler.read())
    fhandler.close()
    return users

def dump_users(path, users):
    fhandler = open(path, 'wt')
    fhandler.write(json.dumps(users))
    fhandler.close()


def validate_login(name, password):
    users = load_users(path)

    for user in users.values():
        if user['name'] == name and user['password'] == password:
            return True

    return False


'''
return True/False, ''
'''
def validate_add_user(name, age, tel, password):
    users = load_users(path)
    if len(name) < 0 or len(name) > 8:
        return False, '用户名必须在0到8个字符之间'

    if not(age.isdigit() and int(age) > 0 and int(age) < 100):
        return False, '年龄必须是1到100的整数'

    if name in users:
        return False, '添加用户失败, 失败原因: 用户名已存在'

    return True, ''


def add_user(name, age, tel, password):
    users = load_users(path)
    users[name] = {'name' : name, 'age' : age, 'tel' : tel, 'password' : password}
    dump_users(path, users)


def input_add_user():
    user_txt = input('请输入用户信息(用户名:年龄:电话:密码):')
    name, age, tel, password = user_txt.split(':')
    return name, age, tel, password


def input_delete_user():
    return input('请输入你要删除的用户名:')


def validate_delete_user(name, users):
    user = users.get(name)
    if user:
        return True, ''
    else:
        return False, '删除用户失败, 失败原因: 用户名不存在'


def delete_user(name):
    users = load_users(path)
    users.pop(name, None)
    dump_users(path, users)


def input_modify_user():
    user_txt = input('请输入用户信息(用户名:年龄:电话:密码):')
    name, age, tel, password = user_txt.split(':')
    return name, age, tel, password


def validate_modify_user(name, age, tel, password, users):
    if name not in users:
        return False, '更新用户失败, 错误原因: 用户名不存在'

    if len(password) < 8:
        return False, '密码长度必须大于等于8个字符'

    if not(age.isdigit() and int(age) > 0 and int(age) < 100):
        return False, '年龄必须是1到100的整数'

    return True, ''


def modify_user(name, age, tel, password):
    users = load_users(path)
    users[name] = {'name' : name, 'age' : age, 'tel' : tel, 'password' : password}
    dump_users(path, users)

def find_user(name, users):
    rt_list = []
    for user in users.values():
        if user['name'].find(name) != -1:
            rt_list.append(user)

    return rt_list

def list_user(field, users):
    user_list = list(users.values())
    return sorted(user_list, key=lambda x: x.get(field))

