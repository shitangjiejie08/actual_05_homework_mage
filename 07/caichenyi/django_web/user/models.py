from django.db import models

import json
# Create your models here.

path = 'conf/users.txt'

def load_users():
    with open(path, 'rt') as f:
        return json.loads(f.read())

def dump_users(users):
    with open(path, 'wt') as f:
        f.write(json.dumps(users))

def list_users(users, field='name'):
    user_list = list(users.values())
    return sorted(user_list, key=lambda x: x.get(field))

def validate_login(name, password, users):
    for user in users.values():
        if user['name'] == name and user['password'] == password:
            return True, '用户认证成功'
    return False, '用户认证失败'

def delete_user(name, users):
    users.pop(name, None)
    dump_users(users)

def validate_add_user(name, age, tel, password, users):
    if name and age and tel and password:
        if name in users:
            return False, '用户名重复'
        if len(name) < 0 or len(name) > 8:
            return False, '用户名必须在0到8个字符之间'
        if not (age.isdigit() and int(age) > 0 and int(age) < 100):
            return False, '年龄必须是1到100的整数'
        if name in users:
            return False, '添加用户失败, 失败原因: 用户名已存在'
        return True, ''
    else:
        return False, '输入不能为空'

def add_user(name, age, tel, password, users):
    users[name] = {'name': name, 'age': age, 'tel': tel, 'password': password}
    dump_users(users)

def validate_modify_user(name, age, tel, password):
    if name and age and tel and password:
        if len(password) < 8:
            return False, '密码长度必须大于等于8个字符'
        if not (age.isdigit() and int(age) > 0 and int(age) < 100):
            return False, '年龄必须是1到100的整数'
        return True, ''
    else:
        return False, '输入不能为空'

def modify_user(name, age, tel, password, users):
    users[name] = {'name': name, 'age': age, 'tel': tel, 'password': password}
    dump_users(users)