#encoding:utf-8

'''
用户管理v4.0
Author:daikai

在用户管理功能中各功能修改为函数
登录验证、添加、修改、查询、列表、删除
用户信息文件读、写
使用json格式存储用户信息
列表展示排序:Sorted/list.sort
'''

import json

def read_user(filepath):
    users = {}
    fhandler = open(filepath, 'r')
    users = json.loads(fhandler.read())
    fhandler.close()
    return users

def auth_login(count = 3):
    is_valid = False
    for i in range(count):
        name = input('请输入用户名:')
        passwd = input('请输入密码:')
        for user in users_data.values():
            if user['name'] == name and user['passwd'] == passwd:
                is_valid = True
                break

        if is_valid:
            return True
        else:
            print('认证失败，请重试')
    return False


def user_add():
    add_data = input('请输入需增加的用户信息(用户名:年龄:联系方式:密码，以英文冒号隔开)：')
    name, age, tel, passwd = add_data.strip().split(':')
    if name not in users_data:
        users_data[name] = {'name': name, 'age': age, 'tel': tel, 'passwd': passwd}
        print('添加用户{}的信息成功'.format(name))
    else:
        print('需添加信息的{}用户已存在'.format(name))

def user_del():
    name = input('请输入需删除信息的用户名：')
    name = name.strip()
    if users_data.pop(name, None):
        print('删除用户{}的信息成功'.format(name))
    else:
        print('待删除信息的{}用户不存在'.format(name))

def user_update():
    update_data = input('请输入需更新的用户信息(用户名:年龄:联系方式:密码，以英文冒号隔开)：')
    name, age, tel, passwd = update_data.strip().split(':')
    if name not in users_data:
        print('需更新信息的{}用户不存在'.format(name))
    else:
        users_data[name] = {'name': name, 'age': age, 'tel': tel, 'passwd': passwd}
        print('更新用户{}的信息成功'.format(name))

def user_find():
    name = input('请输入需要查找信息的用户名：')
    name = name.strip()
    header_exist = False
    for key, value in users_data.items():
        if key.startswith(name):
            if not header_exist:
                print(user_info_header)
                header_exist = True
            print(user_info_tpl.format(value['name'], value['age'], value['tel'], '*' * len(value['passwd'])))
    if not header_exist:
        print('待查找信息的用户{}不存在'.format(name))

def user_list():
    if len(users_data) == 0:
        print('没有用户信息进行展示！')
        return None

    sort_method = input('请输入排序字段[name|age|tel]:')
    if sort_method in ['name', 'age', 'tel']:
        print(user_info_header)
        sorted_user = sorted(list(users_data.values()), key = lambda x:x[sort_method])

        for user in sorted_user:
            print(user_info_tpl.format(user['name'], user['age'], user['tel'], '*' * len(user['passwd'])))
    else:
        print("输入的排序字段格式不正确!")

def user_exit(filepath):
    fhandler = open(filepath, 'w')
    fhandler.write('{}'.format(json.dumps(users_data)))
    fhandler.close()
    print('退出程序！')

path = 'user.txt'
users_data = read_user(path)
user_info_tpl = '|{0:>15}|{1:>5}|{2:>20}|{3:>25}|'
user_info_header = user_info_tpl.format('name','age','tel','passwd')

auth_count = 3

if not auth_login(auth_count):
    print('已超过最大认证次数，退出程序!')
else:
    while True:
        action = input('请输入你的操作(find/list/add/delete/update/exit):')
        if action == 'add':
            user_add()
        elif action == 'delete':
            user_del()
        elif action == 'update':
            user_update()
        elif action == 'find':
            user_find()
        elif action == 'list':
            user_list()
        elif action == 'exit':
            user_exit(path)
            break
        else:
            print('输入的操作不支持，请重新输入！')
