'''
让用户在控制台上输入"find/list/add/delete/update/exit"格式字符串
如果输入add，则让用户继续输入用户名、年龄、联系方式等数据，将用户数据(用户名, 年龄，联系方式)，放入list中存储，在放入list之前检查用户名不重复，如果重复，则提示用户已存在。
如果输入delete，则让用户输入"用户名"字符串，根据用户名查找list中数据，若存在数据则将该数据移除，若用户数据不存在，则提示不存在。
如果输入update，则让用户分别输入用户名、年龄、联系方式等数据，根据用户名查找list中数据，若存在数据则将改数据更新为新的(用户名, 年龄，联系方式)，若用户数据不存在，则提示不存在。
如果用户输入find，则让用户输入"用户名"，根据用户名查找list中数据用户名包含字符串的用户信息，并打印。
如果用户输入list，则打印所有用户信息。
打印用户第一个行数据，第一行数据为用户信息描述，从第二行开始为用户数据。
如果用户输入exit，则打印退出程序，并退出。
'''

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

'''
将用户管理中各功能修改为函数
-登录验证、添加、修改、查询、列表、删除
-用户信息文件读、写
使用json格式存储用户信息
列表展示排序:sorted()/list.sort()
'''

'''
"keith1:18:110:abc"
"keith2:19:111:abc"
"keith3:20:112:abc"
"keith4:21:113:abc"
"jerry:36:120:abcabc"
"charlse:3:139:abc"
"tom:38:138:abc"
'''

#encoding: utf-8
import getpass
import json

#从文件读取用户信息
def user_load():
    fhandler = open(path,'rt')
    for line in fhandler:
        line = json.loads(line)
        name,age,tel,passwd = line.strip().split(':')
        users[name] = {'name':name,'age':int(age),'tel':int(tel),'passwd':passwd}
    fhandler.close()

#登录验证，最多三次，用户输入用户名和密码
def user_auth():
    is_valid = False
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
    return is_valid        

#添加用户
def user_add():
    useradd = input('请按格式输入信息(用户名:年龄:联系方式:密码): ')
    name,age,tel,passwd = useradd.split(':')
    if name in users:
        print('添加失败，用户已存在')
    else:
        users[name] = {'name':name,'age':int(age),'tel':int(tel),'passwd':passwd}    
        print('添加成功')

#删除用户
def user_del():
    name = input('请输入要删除的用户名：')
    if name in users:
        del users[name]
        print('删除用户成功')
    else:
        print('删除失败，用户不存在')        

#修改用户信息
def user_update():
    userupdate = input('请按格式输入信息(用户名:年龄:联系方式:密码): ')
    name,age,tel,passwd = userupdate.split(':')
    if name in users:
        users[name] = {'name':name,'age':int(age),'tel':(tel),'passwd':passwd}
        print('更新用户成功')
    else:
        print('更新失败，用户不存在')

#查询用户
def user_find():
    name = input('请输入要查找的用户名：')
    is_exists=False
    print(user_info_header)
    for user in users.values():
        if user['name'].find(name) != -1:
            is_exists=True
            print(user_info_dict.format(name=user['name'],age=user['age'],tel=user['tel'],passwd='*'*len(user['passwd'])))
    if not is_exists:
        print('用户不存在')

#列出所有用户
def user_list():
    field = input('请输入排序的列(name,age,tel):')
    print(user_info_header)
    list_users = list(users.values())
    #list.sort()排序
    list_users.sort(key=lambda x:x[field])
    for user in list_users:
        print(user_info_dict.format(name=user['name'],age=user['age'],tel=user['tel'],passwd='*'*len(user['passwd'])))

#写入用户信息到文件
def user_save():
    fhandler = open(path,'wt')
    for user in users.values():
        user_json = json.dumps('{}:{}:{}:{}'.format(user['name'],user['age'],user['tel'],user['passwd']))
        fhandler.write(user_json+'\n')
    fhandler.close()    
    print('数据已保存，退出程序')

path='users.txt'

users = {}
user_info_dict = '|{name:^20}|{age:^15}|{tel:^20}|{passwd:^15}|'
user_info_header = user_info_dict.format(name='name',age='age',tel='tel',passwd='passwd')

user_load()

if not user_auth():
    print('超过最大认证次数，退出程序')
else:
    while True:
        action = input('Please input(add/delete/find/update/list/exit): ')
        if action == 'add':
            user_add()

        elif action == 'delete':
            user_del()

        elif action == 'update':
            user_update()

        elif action == 'find':
            user_find()

        elif action == 'list':
            user_list()

        elif action == 'exit':
            user_save()
            break

        else:
            print('输入错误')
