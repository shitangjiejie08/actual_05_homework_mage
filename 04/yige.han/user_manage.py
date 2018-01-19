# _*_ coding: utf-8 _*_
import os
"""
人员管理 增删改查
"""

users_db = "users.db"
users = {}
# users = {'hug': {'age': 12, 'name': 'hug', 'tel': 13, 'password': '123456'}, 'had': {'age': 1, 'name': 'had', 'tel': 2, 'password': '123456'}}
user_info_split = '- ' * 40
user_info_tpl = '|{name:20} |{age:20} |{tel:20}|{password:20}'
user_info_tpl_format = user_info_tpl.format(name='name', age='age', tel='tel', password='password')

# 从文件读取用户信息
if os.path.isfile(users_db):
    with open(users_db, 'rt') as f:
        for line in f:
            user = line.strip().split(':')
            if len(user) > 3:
                users[user[0]] = {'name': user[0], 'age': int(user[1]), 'tel': int(user[2]), 'password': user[3]}

# 认证用户
is_auth = False
auth_times = 3
while auth_times > 0:
    name_auth = input("name>>")
    password = input("password>>")

    for user in users.values():
        if user['name'] == name_auth and user['password'] == password:
            is_auth = True
    if is_auth:
        print("认证通过!")
        break
    else:
        auth_times -= 1
        print("认证失败,请重试,还剩{}次".format(auth_times))

# 认证通过, 操作数据.
if is_auth:
    while True:
        action = input("find/list/add/delete/update/exit:")
        if action == "add":
            input_user = input("name:age:tel:password >>")
            user = input_user.strip().split(':')
            if len(user) == 4:
                name, age, tel, password = user
            else:
                print("数据格式错误,请重新输入！")
                continue
            if name in users:
                print("同名用户[{}]已存在: ".format(name))
                user = users[name]
                print(user_info_tpl_format)
                print(user_info_split)
                print(user_info_tpl.format(name=user['name'], age=user['age'], tel=user['tel'], password='*'*len(user['password'])))
            else:
                users[name] = {'name': name, 'age': int(age), 'tel': int(tel), 'password': password}

        elif action == "delete":
            name = input("delete user name:")
            if name in users:
                users.pop(name)
                print("删除用户{{{}}}成功".format(name))
            else:
                print("用户不存!")

        elif action == "update":
            input_user = input("name:age:tel:password>>")
            user = input_user.strip().split(':')
            if len(user) == 4:
                name, age, tel, password = user
                if name in users:
                    users[name] = {'name': name, 'age': int(age), 'tel': int(tel), 'password': password}
                    print("用户{{{}}}更新成功".format(name))
                else:
                    print("用户不存在!")
            else:
                print("数据格式有误,请重新输入!")

        elif action == "find":
            is_find = False
            find_users = []
            find_name = input("find name:")
            for name in users.keys():
                if name.find(find_name) != -1:
                    if not is_find:
                        print(user_info_tpl_format)
                        print(user_info_split)
                        is_find = True
                    user = users[name]
                    print(user_info_tpl.format(name=user['name'], age=user['age'], tel=user['tel'], password='*'*len(user['password'])))
            if not is_find:
                print("未找到任何相关用户")

        elif action == "list":
            while True:
                sort_row = input("请输入需要排序的列name or age or tel>>")
                if sort_row in ['name', 'age', 'tel']:
                    break
                else:
                    print("输入的排序列名不正确!")
            print(user_info_tpl_format)
            print(user_info_split)
            sort_users = sorted(users.values(), key=lambda u: u[sort_row])
            for user in sort_users:
                print(user_info_tpl.format(name=user['name'], age=user['age'], tel=user['tel'], password='*'*len(user['password'])))
        elif action == "exit":
            with open(users_db, 'wt') as f:
                for user in users.values():
                    f.write("{}:{}:{}:{}\n".format(user['name'], user['age'], user['tel'], user['password']))

            print("数据保存成功,正常退出!")
            break
        else:
            print("指令输入错误,请输入正确的指令!")
