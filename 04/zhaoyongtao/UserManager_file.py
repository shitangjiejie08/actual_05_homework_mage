# encoding:utf-8
"""
在用户管理功能中添加密码信息
增、改用户密码
显示时将用户密码显示为N(密码长度)个*
用户验证修改为用户名和密码，只在登录时验证
加分项
输入list后提示用户排序字段（name, age, tel），根据用户输入字段进行排序（升序），然后将结果输出
"""

keys = ('name', 'age', 'tel', 'password')
users = {}
tpl = '|{name:^10}|{age:^5}|{tel:^11}|{password:^20}|'
header = (tpl.format(name=keys[0], age=keys[1], tel=keys[2], password=keys[3]))
mark = False

# 从文件读取用户信息并添加到字典中
with open('users.txt', 'r') as f:
    for line in f:
        if len(line.strip().split(':')) == 4:
            name, age, tel, password = line.strip().split(':')
            users[name] = {'name': name, 'age': age, 'tel': tel, 'password': password}
        else:
            continue

# 验证用户密码
for i in range(3):
    name = input('请输入姓名:')
    password = input('请输入密码:')
    for v in users.values():
        if v['name'] == name and v['password'] == password:
            mark = True
            break
    else:
        print('用户信息验证有误!请重试!')
    if mark:
        break
if mark == False:
    print('已经超过最大认证次数！程序退出...')
else:
    # 验证通过，执行代码
    while True:
        action = input('请输入命令：add/delete/update/find/list/exit\n')
        # add
        if action == 'add':
            user_info = input('请输入用户信息[用户名:年龄:电话:密码]：')
            if len(user_info.strip().split(':')) == 4:
                name, age, tel, password = user_info.strip().split(':')
            else:
                print('请正确输入用户信息！格式：[用户名:年龄:电话:密码]')
                continue
            if name not in users:
                users[name] = {'name': name, 'age': age, 'tel': tel, 'password': password}
                print('添加用户', name, '成功！')
            else:
                print(' 用户', name, '已存在！')

        # list
        elif action == 'list':
            # 根据用户输入排序
            user_list = []
            user_sort = input('请输入要排序的字段：[name/age/tel]\n')

            if user_sort == 'name':
                for user in users.values():
                    tmp = []
                    tmp.append(user['name'])
                    tmp.append(user['age'])
                    tmp.append(user['tel'])
                    tmp.append(user['password'])
                    user_list.append(tmp)

                print(header)
                user_list.sort()  # 默认索引为0处是name
                for i in range(len(user_list)):
                    print(tpl.format(name=user_list[i][0], age=user_list[i][1], tel=user_list[i][2],
                                     password=len(user_list[i][3]) * '*'))

            elif user_sort == 'age':
                for user in users.values():
                    tmp = []
                    tmp.append(user['age'])
                    tmp.append(user['name'])
                    tmp.append(user['tel'])
                    tmp.append(user['password'])
                    user_list.append(tmp)
                    user = list(user.values())  # name与age交换了位置

                print(header)
                user_list.sort()  # 索引为0处是age
                for i in range(len(user_list)):
                    print(tpl.format(name=user_list[i][1], age=user_list[i][0], tel=user_list[i][2],
                                     password=len(user_list[i][3]) * '*'))

            elif user_sort == 'tel':
                for user in users.values():
                    tmp = []
                    tmp.append(user['tel'])
                    tmp.append(user['age'])
                    tmp.append(user['name'])
                    tmp.append(user['password'])
                    user_list.append(tmp)
                    user = list(user.values())  # name与tel交换了位置

                print(header)
                user_list.sort()  # 索引为0处是tel
                for i in range(len(user_list)):
                    print(tpl.format(name=user_list[i][2], age=user_list[i][1], tel=user_list[i][0],
                                     password=len(user_list[i][3]) * '*'))
            else:
                print('输入的排序字段不正确！')

        # find
        elif action == 'find':
            username = input('请输入要查找的用户名：')
            print(header)
            for v in users.values():
                if v['name'].find(username) != -1:
                    print(tpl.format(name=v['name'], age=v['age'], tel=v['tel'], password=len(v['password']) * '*'))
                else:
                    print('用户不存在!')
        # update
        elif action == 'update':
            user_info = input('请输入修改后的用户信息[用户名:年龄:电话:密码]：')
            if len(user_info.strip().split(':')) == 4:
                name, age, tel, password = user_info.strip().split(':')
            else:
                print('请正确输入用户信息！格式：[用户名:年龄:电话:密码]')
                continue
            name, age, tel, password = user_info.strip().split(':')
            if name in users:
                users[name] = {'name': name, 'age': age, 'tel': tel, 'password': password}
                print('修改用户', name, '信息成功！')
            else:
                print(' 用户', name, '不存在！')

        # delete
        elif action == 'delete':
            username = input('请输入要删除的用户名：')
            if users.pop(username, None):
                print('删除', username, '成功！')
            else:
                print('用户', username, '不存在！')

        # exit 将用户信息写入到文件中
        elif action == 'exit':
            with open('users.txt', 'w') as f:
                for user in users.values():
                    f.write(user['name'] + ':' + user['age'] + ':' + user['tel'] + ':' + user['password'] + '\n')
            print('保存用户信息成功，退出...')
            break

        # 其它情况
        else:
            print('命令错误!')

