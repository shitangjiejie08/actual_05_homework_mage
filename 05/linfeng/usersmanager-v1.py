#encoding: utf-8

'''
1. 每一个用户存储信息修改为字典
{name : xxx, age : xxxx, tel: xxx}
2. 用户输入了三次，修改为一次，使用:分隔用户信息
3. 查找的时候使用包含关系，name包含查找的字符串
4.从文件中读取和保存
5.用户认证
6.改用函数
'''
import usermod
import json
path = 'users.txt'
users = {}

'''
输入用户名和密码认证
'''
fhandler = open(path,'rt')
users = json.loads(fhandler.read())
fhandler.close()

rt_value = usermod.auth(users)
if not rt_value:
    print('已超过最大认证次数:')
else:
    while True:
        action = input('please input(find/list/add/delete/update/exit):')
        print(action)
        if action == 'add':
            #增加用户
            usermod.add_user(users)
        elif action == 'delete':
            #删除用户
            usermod.delete_user(users)
        elif action == 'update':
            # 更改用户
            usermod.update_user(users)
        elif action == 'find':
            # 查找用户
            usermod.find_user(users)

        elif action == 'list':
            #罗列所有用户
            usermod.list_user(users)
        elif action == 'exit':
            #退出程序
            fhandler = open(path,'wt')
            content = json.dumps(users)
            fhandler.write(content)
            fhandler.close()
            break
        else:
            print('命令错误')
