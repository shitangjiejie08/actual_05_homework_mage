#!/usr/bin/env python3
# encoding: utf-8

"""
@version: 1.4
@author: huangyisan
@license: Apache Licence
@file: users.py
@time: 2017/4/25 22:07
"""
import os
import json
count = 3
file_path = os.getcwd()
user_file_name = '/user_db'
login_passwd = '/passwd'
user_info_tpl = '|{0:^20}|{1:^5}|{2:^20}|'
login_user_info_tpl = '|{0:^20}|{1:^20}|'
user_info_header = user_info_tpl.format('name', 'age', 'telephone')
login_user_info_header = login_user_info_tpl.format('name', 'password')


def Func_Authen(auth_file_path=file_path, auth_file_name=login_passwd, mode=0):
    '''
    认证函数：
    uri_path 路径
    file_name 认证文本
    mode=0 登陆认证
    mode=1 管理员认证
    mode=2 当前用户认证
    '''
    count = 3
    global current_login_user
    if mode == 0:
        while count:
            # 用户登录验证
            enter_username = input('请输入登录用户名 admin : ')
            enter_password = input('请输入密码 0000 : ')
            Func_User_Info_Write_Read(auth_file_name=login_passwd, mode='ar')
            if all_login_user.get(enter_username) == enter_password:
                print('登录成功!')
                current_login_user = enter_username
                return True
            else:
                print('用户名或密码错误!')
                count -= 1
    elif mode == 1:
        admin_passwd = input('请输入管理员密码:')
        if admin_passwd == all_login_user.get('admin'):
            return True
        else:
            print('管理员密码有误')
    elif mode == 2:
        current_passwd = input('请输入当前用户的密码:')
        # 添加用户，当前用户密码验证
        if current_passwd == all_login_user.get(current_login_user):
            return True
        else:
            print('当前认证失败,无权进行添加用户信息操作!')



def Func_User_Info_Write_Read(auth_file_path=file_path, auth_file_name=user_file_name, mode='nr'):
    global users
    global all_login_user
    # 这两个变量在其他函数中会用到，所以需要global定义变成全局作用域
    if mode == 'nr':
        file_user_db = open(auth_file_path + auth_file_name, 'r')
        users = json.load(file_user_db)
        file_user_db.close()
    elif mode == 'nw':
        file_user_db = open(auth_file_path + auth_file_name, 'w')
        file_user_db.write(json.dumps(users))
        file_user_db.close()
        exit()
    elif mode == 'ar':
        login_user_file = open(auth_file_path + auth_file_name, 'r')
        all_login_user = json.load(login_user_file)
        login_user_file.close()
    elif mode == 'aw':
        login_user_file = open(auth_file_path + auth_file_name, 'w')
        login_user_file.write(json.dumps(all_login_user))
        login_user_file.close()
        print('操作成功!')


def Func_User_Info_Add():
    while True:
        add_info = input('请以"用户名:年龄:联系方式"形式输入添加用户信息，输入back返回上一层: ')
        if add_info.count(':') != 2 and add_info != 'back':
            print('输入格式有误')
        elif add_info == 'back':
            return 0
        else:
            name, age, tel = add_info.split(':')
            name = name.strip()
            if (age.isdigit() or age.strip() == '') and (tel.isdigit() or tel.strip() == ''):
                if name in users:
                    print('用户{0}已经存在,如果需要修改{1}，请使用update命令。'.format(name, name))
                else:
                    users.update({name: {'Age': age, 'Tel': tel}})
                    print('已经成功添加{0}用户。'.format(name))
            else:
                print('请确保输入的"年龄"、"手机"为数字,或为空。')


def Func_User_Info_Del(auth_file_path=file_path, auth_file_name=login_passwd, mode=2):
    if mode == 2:
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
    elif mode == 1:
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
                Func_User_Info_Write_Read(
                    auth_file_name=login_passwd, mode='aw')


def Func_User_Info_Modify(auth_file_path=file_path, auth_file_name=login_passwd, mode=2):
    '''
    mode = 1 修改登陆用户信息
    mode = 2 修改用户信息
    '''
    if mode == 2:
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
                        print('修改之前信息：\nName:{0},Age:{1},Tel:{2}'.format(
                            name, users.get(name)['Age'], users.get(name)['Tel']))
                        users.update({name: {'Age': age, 'Tel': tel}})
                        print('修改之后信息：\nName:{0},Age:{1},Tel:{2}'.format(
                            name, users.get(name)['Age'], users.get(name)['Tel']))
                else:
                    print('请确保输入的"年龄"、"手机"为数字，或为空。')
    elif mode == 1:
        while True:
            user_add_info = input('请以"用户:密码"的形式输入添加或修改登陆用户，输入back返回上一层: ')
            if user_add_info.count(':') != 1 and user_add_info != 'back':
                print('输入格式有误!')
            elif user_add_info == 'back':
                break
            else:
                login_name, login_pass = user_add_info.split(':')
                all_login_user.update({login_name: login_pass})
                Func_User_Info_Write_Read(auth_file_path=file_path,auth_file_name=login_passwd,mode='aw')


