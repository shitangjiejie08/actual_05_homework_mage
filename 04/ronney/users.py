#encoding: utf-8

'''
1. 每一个用户存储信息修改为字典
{name : xxx, age : xxxx, tel: xxx}
2. 用户输入了三次，修改为一次，使用:分隔用户信息
3. 查找的时候使用包含关系，name包含查找的字符串
'''
import os

users = {}
user_info_tpl = '|{name:^20}|{age:^5}|{tel:>20}| {password:>20}|'
user_info_header = user_info_tpl.format(name='name',age= 'age', tel='tel',password='password')


if os.path.isfile('users_db.txt'):
    with open('users_db.txt') as f:
        for line in f:
            name,age,tel,password = line.strip().split(':')
            users[name] = {'name':name,'age':age,'tel':tel,'password':password}
is_valid = False
for i in range(3):
    print("用户认证")
    name = input('请输入用户名：')
    password = input('密码：')
    for user in users.values():
        if user['name'] == name and user['password'] == password:
            is_valid = True
    if is_valid:
        print('认证成功')
        break
    else:
        print('认证失败，请重试')
if not is_valid:
    print('已超过最大认证次数，程序退出')
else:
    while True:
        action = input('please input(find/list/add/delete/update/exit):')
        print(action)
        if action == 'add':
            #增加用户
            user_txt = input('请输入用户信息(用户名:年龄:电话:密码):')
            user = user_txt.split(':')
            if len(user) == 4:
                name,age,tel,password = user
            else:
                print('你输入的格式有误，请重新输入')
                continue
            if name in users:
                print('添加用户失败, 失败原因: 用户名已存在')
            else:

                users[name] = {'name':name,'age':age,'tel':tel,'password':password}
        elif action == 'delete':            #删除用户
            name = input('请输入要删除的用户名：')
            if users.pop(name,None):
                print('删除用户成功')
            else:
                print('用户名不存在，删除失败')
        elif action == 'update':
            # 更改用户
            user_txt = input('请输入用户信息(用户名:年龄:电话:密码):')
            user = user_txt.split(':')
            if len(user) == 4:
                name,age,tel,password = user
                if name in users:
                    users[name] = {'name':name,'age':age,'tel':tel,'password':password}
                    print("用户%s更新成功" % name)
                else:
                    print('更新用户失败, 错误原因: 用户名不存在')
            else:
                print('你输入的数据格式有误，请重新输入')
                continue
        elif action == 'find':
            # 查找用户
            name = input('请输入你要查询的用户名:')
            is_exists = False
            print(user_info_header)
            for user in users.values():
                if user['name'].find(name) != -1:
                    print(user_info_tpl.format(name= user['name'],age= user['age'],tel= user['tel'],passwd=user['password']))
                    is_exists = True

            if not is_exists:
                print('没有该用户信息')

        elif action == 'list':
            #罗列所有用户
            print(user_info_header)
            for user in users.values():
                print(user_info_tpl.format(name=user['name'], age=user['age'],tel= user['tel'],password='*' * len(user['password'])))

        elif action == 'exit':
            fw = open('users_db.txt','w')
            for user in users.values():
                fw.write('{0}:{1}:{2}:{3}\n'.format(user['name'],user['age'],user['tel'],user['password']))
            print(users)
            fw.close()
            #退出程序
            break
        else:
            print('命令错误')
