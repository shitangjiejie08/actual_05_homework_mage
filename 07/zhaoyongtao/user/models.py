from django.db import models

# Create your models here.
import json


path = 'appendix/user/users.txt'

user_info_tpl = '|{0:>20}|{1:>5}|{2:>20}|{3:>20}|'
user_info_header = user_info_tpl.format('name', 'age', 'telephone', 'password')

# read user data from file
def load_users():
    fhandler = open(path, 'rt')
    users = json.loads(fhandler.read())
    fhandler.close()
    return users

# save user data to file
def dump_users(users):
    fhandler = open(path, 'wt')
    fhandler.write(json.dumps(users))
    fhandler.close()

def validate_login(name, password):
    users = load_users()
    for user in users.values():
        if user['name'] == name and user['password'] == password:
            return True
    return False

'''
return True/False, ''
'''
def validate_add_user(name, age, tel, password):
    users = load_users()
    if len(name) < 0 or len(name) > 8:
        return False, '用户名必须在0到8个字符之间'

    if not(age.isdigit() and int(age) > 0 and int(age) < 100):
        return False, '年龄必须是1到100的整数'

    if name in users:
        return False, '添加用户失败, 失败原因: 用户名已存在'

    return True, ''


def add_user(name, age, tel, password):
    users = load_users()
    users[name] = {'name' : name, 'age' : age, 'tel' : tel, 'password' : password}
    f = open(path,'w')
    f.write(json.dumps(users))
    f.close()

def validate_delete_user(name):
    users = load_users()
    user = users.get(name)
    if user:
        return True, ''
    else:
        return False, '删除用户失败, 失败原因: 用户名不存在'


def delete_user(name):
    users = load_users()
    users.pop(name, None)
    dump_users(users)
    return True


def validate_modify_user(name, age, tel, password):
    users = load_users()
    if name not in users:
        return False, '更新用户失败, 错误原因: 用户名不存在'

    if len(password) < 8:
        return False, '密码长度必须大于等于8个字符'

    if not(age.isdigit() and int(age) > 0 and int(age) < 100):
        return False, '年龄必须是1到100的整数'

    return True, ''


def modify_user(name, age, tel, password):
    users = load_users()
    users[name] = {'name' : name, 'age' : age, 'tel' : tel, 'password' : password}
    dump_users(users)

