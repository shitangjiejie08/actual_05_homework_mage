#encoding:utf-8

'''
用户管理v2.0
Author:daikai

1、让用户在控制台上输入”find/list/add/delete/update/exit”格式字符串
2、如果输入add，则让用户继续输入”用户名:年龄:联系方式”格式字符串，去除前后空字符，并使用:分隔用户数据，将用户数据放入dict中存储，
   用户名作为key，value使用{name: 用户名, age: 年龄，tel:联系方式}，在放入dict之前检查用户名不重复，如果重复，则提示用户已存在
3、如果输入delete，则让用户输入”用户名”格式字符串，根据用户名查找dict中数据，若存在数据则将该数据移除，若用户数据不存在，则提示不存在
4、如果输入update，则让用户输入”用户名:年龄:联系方式”格式字符串，并使用:分隔用户数据，根据用户名查找dict中数据，
   若存在数据则将改数据更新数据，若用户数据不存在，则提示不存在
5、如果用户输入find，则让用户输入”用户名”格式字符串，根据用户名查找dict中数据包含输入字符串的用户信息，并打印
6、如果用户输入list，则打印所有用户信息，打印用户第一个行数据为用户信息描述，从第二行开始为用户数据
7、如果用户输入exit，则打印退出程序，并退出
'''

users_data = {}
user_info_tpl = '|{0:>15}|{1:>5}|{2:>20}|'
user_info_header = user_info_tpl.format('name','age','tel')
value_keys = ('name','age','tel')

while True:
    action = input('请输入你的操作(find/list/add/delete/update/exit):')
    action = action.strip()
    if action == 'add':
        add_data = input('请输入需增加的用户信息(格式为用户名:年龄:联系方式，以英文冒号隔开)：')
        add_data_list = add_data.strip().split(':')
        user_name = add_data_list[0]
        add_data_dict = dict(zip(value_keys,add_data_list))
        if user_name not in users_data:
            users_data[user_name] = add_data_dict
            print('添加用户{}的信息成功'.format(user_name))
        else:
            print('需添加信息的{}用户已存在'.format(user_name))
    elif action == 'delete':
        delete_name = input('请输入需删除信息的用户名：')
        delete_name = delete_name.strip()
        if delete_name not in users_data:
            print('待删除信息的{}用户不存在'.format(delete_name))
        else:
            delete_data = users_data.pop(delete_name)
            print('删除用户{}的信息成功'.format(delete_name))
    elif action == 'update':
        user_update = input('请输入需更新的用户信息(格式为用户名:年龄:联系方式，以英文冒号隔开)：')
        update_list = user_update.strip().split(':')
        user_name = update_list[0]
        update_dict = dict(zip(value_keys,update_list))
        if user_name not in users_data:
            print('需更新信息的{}用户不存在'.format(user_name))
        else:
            users_data[user_name] = update_dict
            print('更新用户{}的信息成功'.format(user_name))
    elif action == 'find':
        find_name = input('请输入需要查找信息的用户名：')
        find_name = find_name.strip()
        header_exist = False
        for key,value in users_data.items():
            if key.find(find_name) != -1 and key.index(find_name) == 0:
                if not header_exist:
                    print(user_info_header)
                    header_exist = True
                print(user_info_tpl.format(value['name'],value['age'],value['tel']))
        if not header_exist:
            print('待查找信息的用户{}不存在'.format(find_name))
    elif action == 'list':
        if len(users_data) == 0:
            print('没有用户信息进行展示！')
            continue
        print(user_info_header)
        for value in users_data.values():
            print(user_info_tpl.format(value['name'],value['age'],value['tel']))
    elif action == 'exit':
        print('退出程序！')
        break
    else:
        print('输入的操作不支持，请重新输入！')


'''
功能ok，非常棒 继续坚持，加油
1. line59，理解是想以查找字符开头的所有信息，考虑只用find如何完成
'''
