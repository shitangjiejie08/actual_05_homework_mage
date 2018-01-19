# encoding:utf-8
'''
让用户输入find,list,add,delete,update,exit
如果add,让用户继续输入用户名，年龄，联系方式，并放入list中，存入之前先检查用户名不重复
若输入delete，让用户输入用户名，根据用户名删除list中数据，若无，则提示不存在
'''

keys = ('name', 'age', 'tel')
users = {}
tpl = '|{name:^10}|{age:^6}|{tel:^11}|'
header = (tpl.format(name=keys[0], age=keys[1], tel=keys[2]))
while True:
    print('\n有效命令：\n-----> list\n-----> find\n-----> add\n-----> update\n-----> delete\n-----> exit\n')
    user_input = input('请输入：')

    # add
    if user_input == 'add':
        user_info = input('请输入用户信息[name:age:tel]：')
        values = tuple(user_info.strip().split(':'))
        user_name, age, tel = values
        if user_name.isalpha() and age.isdigit() and tel.isdigit():
            if user_name not in users:
                user_info_dict = dict(zip(keys, values))
                users.setdefault(user_name, user_info_dict)
                print('添加用户', user_name, '成功！')
            else:
                print(' 用户', user_name, '已存在！')
        else:
            print('用户信息类型错误！')
    # list
    elif user_input == 'list':
        print(header)
        for d in users.values():
            print(tpl.format(name=d['name'], age=d['age'], tel=d['tel']))
    # find
    elif user_input == 'find':
        username = input('请输入要查找的用户名：')
        print(header)
        find_dict = users.get(username, 0)
        if find_dict != 0:
            print(tpl.format(name=find_dict['name'], age=find_dict['age'], tel=find_dict['tel']))
        else:
            print('用户', username, '不存在！')
    # update
    elif user_input == 'update':
        user_info = input('请输入修改后的用户信息[name:age:tel]：')
        values = tuple(user_info.strip().split(':'))
        user_name, age, tel = values
        if user_name.isalpha() and age.isdigit() and tel.isdigit():
            if user_name in users:
                user_info_dict = dict(zip(keys, values))
                users[user_name] = user_info_dict
                print('修改用户', user_name, '信息成功！')
            else:
                print(' 用户', user_name, '不存在！')
        else:
            print('用户信息类型错误！')

    # delete
    elif user_input == 'delete':
        username = input('请输入要删除的用户名：')
        find_dict = users.get(username, 0)
        if find_dict != 0:
            users.pop(username)
            print('删除', username, '成功！')
        else:
            print('用户', username, '不存在！')

    # exit
    elif user_input == 'exit':
        print('退出...')
        break
    else:
        print('输入不合法！')


'''
功能ok，继续坚持，加油
1. line39 保持格式统一，对于引用类型，如果没有尽量使用None标识
2. line19不用转化为tuple有什么影响
3. 查询用户名只要存在查找的字符串就显示
4. 考虑下代码有没有冗余代码，能否简化某些操作
'''
