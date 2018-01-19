#!/usr/bin/env python3
# encoding: utf-8

"""
@version: 1.0
@author: huangyisan
@license: Apache Licence
@file: 用户信息.py
@time: 2017/4/12 22:07
"""

users = {'yisan': {'Age': '27', 'Tel': '1876666666'}, 'kk': {'Age': '29', 'Tel': '1888888888'}}
user_info_tpl = '|{0:^20}|{1:^5}|{2:^20}|'
user_info_header = user_info_tpl.format('name', 'age', 'telephone')
while True:
    action = input('Please input  [A]dd  [D]elete  [F]ind  [U]pdate  [L]ist  [E]xit to continue...): ')
    if action.strip() in ['add', 'A']:
        # flag=True
        while True:
            add_info = input('请以”用户名:年龄:联系方式”形式输入添加用户信息，输入back返回上一层: ')
            if add_info.count(':') != 2 and add_info != 'back':
                print('输入格式有误')
            elif add_info == 'back':
                break
            else:
                name = add_info.split(':')[0].strip()
                age = add_info.split(':')[1]
                tel = add_info.split(':')[2]
                if (age.isdigit() or age.strip() == '') and (tel.isdigit() or tel.strip() == ''):
                    if name in users:
                        print('用户{0}已经存在,如果需要修改{1}，请使用update命令。'.format(name, name))
                    else:
                        users.update({name: {'Age': age,'Tel': tel}})
                        print('已经成功添加{0}用户。'.format(name))
                else:
                    print('请确保输入的"年龄"、"手机"为数字,或为空。')

    elif action.strip() in ['delete', 'D']:
        # 删除用户
        # flag = True
        while True:
            name = input('请输入你要删除的用户名，多个用户请用","分割，输入back返回上一层: ')
            if name.strip() == 'back':
                break
            else:
                for del_name in list(name.split(',')):
                    del_name = del_name.strip()
                    if del_name in users:
                        users.pop(del_name)
                        print('删除用户{0}成功'.format(del_name))
                    else:
                        print('该{0}用户不存在'.format(del_name))

    elif action.strip() in ['update', 'U']:
        # 修改用户信息
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
                name = add_info.split(':')[0].strip()
                age = add_info.split(':')[1]
                tel = add_info.split(':')[2]
                if (age.isdigit() or age.strip() == '') and (tel.isdigit() or tel.strip() == ''):
                    if name not in users:
                        print('用户{0}不存在'.format(name))
                    else:
                        print('修改之前信息：\nName:{0},Age:{1},Tel:{2}'.format(name, users.get(name)['Age'], users.get(name)['Tel']))
                        users.update({name: {'Age': age, 'Tel': tel}})
                        print('修改之后信息：\nName:{0},Age:{1},Tel:{2}'.format(name, users.get(name)['Age'], users.get(name)['Tel']))
                else:
                    print('请确保输入的"年龄"、"手机"为数字，或为空。')

    elif action.strip() in ['find', 'F']:
        # 查找用户
        name = input('请输入你要查询的用户名:').strip()
        if name in users:
            print('{0}查询结果{1}\n{2}\n{3}'.format('*'*21,'*'*21, user_info_header,'+'+'-'*47+'+'))
            print(user_info_tpl.format(name, users.get(name)['Age'], users.get(name)['Tel']))
            print('+'+'-'*47+'+')
        # 想用get(name,default)省去else,但若触发default暂时没想到如何解决后续格式化输出的问题。
        else:
            print('用户{0}不存在'.format(name))

    elif action.strip() in ['list', 'L']:
        # 罗列所有用户
        print('{0}用户信息{1}\n{2}\n{3}'.format('*'*21, '*'*21, user_info_header,'+'+'-'*47+'+'))
        for name in users:
            print(user_info_tpl.format(name, users.get(name)['Age'], users.get(name)['Tel']))
            print('+'+'-'*47+'+')

    elif action.strip() in ['exit', 'E']:
        # 退出程序
        break
    else:
        print('命令错误')



'''
功能ok, 继续坚持，加油
1. line46 需要使用list吗
2. 考虑下find，如果想查找名字中包含搜索字母的所有舒勇信息如何完成
3. 练习list赋值给多个变量如何使用
'''
