# encoding:utf-8
"""
在用户管理功能中各功能修改为函数
登录验证、添加、修改、查询、列表、删除
用户信息文件读、写
使用json格式存储用户信息
列表展示排序:Sorted/list.sort
"""
import json
keys = ('name', 'age', 'tel', 'password')
users = {}
tpl = '|{name:^10}|{age:^5}|{tel:^11}|{password:^20}|'
header = (tpl.format(name=keys[0], age=keys[1], tel=keys[2], password=keys[3]))

def read_user(filepath, mode):
    # 从文件读取用户信息并添加到字典中
    f = open(filepath, mode)
    for line in f:
        line = json.loads(line)
        line =line.strip().split(':')
        name, age, tel, password = line
        users[name] = {'name': name, 'age': age, 'tel': tel, 'password': password}
    f.close()

def user_auth(count, mark=False):
    '''
    根据用户名、密码、次数验证
    '''
    for i in range(count):
        name = input('请输入姓名:')
        password = input('请输入密码:')
        for v in users.values():
            if v['name'] == name and v['password'] == password:
                mark = True
                break
        if mark == True:
            break
        else:
            print('用户信息验证有误!请重试!')
    return mark

def add_user(user_info):
    '''
    添加用户
    '''
    if len(user_info.strip().split(':')) == 4:
        name, age, tel, password = user_info.strip().split(':')
    else:
        print('请正确输入用户信息！格式：[用户名:年龄:电话:密码]')
    if name not in users:
        users[name] = {'name': name, 'age': age, 'tel': tel, 'password': password}
        print('添加用户', name, '成功！')
    else:
        print(' 用户', name, '已存在！')

def delete_user(name):
    '''
    删除用户，参数为用户名
    '''
    if users.pop(username, None):
        print('删除', username, '成功！')
    else:
        print('用户', username, '不存在！')

def user_list(k):
    '''
    用户排序及查找
    '''
    user_list = list(users.values())
    if k in ['name', 'age', 'tel']:
        result_list = sorted(user_list, key=lambda x: x[k])
        print(header)
        for user in result_list:
            print(tpl.format(name=user['name'], age=user['age'], tel=user['tel'], password='*' * len(user['password'])))
    else:
        print('排序列错误！')

def user_find(name):
    '''
    根据用户名查找用户
    '''
    print(header)
    mark = False
    for user in users.values():
        if user['name'].find(name) != -1:
            print(tpl.format(name=user['name'], age=user['age'], tel=user['tel'],password = user['password']))
            mark = True
    if mark == False:
        print('用户', name, '不存在！')

def user_update(user_info):
    '''
    用户信息修改
    '''
    if len(user_info.strip().split(':')) == 4:
        name, age, tel, password = user_info.strip().split(':')
    else:
        print('请正确输入用户信息！格式：[用户名:年龄:电话:密码]')

    name, age, tel, password = user_info.strip().split(':')
    if name in users:
        users[name] = {'name': name, 'age': age, 'tel': tel, 'password': password}
        print('修改用户', name, '信息成功！')
    else:
        print(' 用户', name, '不存在！')

def user_exit(filepath, mode):
    '''
    退出并写入到json文件中
    '''
    f = open(filepath, mode)
    for user in users.values():
        info = user['name'] + ':' + user['age'] + ':' + user['tel'] + ':' + user['password']
        json_info = json.dumps(info)
        f.write(json_info+'\n')
    print('保存用户信息成功，退出...')
    f.close()

# read users
read_user('users.json', 'rt')
print('--->用户读取完成<---')
# user auth
mark = user_auth(3)
if mark == False:
    print('用户认证失败！退出...')
else:
    # 验证通过，执行代码
    while True:
        action = input('请输入命令：add/delete/update/find/list/exit\n')
        # add
        if action == 'add':
            user_info = input('请输入用户信息[用户名:年龄:电话:密码]：')
            add_user(user_info)

        # list
        elif action == 'list':
            key = input('请输入排序的列(name, age, tel):')
            user_list(key)

        # find
        elif action == 'find':
            username = input('请输入要查找的用户名：')
            user_find(username)

        # update
        elif action == 'update':
            user_info = input('请输入修改后的用户信息[用户名:年龄:电话:密码]：')
            user_update(user_info)

        # delete
        elif action == 'delete':
            username = input('请输入要删除的用户名：')
            delete_user(username)

        # exit 将用户信息写入到json中
        elif action == 'exit':
            user_exit('users.json', 'wt')
            break

        # 其它情况
        else:
            print('命令错误!')

