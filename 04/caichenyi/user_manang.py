# encoding: utf-8
# Author: Cai Chenyi

'''
在用户管理功能中添加密码信息
增、改添加用户密码输入
显示时将用户密码显示为N(密码长度)个*
用户验证修改为用户名和密码
加分项
输入list后提示用户排序字段（name, age, tel），根据用户输入字段进行排序（升序）后将结果输入
'''

users = {}
user_file = 'users.txt'
try_time = 3
user_info_tpl = '|{0:>20}|{1:>20}|{2:>5}|{3:>20}|'
user_info_header = user_info_tpl.format('name', 'password', 'age', 'tel')

# 读用户文件
with open(user_file, 'rt') as fhandler:
    for line in fhandler:
        name, password, age, tel = line.strip().split(':')
        users[name] = {'name': name, 'password': password, 'age': age, 'tel': tel}

# 用户认证
is_exsit = False
for i in range(try_time):
    name = input('请输入用户名：')
    password = input('请输入{}的密码：'.format(name))
    for user in users.values():
        if name == user['name'] and password == user['password']:
            is_exsit = True
            break
    if is_exsit:
        break
if not is_exsit:
    print('认证超过{}次，退出系统'.format(try_time))
else:
    while True:
        action = input('please input(find/list/add/delete/update/exit):')
        if action == 'add':
            # 增加用户
            user_txt = input('请输入用户信息(用户名:密码:年龄:电话):')
            name, password, age, tel = user_txt.split(':')
            if name in users:
                print('用户存在')
            else:
                users[name] = {'name': name, 'password': password, 'age': age, 'tel': tel}

        elif action == 'delete':
            # 删除用户
            name = input('请输入你要删除的用户名:')
            if users.pop(name, None):
                print('删除成功')
            else:
                print('删除用户失败, 失败原因: 用户名不存在')

        elif action == 'update':
            # 更改用户
            user_txt = input('请输入用户信息(用户名:密码:年龄:电话):')
            name, password, age, tel = user_txt.split(':')
            if name in users:
                users[name] = {'name': name, 'password': password, 'age': age, 'tel': tel}
            else:
                print('更新用户失败, 错误原因: 用户名不存在')

        elif action == 'find':
            # 查找用户
            name = input('请输入你要查询的用户名:')
            is_exists = False
            print(user_info_header)
            for user in users.values():
                if user['name'].find(name) != -1:
                    print(user_info_tpl.format(user['name'], '*' * len(user['password']), user['age'], user['tel']))
                    is_exists = True
            if not is_exists:
                print('没有该用户信息')

        elif action == 'list':
            #罗列所有用户
            list_action = input('请输入排序规则(name,age,tel)：')
            user_list = list(users.values())
            print(user_list)
            for i in range(len(user_list) - 1):
                for j in range(len(user_list) - 1 - i):
                    if user_list[j][list_action] > user_list[j + 1][list_action]:
                        user_list[j], user_list[j + 1] = user_list[j + 1], user_list[j]
            print(user_info_header)
            for user in user_list:
                print(user_info_tpl.format(user['name'], '*' * len(user['password']), user['age'], user['tel']))

        elif action == 'exit':
            # 退出系统
            with open(user_file, 'wt') as fhandler:
                for user in users.values():
                    fhandler.write('{}:{}:{}:{}\n'.format(user['name'], user['password'], user['age'], user['tel']))
            break

        else:
            print('命令错误')