def Func_User_Info_Search():
    name = input('请输入你要查询的用户名:').strip()
    print('{0}查询结果{1}\n{2}\n{3}'.format('*' * 21, '*' *
                                        21, user_info_header, '+' + '-' * 47 + '+'))
    for dict_name in users:
        if dict_name.find(name) != -1:
            print(user_info_tpl.format(dict_name, users.get(
                dict_name)['Age'], users.get(dict_name)['Tel']))
            print('+' + '-' * 47 + '+')


def Func_User_Info_Show(mode=2):
    if mode == 2:
        while True:
            sort_info = input(
                '请选择需要排序的方式 [N]ame  [A]ge  [T]elephone 直接回车默认以name方式排序,输入"back"返回上一层:')
            # 使用sorted(xx,key)方式进行排序
            if sort_info.strip() in ['name', 'N', '']:
                print('{0}用户信息{1}\n{2}\n{3}'.format('*' * 21, '*' *
                                                    21, user_info_header, '+' + '-' * 47 + '+'))
                sorted_users=sorted(users.items(),key=lambda x :x[0])
                for items in sorted_users:
                    print(user_info_tpl.format(items[0], users.get(
                        items[0])['Age'], users.get(items[0])['Tel']))
                    print('+' + '-' * 47 + '+')
            elif sort_info.strip() in ['age', 'A']:
                print('{0}用户信息{1}\n{2}\n{3}'.format('*' * 21, '*' *
                                                    21, user_info_header, '+' + '-' * 47 + '+'))
                sorted_age=sorted(users.items(),key=lambda x :int(x[1]['Age']))
                for items in sorted_age:
                    print(user_info_tpl.format(items[0], users.get(
                        items[0])['Age'], users.get(items[0])['Tel']))
                print('+' + '-' * 47 + '+')
            # telephone 排序
            elif sort_info.strip() in ['telephone', 'T']:
                print('{0}用户信息{1}\n{2}\n{3}'.format('*' * 21, '*' *
                                                    21, user_info_header, '+' + '-' * 47 + '+'))
                sorted_tel=sorted(users.items(),key = lambda x :int(x[1]['Tel']))
                for items in sorted_tel:
                    print(user_info_tpl.format(items[0], users.get(
                        items[0])['Age'], users.get(items[0])['Tel']))
                print('+' + '-' * 47 + '+')
            elif sort_info.strip() == 'back':
                break
            else:
                print('命令错误')
    elif mode == 1:
        print('{0}账号信息{1}\n{2}\n{3}'.format('*' * 18, '*' * 18,
                                            login_user_info_header, '+' + '-' * 41 + '+'))
        for key in all_login_user:
            print('|{0:^20}|'.format(key) +
                  '{0:^20}|'.format('*' * len(str(all_login_user[key]))))
            print('+' + '-' * 41 + '+')


def Func_System_Option():
    if Func_Authen(mode=1):
        while True:
            option_action = input(
                'Please input [M]odify  [D]elete  [L]ist  [B]ack to operate authentication info ...:')
            if option_action.strip() in ['back', 'B']:
                break
            elif option_action.strip() in ['modify', 'M']:
                Func_User_Info_Modify(mode=1)
            elif option_action.strip() in ['delete', 'D']:
                Func_User_Info_Del(mode=1)
            elif option_action.strip() in ['list', 'L']:
                Func_User_Info_Show(mode=1)
            elif option_action.strip() in ['back', 'B']:
                break


Func_User_Info_Write_Read(mode='nr')
Func_User_Info_Write_Read(auth_file_path=file_path,auth_file_name=login_passwd,mode='ar')
if Func_Authen():
    while True:
        action = input(
            'Please input  [A]dd  [D]elete  [F]ind  [U]pdate  [L]ist  [O]ption  [E]xit to operate user info ...: ')
        if action.strip() in ['add', 'A']:
            # 添加用户
            if Func_Authen(mode=2):
                Func_User_Info_Add()
        elif action.strip() in ['delete', 'D']:
            # 删除用户
            Func_User_Info_Del()
        elif action.strip() in ['update', 'U']:
            # 更新用户
            if Func_Authen(mode=2):
                Func_User_Info_Modify()
        elif action.strip() in ['find', 'F']:
            # 查询用户
            Func_User_Info_Search()
        elif action.strip() in ['list', 'L']:
            # 列出用户
            Func_User_Info_Show()
        elif action.strip() in ['option', 'O']:
            # 系统设置
            Func_System_Option()
        elif action.strip() in ['exit', 'E']:
            # 退出程序,将缓存中内容写入user_db中。
            Func_User_Info_Write_Read(mode='nw')
            exit()
        else:
            print('命令错误')
