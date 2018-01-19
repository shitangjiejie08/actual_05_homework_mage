# encoding: utf-8

users = {}
users_file = open('users.txt')
for line in users_file:
    name, pwd, age, tel = line.strip().split(':')
    users[name] = {'name': name, 'pwd': pwd, 'age': age, 'tel': tel}
users_file.close()

print('请先输入用户名和密码')
for i in range(3):
    name = input('输入用户名：')
    pwd = input('输入密码：')
    if (name in users) and (pwd == users[name]['pwd']):
        print('验证通过')
        break
    elif i < 2:
        print('验证通过你还有%s次机会' % (2-i))
    else:
        print('验证失败')
        exit()


user_info_tpl = '|{0:^10}|{1:^10}|{2:^10}|{3:^10}|'
user_info_header = user_info_tpl.format('name', 'pwd', 'age', 'telephone')
while True:
    action = input('please input(find/list/add/delete/update/exit):')
    print(action)
    if action == 'add':
        # 增加用户
        user_txt = input('请输入用户信息(用户名:密码:年龄:电话):')
        name, pwd, age, tel = user_txt.split(':')
        if name in users:
            print('添加用户失败，失败原因：用户名已存在')
        else:
            users[name] = {'name': name, 'pwd': pwd, 'age': age, 'tel': tel}
            print('添加用户成功')

    elif action == 'delete':
        # 删除用户
        name = input('请输入你要删除的用户名:')
        isSuc = users.pop(name, False)
        if isSuc:
            print('删除用户成功')
        else:
            print('删除用户失败, 失败原因: 用户名不存在')

    elif action == 'update':
        # 更改用户
        user_txt = input('请输入用户信息(用户名:密码:年龄:电话):')
        name, pwd, age, tel = user_txt.split(':')
        if name in users:
            users.update({name: {'name': name, 'pwd': pwd, 'age': age, 'tel': tel}})
            print('更新用户成功')
        else:
            print('更新用户失败, 错误原因: 用户名不存在')

    elif action == 'find':
        # 查找用户
        name = input('请输入你要查询的用户名:')
        is_exists = False
        for tempName in users:
            if name in tempName:
                is_exists = True
                user = users[tempName]
                print(user_info_tpl.format(user['name'], '*' * len(user['pwd']), user['age'], user['tel']))
        if not is_exists:
            print('没有该用户信息')

    elif action == 'list':
        # 罗列所有用户
        sort_type = input('你可以选择排序方式(name, age, tel)：')
        print(user_info_header)
        if sort_type == 'name':
            names = users.keys()
            names_list = list(names)
            names_list.sort()
            for name in names_list:
                user = users[name]
                print(user_info_tpl.format(user['name'], '*' * len(user['pwd']), user['age'], user['tel']))
        elif sort_type == 'age':
            age_list = []
            for user in users.values():
                age_list.append(user['age'])
            age_list = list(set(age_list))
            age_list.sort()
            for age in age_list:
                for user in users.values():
                    if user['age'] == age:
                        print(user_info_tpl.format(user['name'], '*' * len(user['pwd']), user['age'], user['tel']))
        elif sort_type == 'tel':
            tel_list = []
            for user in users.values():
                tel_list.append(user['tel'])
            tel_list = list(set(tel_list))
            tel_list.sort()
            for tel in tel_list:
                for user in users.values():
                    if user['tel'] == tel:
                        print(user_info_tpl.format(user['name'], '*' * len(user['pwd']), user['age'], user['tel']))
        else:
            for user in users.values():
                print(user_info_tpl.format(user['name'], '*' * len(user['pwd']), user['age'], user['tel']))

    elif action == 'exit':
        # 退出程序
        users_file = open('users.txt', 'w')
        for user in users:
            user_str = '{name}:{pwd}:{age}:{tel}\n'\
                .format(name=user, pwd=users[user]['pwd'], age=users[user]['age'], tel=users[user]['tel'])
            users_file.writelines(user_str)
        users_file.close()
        break
    else:
        print('命令错误')




