# encoding: utf-8

'''
1. 每一个用户存储信息修改为字典
{name : xxx, age : xxxx, tel: xxx}
2. 用户输入了三次，修改为一次，使用:分隔用户信息
3. 查找的时候使用包含关系，name包含查找的字符串
4. 显示的时候用*表示
5. 添加密码信息
'''
users = {}
fhandler = open('user_info.txt')
for line in fhandler:
    name, age, tel, pw = line.strip().split(':')
    users[name] = {'name': name, 'age': age, 'tel': tel, 'pw': pw}
fhandler.close()
user_info_tpl = '|{0:>20}|{1:>5}|{2:>20}|{3:>20}|'
user_info_header = user_info_tpl.format('name', 'age', 'telephone', 'password')
is_bool = False
for i in range(3):
    name = input('Please input your name:')
    pw = input('Please input your password:')
    for user in users.values():
        if name == user['name'] and pw == user['pw']:
            print('用户认证成功！')
            is_bool = True
            break
    if is_bool:
        break
    else:
        print('认证失败！')
if not is_bool:
    print('超过最大认证次数！')
while True:
    action = input('please input(find/list/add/delete/update/exit):')
    print(action)
    if action == 'add':
        # 增加用户
        user_txt = input('请输入用户信息(用户名:年龄:电话:密码):')
        name, age, tel, pw = user_txt.split(':')
        is_exists = False
        if name in users:
            print('用户已存在')
        else:
            users[name] = {'name': name, 'age': age, 'tel': tel, 'pw': pw}
        # print(users)

    elif action == 'delete':
        # 删除用户
        name = input('请输入你要删除的用户名:')
        is_exists = False
        if users.pop(name, None):
            print('删除用户成功')
        else:
            print('用户不存在，删除失败')
        # print(users)
    elif action == 'update':
        # 更改用户
        user_txt = input('请输入用户信息(用户名:年龄:电话:密码):')
        name, age, tel = user_txt.split(':')
        is_exists = False
        for user in users:
            if name == user['name']:
                users.remove(user)
                is_exists = True
                break

        if is_exists:
            users.append({'name': name, 'age': age, 'tel': tel, 'pw': pw})
            print('更新用户成功')
            # print(users)
        else:
            print('更新用户失败, 错误原因: 用户名不存在')
    elif action == 'find':
        # 查找用户
        name = input('请输入你要查询的用户名:')
        is_exists = False
        print(user_info_header)
        for user in users:
            if user['name'].find(name) != -1:
                print(user_info_tpl.format(user['name'], user['age'], user['tel'], user['pw']))
                is_exists = True

        if not is_exists:
            print('没有该用户信息')

    elif action == 'list':
        # 罗列所有用户
        print(user_info_header)
        for user in users.values():
            print(user_info_tpl.format(user['name'], user[
                  'age'], user['tel'], '*' * len(user['pw'])))
        in_fo = input('请输入name，age，tel中的一个进行排序:')
        if in_fo == 'name':
            names = []
            for name in users:
                names.append(name)
            names.sort()
            for i in names:
                print(user_info_tpl.format(users[i]['name'], users[i][
                          'age'], users[i]['tel'], '*' * len(users[i]['pw'])))
        if in_fo == 'age':
            ages = []
            for user in users.values():
                ages.append(user['age'])
            ages = list(set(ages))
            ages.sort()
            for i in ages:
                for user in users.values():
                    if i == user['age']:
                        print(user_info_tpl.format(user['name'], user[
                              'age'], user['tel'], '*' * len(user['pw'])))
        if in_fo == 'tel':
            ages = []
            for user in users.values():
                ages.append(user['tel'])
            ages = list(set(ages))
            ages.sort()
            for i in ages:
                for user in users.values():
                    if i == user['tel']:
                        print(user_info_tpl.format(user['name'], user[
                              'age'], user['tel'], '*' * len(user['pw'])))

    elif action == 'exit':
        fhandler = open('user_info.txt', 'wt')
        for user in users.values():
            fhandler.write('{}:{}:{}:{}\n'.format(
                user['name'], user['age'], user['tel'], user['pw']))
        #    name, age, tel = user.values()
        #    fhandler.writelines([name, age, tel, '\n'])
        fhandler.close()
        # 退出程序
        break
    else:
        print('命令错误')
