#!/usr/bin/env python3
# encoding: utf-8

"""
@version: 1.3
@author: huangyisan
@license: Apache Licence
@file: 用户信息.py
@time: 2017/4/16 00:07
"""
import os
current_login_user = ''
count = 3
all_login_user = {}
file_path = os.getcwd()
user_file_name = '/user_db'
login_user_file_name = '/passwd'
while count:
    # 用户登录验证
    enter_username = input('请输入登录用户名 admin : ')
    enter_password = input('请输入密码 0000 : ')
    login_user_file = open(file_path+login_user_file_name, 'r')
    for login_user_line in login_user_file:
        login_user, login_passwd = login_user_line.strip().split(':')
        all_login_user[login_user] = login_passwd
    login_user_file.close()
    # 记得关闭文件句柄
    if all_login_user.get(enter_username) == enter_password:
        print('登录成功!')
        current_login_user = enter_username

        users = {}
        user_info_tpl = '|{0:^20}|{1:^5}|{2:^20}|'
        login_user_info_tpl = '|{0:^20}|{1:^20}|'
        user_info_header = user_info_tpl.format('name', 'age', 'telephone')
        login_user_info_header = login_user_info_tpl.format('name', 'password')
        file_path = os.getcwd()
        # 首先从user_db内读取信息，写入到users这个字典内
        file_user_db = open(file_path+user_file_name, 'rb')
        for line in file_user_db:
            name, age, tel = line.decode().strip().split(':')
            users.update({name: {'Age': age, 'Tel': tel}})
        file_user_db.close()

        while True:
            action = input('Please input  [A]dd  [D]elete  [F]ind  [U]pdate  [L]ist  [O]ption  [E]xit to operate user info ...: ')
            if action.strip() in ['add', 'A']:
                current_passwd = input('请输入当前用户的密码:')
                # 添加用户，当前用户密码验证
                if current_passwd == all_login_user.get(current_login_user):
                    while True:
                        add_info = input('请以"用户名:年龄:联系方式"形式输入添加用户信息，输入back返回上一层: ')
                        if add_info.count(':') != 2 and add_info != 'back':
                            print('输入格式有误')
                        elif add_info == 'back':
                            break
                        else:
                            name, age, tel = add_info.split(':')
                            name = name.strip()
                            if (age.isdigit() or age.strip() == '') and (tel.isdigit() or tel.strip() == ''):
                                if name in users:
                                    print('用户{0}已经存在,如果需要修改{1}，请使用update命令。'.format(name, name))
                                else:
                                    users.update({name: {'Age': age,'Tel': tel}})
                                    print('已经成功添加{0}用户。'.format(name))
                            else:
                                print('请确保输入的"年龄"、"手机"为数字,或为空。')
                else:
                    print('当前认证失败,无权进行添加用户信息操作!')

            elif action.strip() in ['delete', 'D']:
                # 删除用户
                # flag = True
                while True:
                    name = input('请输入你要删除的用户名，多个用户请用","分割，输入back返回上一层: ')
                    if name.strip() == 'back':
                        break
                    else:
                        for del_name in name.split(','):
                            del_name = del_name.strip()
                            if del_name in users:
                                users.pop(del_name)
                                print('删除用户{0}成功'.format(del_name))
                            else:
                                print('该{0}用户不存在'.format(del_name))

            elif action.strip() in ['update', 'U']:
                current_passwd = input('请输入当前用户的密码:')
                if current_passwd == all_login_user.get(current_login_user):
                # 修改用户信息，进行当前用户密码认证
                    print('当前可供修改的用户名如下: ')
                    for exist_name in users.keys():
                        print(exist_name)
                    # flag = True
                    while True:
                        add_info = input('请以”用户名:年龄:联系方式”形式进行用户信息修改，输入back返回上一层: ')
                        if add_info.count(':') != 2 and add_info != 'back':
                            print('输入格式有误')
                        elif add_info == 'back':
                            break
                        else:
                            name, age, tel = add_info.split(':')
                            name = name.strip()
                            if (age.isdigit() or age.strip() == '') and (tel.isdigit() or tel.strip() == ''):
                                if name not in users:
                                    print('用户{0}不存在'.format(name))
                                else:
                                    print('修改之前信息：\nName:{0},Age:{1},Tel:{2}'.format(name, users.get(name)['Age'], users.get(name)['Tel']))
                                    users.update({name: {'Age': age, 'Tel': tel}})
                                    print('修改之后信息：\nName:{0},Age:{1},Tel:{2}'.format(name, users.get(name)['Age'], users.get(name)['Tel']))
                            else:
                                print('请确保输入的"年龄"、"手机"为数字，或为空。')
                else:
                    print('当前认证失败,无权进行修改用户信息操作!')

            elif action.strip() in ['find', 'F']:
                # 查找用户
                name = input('请输入你要查询的用户名:').strip()
                print('{0}查询结果{1}\n{2}\n{3}'.format('*' * 21, '*' * 21, user_info_header, '+' + '-' * 47 + '+'))
                for dict_name in users:
                    if dict_name.find(name) != -1:
                        print(user_info_tpl.format(dict_name, users.get(dict_name)['Age'], users.get(dict_name)['Tel']))
                        print('+' + '-' * 47 + '+')
            elif action.strip() in ['list', 'L']:
                # 罗列所有用户
                while True:
                    sort_info = input('请选择需要排序的方式 [N]ame  [A]ge  [T]elephone 直接回车默认以name方式排序,输入"back"返回上一层:')
                    # name方式排序，因为是key所以可以直接排序，无需考虑重复情况
                    if sort_info.strip() in ['name','N','']:
                        print('{0}用户信息{1}\n{2}\n{3}'.format('*'*21, '*'*21, user_info_header,'+'+'-'*47+'+'))
                        user_list=[]
                        for name in users:
                            user_list.append(name)
                        user_list.sort()
                        for items in user_list:
                            print(user_info_tpl.format(items, users.get(items)['Age'], users.get(items)['Tel']))
                            print('+'+'-'*47+'+')
                    # age方式排序，因为是value，所以可能存在重复情况，需要先set，然后再转换为list进行sort，接着反查先前字典内容，最后打印输出
                    # key的顺序输出。
                    elif sort_info.strip() in ['age','A']:
                        print('{0}用户信息{1}\n{2}\n{3}'.format('*' * 21, '*' * 21, user_info_header, '+' + '-' * 47 + '+'))
                        age_list=[]
                        for name in users:
                            age_list.append(int(users.get(name)['Age']))
                        age_list=sorted(list(set(age_list)))
                        for sorted_age in age_list:
                            for name in users:
                                if users[name]['Age'] == str(sorted_age):
                                    print(user_info_tpl.format(name, users.get(name)['Age'], users.get(name)['Tel']))
                        print('+' + '-' * 47 + '+')
                    # telephone 排序
                    elif sort_info.strip() in ['telephone','T']:
                        print('{0}用户信息{1}\n{2}\n{3}'.format('*' * 21, '*' * 21, user_info_header, '+' + '-' * 47 + '+'))
                        tel_list=[]
                        for name in users:
                            tel_list.append(int(users.get(name)['Tel']))
                        tel_list=sorted(list(set(tel_list)))
                        for sorted_tel in tel_list:
                            for name in users:
                                if users[name]['Tel'] == str(sorted_tel):
                                    print(user_info_tpl.format(name, users.get(name)['Age'], users.get(name)['Tel']))
                        print('+' + '-' * 47 + '+')
                    elif sort_info.strip() == 'back':
                        break
                    else:
                        print('命令错误')

            elif action.strip() in ['option', 'O']:
                # 增删查改可登陆用户信息
                admin_passwd = input('请输入管理员密码:')
                if admin_passwd == all_login_user.get('admin'):
                    while True:
                        option_action = input('Please input [M]odify  [D]elete  [L]ist  [B]ack to operate authentication info ...:')
                        if option_action.strip() in ['back','B']:
                            break
                        elif option_action.strip() in ['modify', 'M']:
                            user_add_info = input('请以"用户:密码"的形式输入添加或修改登陆用户，输入back返回上一层: ')
                            if user_add_info.count(':') != 1 and user_add_info != 'back':
                                print('输入格式有误!')
                            elif user_add_info == 'back':
                                break
                            else:
                                login_name, login_pass = user_add_info.split(':')
                                all_login_user.update({login_name:login_pass})
                                login_user_file = open(file_path + login_user_file_name, 'w')
                                for key in all_login_user:
                                    login_user_file.write('{0}:{1}\n'.format(key, all_login_user[key]))
                                login_user_file.close()
                                print('操作成功!')

                        elif option_action.strip() in ['delete', 'D']:
                            while True:
                                del_user = input('请输入需要删除的登陆账号，输入back返回上一层: ')
                                if del_user == 'admin':
                                    print('无法删除管理员账号')
                                elif del_user == 'back':
                                    break
                                elif del_user not in all_login_user:
                                    print('不存在该登陆账号')
                                else:
                                    del all_login_user[del_user]
                                    login_user_file = open(file_path + login_user_file_name, 'w')
                                    for key in all_login_user:
                                        login_user_file.write('{0}:{1}\n'.format(key,all_login_user[key]))
                                    login_user_file.close()
                                    print('删除成功!')

                        elif option_action.strip() in ['list', 'L']:
                            print('{0}账号信息{1}\n{2}\n{3}'.format('*' * 18, '*' * 18, login_user_info_header, '+' + '-' * 41 + '+'))
                            for key in all_login_user:
                                print('|{0:^20}|'.format(key)+'{0:^20}|'.format('*'*len(str(all_login_user[key]))))
                                print('+' + '-' * 41 + '+')
                        elif option_action.strip() in ['back', 'B']:
                            break
                        else:
                            print('命令错误')

            elif action.strip() in ['exit', 'E']:
                # 退出程序,将缓存中内容写入user_db中。
                file_user_db = open(file_path + user_file_name, 'wb')
                for key, sub_dict in users.items():
                    file_user_db.write('{0}:{1}:{2}\n'.format(key,sub_dict['Age'],sub_dict['Tel']).encode())
                    file_user_db.flush()
                file_user_db.close()
                exit()
            else:
                print('命令错误')
    else:
        print('用户名或密码错误!')
        count -= 1
else:
    print('超过最大尝试次数!')
