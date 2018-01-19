#encoding: utf-8

'''
1. 每一个用户存储信息修改为字典
{name : xxx, age : xxxx, tel: xxx}
2. 用户输入了三次，修改为一次，使用:分隔用户信息
3. 查找的时候使用包含关系，name包含查找的字符串
4.从文件中读取和保存
5.用户认证
'''
user_info_tpl = '|{0:>20}|{1:>5}|{2:>20}|{3:>20}|'
user_info_header = user_info_tpl.format('name', 'age', 'telephone','passwd')
users = {}
path = 'users.txt'
fhandler = open(path,'rt')
for line in fhandler:
    name, age, tel, passwd = line.strip().split(':')
    users[name] = {'name':name,'age':age,'tel':tel,'passwd':passwd}
fhandler.close()
'''
输入用户名和密码认证
'''
print('请输入用户名和密码验证:')
is_valid = False
for i in range(3):
    name = input('请输入用户名:')
    passwd = input('请输电话号码:')
    for user in users.values():
        if (user['name'] == name and user['passwd'] == passwd):
            is_valid = True
            break
    if is_valid:
        break
    else:
        print('认证失败')
if not is_valid:
    print('已超过最大认证次数:')
else:
    while True:
        action = input('please input(find/list/add/delete/update/exit):')
        print(action)
        if action == 'add':
            #增加用户
            user_txt = input('请输入用户信息(用户名:年龄:电话:密码):')
            name, age, tel, passwd = user_txt.split(':')
            if name in users:
                print('添加用户失败, 失败原因: 用户名已存在')
            elif  passwd.isdigit() == False:
                print('密码需为纯数字')
                break
            else :
                users[name] = {'name' : name, 'age' : age, 'tel' : tel,'passwd':passwd}
                print('添加用户成功')

        elif action == 'delete':
            #删除用户
            name = input('请输入你要删除的用户名:')
            if name in users:
                del users[name]
                print('删除用户成功')
            else:
                print('删除用户失败, 失败原因: 用户名不存在')
        elif action == 'update':
            # 更改用户
            user_txt = input('请输入用户信息(用户名:年龄:电话:密码):')
            name, age, tel, passwd = user_txt.split(':')
            if name in users:
                users[name] = {'name' : name, 'age' : age, 'tel' : tel,'passwd':passwd}
                print('更新用户成功')
            else:
                print('更新用户失败, 错误原因: 用户名不存在')
        elif action == 'find':
            # 查找用户
            name = input('请输入你要查询的用户名:')
            is_exists = False
            print(user_info_header)
            for user in users.values():
                if user['name'].find(name) != -1:
                    print(user_info_tpl.format(user['name'], user['age'], user['tel'],'******'))
                    is_exists = True

            if not is_exists:
                print('没有该用户信息')

        elif action == 'list':
            #罗列所有用户
            sort_field = input('请输入结果显示排序字段name/age/tel: ')
            list_users = list(users.values())
            is_validate = False
            if sort_field == 'name':
                is_validate = True
                for i in range(len(list_users)-1):
                    for j in range(len(list_users)-i-1):
                        if list_users[j]['name'] > list_users[j+1]['name']:
                           list_users[j],list_users[j+1] = list_users[j+1],list_users[j]
            elif sort_field == 'age':
                is_validate = True
                for i in range(len(list_users)-1):
                    for j in range(len(list_users)-i-1):
                        if list_users[j]['age'] > list_users[j+1]['age']:
                           list_users[j],list_users[j+1] = list_users[j+1],list_users[j]
            elif sort_field == 'tel':
                is_validate = True
                for i in range(len(list_users)-1):
                    for j in range(len(list_users)-i-1):
                        if list_users[j]['tel'] > list_users[j+1]['tel']:
                           list_users[j],list_users[j+1] = list_users[j+1],list_users[j]
            else:
                print('输入有误')
            if is_validate:
                print(user_info_header)
                for i in range(len(list_users)):
                    print(user_info_tpl.format(list_users[i]['name'], list_users[i]['age'], list_users[i]['tel'],'******'))

        elif action == 'exit':
            #退出程序
            fhandler = open(path,'wt')
            for user in users.values():
                fhandler.write('{0}:{1}:{2}:{3}\n'.format(user['name'],user['age'],user['tel'],user['passwd']))
            fhandler.close()
            break
        else:
            print('命令错误')
