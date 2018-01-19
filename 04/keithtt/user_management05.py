'''
在用户管理操作之前添加用户认证功能
提示用户输入用户名和手机号，如果两个数据都正确，则通过验证进行查询、添加、删除、更改等操作
当输入错误3次后，退出程序
'''
'''
>>> 'keith:18:110'.split(':')
['keith', '18', '110']
>>> name,age,tel='keith:18:110'.split(':')
>>> name
'keith'
>>> age
'18'
>>> tel
'110'
'''
'''
在用户管理功能中添加密码信息
增、改添加用户密码输入
显示时将用户密码显示为N(密码长度)个*
用户验证修改为用户名和密码
加分项
输入list后提示用户排序字段（name, age, tel），根据用户输入字段进行排序（升序），然后将结果输入
'''

#encoding: utf-8
import getpass

path='users.txt'

users = {}
user_info_dict = '|{name:^20}|{age:^15}|{tel:^20}|{passwd:^15}|'
user_info_header = user_info_dict.format(name='name',age='age',tel='tel',passwd='passwd')

fhandler = open(path,'rt')
for line in fhandler:
    name,age,tel,passwd = line.strip().split(':')
    users[name] = {'name':name,'age':age,'tel':tel,'passwd':passwd}
fhandler.close()

is_valid = False
#用户认证，最多三次，用户输入用户名和电话
for i in range(3):
    name = input('请输入用户名：')
    passwd = getpass.getpass('请输入密码：')
    #认证
    for user in users.values():
        if user['name'] == name and user['passwd'] == passwd:
            is_valid = True
            print('认证成功')
            break
    if is_valid:
        break
    else:
        print('认证失败，请重试')

if not is_valid:
    print('超过最大认证次数，退出程序')
else:
    while True:
        action = input('Please input(add/delete/find/update/list/exit): ')
        if action == 'add':
            useradd = input('请按格式输入信息(用户名:年龄:联系方式:密码): ')
            name,age,tel,passwd = useradd.split(':')
            if name in users:
                print('添加失败，用户已存在')
            else:
                users[name] = {'name':name,'age':age,'tel':tel,'passwd':passwd}    
                print('添加成功')

        elif action == 'delete':
            name = input('请输入要删除的用户名：')
            if name in users:
                del users[name]
                print('删除用户成功')
            else:
                print('删除失败，用户不存在')

        elif action == 'update':
            userupdate = input('请按格式输入信息(用户名:年龄:联系方式:密码): ')
            name,age,tel,passwd = userupdate.split(':')
            if name in users:
                users[name] = {'name':name,'age':age,'tel':tel,'passwd':passwd}
                print('更新用户成功')
            else:
                print('更新失败，用户不存在')

        elif action == 'find':
            name = input('请输入要查找的用户名：')
            is_exists=False
            print(user_info_header)
            for user in users.values():
                if user['name'].find(name) != -1:
                    is_exists=True
                    print(user_info_dict.format(name=user['name'],age=user['age'],tel=user['tel'],passwd='*'*len(user['passwd'])))
            if not is_exists:
                print('用户不存在')    

        elif action == 'list':
            field = input('请输入排序的列(name,age,tel):')
            print(user_info_header)
            list_users = list(users.values())
            '''
            for j in range(len(list_users) - 1):
                for i in range(len(list_users) - 1):
                    if list_users[i][field] < list_users[i + 1][field]:
                        list_users[i], list_users[i + 1] = list_users[i + 1], list_users[i]
            '''
            #list.sort()排序
            list_users.sort(key=lambda x:x[field])
            for user in list_users:
                print(user_info_dict.format(name=user['name'],age=user['age'],tel=user['tel'],passwd='*'*len(user['passwd'])))

        elif action == 'exit':
            fhandler = open(path,'wt')
            for user in users.values():
                fhandler.write('{}:{}:{}:{}\n'.format(user['name'],user['age'],user['tel'],user['passwd']))
            fhandler.close()    
            print('数据已保存，退出程序')
            break

        else:
            print('输入错误')