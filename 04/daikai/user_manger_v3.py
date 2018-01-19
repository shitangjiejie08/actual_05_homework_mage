#encoding:utf-8

'''
用户管理v3.0
Author:daikai

在用户管理功能中添加密码信息
增、改添加用户密码输入
显示时将用户密码显示为N(密码长度)个*
用户验证修改为用户名和密码
加分项
输入list后提示用户排序字段（name, age, tel），根据用户输入字段进行排序（升序）后将结果输入
'''

info_path = 'user.info'
auth_count = 3

users_data = {}
user_info_tpl = '|{0:>15}|{1:>5}|{2:>20}|{3:>25}|'
user_info_header = user_info_tpl.format('name','age','tel','passwd')
value_keys = ('name','age','tel','passwd')

fhandler = open(info_path, 'rt')
for line in fhandler:
    name, age, tel, passwd = line.strip().split(':')
    users_data[name] = {'name':name,'age':age,'tel':tel,'passwd':passwd}
fhandler.close()

is_valid = False
#使用用户名和密码进行认证，最多尝试3次
for i in range(auth_count):
    name = input('请输入用户名:')
    passwd = input('请输入密码:')
    for user in users_data.values():
        if user['name'] == name and user['passwd'] == passwd:
            is_valid = True
            break

    if is_valid:
        break
    else:
        print('认证失败，请重试')

if not is_valid:
    print('已超过最大认证次数，退出程序!')
else:
    while True:
        action = input('请输入你的操作(find/list/add/delete/update/exit):')
        action = action.strip()
        if action == 'add':
            add_data = input('请输入需增加的用户信息(格式为用户名:年龄:联系方式:密码，以英文冒号隔开)：')
            add_data_dict = dict(zip(value_keys,add_data.strip().split(':')))
            user_name = add_data_dict.get('name')
            if user_name not in users_data:
                users_data[user_name] = add_data_dict
                print('添加用户{}的信息成功'.format(user_name))
            else:
                print('需添加信息的{}用户已存在'.format(user_name))
        elif action == 'delete':
            delete_name = input('请输入需删除信息的用户名：')
            delete_name = delete_name.strip()
            if users_data.pop(delete_name,None):
                print('删除用户{}的信息成功'.format(delete_name))
            else:
                print('待删除信息的{}用户不存在'.format(delete_name))
        elif action == 'update':
            user_update = input('请输入需更新的用户信息(格式为用户名:年龄:联系方式:密码，以英文冒号隔开)：')
            update_dict = dict(zip(value_keys,user_update.strip().split(':')))
            user_name = update_dict.get('name')
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
                #if key.find(find_name) != -1 and key.index(find_name) == 0:
                if key.startswith(find_name):
                    if not header_exist:
                        print(user_info_header)
                        header_exist = True
                    print(user_info_tpl.format(value['name'],value['age'],value['tel'],'*'*len(value['passwd'])))
            if not header_exist:
                print('待查找信息的用户{}不存在'.format(find_name))
        elif action == 'list':
            if len(users_data) == 0:
                print('没有用户信息进行展示！')
                continue
            sort_method = input('请输入排序字段[name|age|tel]:')
            if sort_method == 'name':
                print(user_info_header)
                name_list = list(users_data.keys())
                name_list.sort()
                for name in name_list:
                    print(user_info_tpl.format(users_data[name]['name'],
                                               users_data[name]['age'],
                                               users_data[name]['tel'],
                                               '*'*len(users_data[name]['passwd'])))
            elif sort_method == 'age':
                print(user_info_header)
                user_list = list(users_data.values())
                for i in range(1, len(user_list)):
                    for j in range(i, 0, -1):
                        if user_list[j - 1]['age'] > user_list[j]['age']:
                            user_list[j - 1], user_list[j] = user_list[j], user_list[j - 1]
                        else:
                            break

                for user in user_list:
                    print(user_info_tpl.format(user['name'],
                                               user['age'],
                                               user['tel'],
                                               '*'*len(user['passwd'])))
            elif sort_method == 'tel':
                print(user_info_header)
                user_list = list(users_data.values())
                for i in range(1, len(user_list)):
                    for j in range(i, 0, -1):
                        if user_list[j - 1]['tel'] > user_list[j]['tel']:
                            user_list[j - 1], user_list[j] = user_list[j], user_list[j - 1]
                        else:
                            break

                for user in user_list:
                    print(user_info_tpl.format(user['name'],
                                               user['age'],
                                               user['tel'],
                                               '*' * len(user['passwd'])))
            else:
                print("输入的排序字段格式不正确!")
        elif action == 'exit':
            fhandler = open(info_path,'wt')
            for user in users_data.values():
                fhandler.write('{}:{}:{}:{}\n'.format(user['name'],user['age'],user['tel'],user['passwd']))
            fhandler.close()
            print('退出程序！')
            break
        else:
            print('输入的操作不支持，请重新输入！')