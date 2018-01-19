#encoding: utf-8
#aft 于20170505
'''
用户管理4.0
在用户管理功能中各功能修改为函数
登录验证、添加、修改、查询、列表、删除
用户信息文件读、写
使用json格式存储用户信息
列表展示排序:Sorted/list.sort
'''
import json
import sys
path = 'users.txt'

users = {}
user_tpl = '|{0:>10}|{2:>5}|{3:>11}|{1:>20}|'
user_header= user_tpl.format('name','password' ,'age', 'telephone')

fhandler = open(path, 'rt')
for line in fhandler:
    name,password, age, tel = line.strip().split(':')
    users[name] = {'name' : name,'password':password, 'age' : age, 'tel' : tel}
fhandler.close()

def user_confirm():
    is_valid = False
    #用户认证，最多3次，用户输入用户名和密码
    for i in range(3):
        name = input('请输入用户名:')
        password=input('请输入密码：')
    #认证
        for user in users.values():
            if user['name'] == name and user['password'] == password:
                is_valid = True
                break

        if is_valid:
            break
        else:
            print('认证失败, 请重试')

    if not is_valid:
        print('已超过最大认证次数，程序退出')
    else:
        while True:
            action = input('please input(find/list/add/delete/update/exit):')
def user_add():
        #增加用户
        user_txt = input('请输入用户信息(用户名:密码:年龄:电话 并用英文:分隔开):')
        name, password, age, tel = user_txt.split(':')
        if name in users:
            print('添加用户失败, 失败原因: 用户名已存在')
        else:
             users[name] = {'name' : name, 'password':password, 'age' : age, 'tel' : tel}
def user_delete():
     #删除用户
    name = input('请输入你要删除的用户名:')
    if users.pop(name, None):
        print('删除用户成功')
           
    else:
         print('删除用户失败, 失败原因: 用户名不存在')
def user_update():
    # 更改用户
    user_txt = input('请输入用户信息(用户名:密码:年龄:电话):')
    name, password, age, tel = user_txt.split(':')
    if name in users:
        users[name] = {'name' : name, 'password':password,  'age' : age, 'tel' : tel}
        print('更新用户成功')
    else:
        print('更新用户失败, 错误原因: 用户名不存在')

def user_find():
     # 查找用户
    name = input('请输入你要查询的用户名:')
    is_exists = False
    print(user_header)
    for user in users.values():
        if user['name'].find(name) != -1:
            print(user_tpl.format(user['name'],'*' * len(user['password'],  user['age'], user['tel'])))
    else:
        print('没有该用户信息')
def user_list():
    #罗列所有用户
    field= input('请输入排序规则(name,age,tel)：')
    user_list = list(users.values())
    print(user_list)
    for i in range(len(user_list) - 1):
        for j in range(len(user_list) - 1 - i):
            if user_list[j][list_action] > user_list[j + 1][list_action]:
                user_list[j], user_list[j + 1] = user_list[j + 1], user_list[j]
            print(user_header)
        for user in user_list:
            print(user_tpl.format(user['name'], '*' * len(user['password']), user['age'], user['tel']))
                
def user_exit():
    #退出程序
    fhandler = open(path, 'wt')
    for user in users.values():
        json.dumps(fhandler.write('{0}:{1}:{2}:{3}\n'.format(user['name'], user['password'] ,user['age'], user['tel'])))
    fhandler.close()
    sys.exit('退出程序，欢迎下次再来！')

user_confirm()
while True:
    action = input('请输入你需要的操作(find/dict/add/delete/update/exit): ')
    action = action.strip()
    if action== 'add':
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
        user_exit()

    else:
        print('命令错误,请重新选择！')