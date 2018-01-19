#encoding: utf-8

'''
1. 每一个用户存储信息修改为字典
{name : xxx, age : xxxx, tel: xxx}
2. 用户输入了三次，修改为一次，使用:分隔用户信息
3. 查找的时候使用包含关系，name包含查找的字符串

防止用户重复，使用字典存储
{
    Evan:{'name':'Evan','age':28,'tel':10000,'pwd':****}
}
'''

fhandler = open('users.txt')
users = {}
for user in fhandler:
    name, age, tel, pwd = user.strip().split(':')
    users[name] = {'name':name,'age':age,'tel':tel, 'pwd': pwd}
fhandler.close()
user_info_tpl = '|{0:^20}|{1:^5}|{2:^20}|{3:^10}'
save_format = '{}:{}:{}:{}\n'
user_info_header = user_info_tpl.format('name', 'age', 'telephone','password')
is_valid = False

#用户认证，最多三次，用户输入用户名和电话
for i in range(3):
    name = input('请输入用户名:')
    pwd = input('请输入密码：')
    #认证：
    for user in users.values():
        if user['name'] == name and user['pwd'] == pwd:
            is_valid = True
            break
    if is_valid:
        break
    else:
        print('用户名或密码不正确，请重试。')
if not is_valid:
    print('认证三次，失败')
else:
    print('欢迎 %s' % name)
    while True:
        action = input('please input(find/list/add/delete/update/exit):')
        if action == 'add':
            #增加用户
            user_txt = input('请输入用户信息(用户名:年龄:电话:密码):')
            name, age, tel, pwd = user_txt.split(':')
            if name in users:
                print('添加用户失败, 失败原因: 用户名已存在')
            else:
                users[name] = {'name':name,'age':age,'tel':tel,'pwd':pwd}
                print('添加用户成功')
            #print(users)

        elif action == 'delete':
            #删除用户
            name = input('请输入你要删除的用户名:')
            if users.pop(name,None):
                print('删除用户成功')
            else:
                print('删除用户失败, 失败原因: 用户名不存在')
            
        elif action == 'update':
            # 更改用户
            user_txt = input('请输入用户信息(用户名:年龄:电话:密码):')
            name, age, tel,pwd= user_txt.split(':')
            if name in users:
                users[name] = {'name':name,'age':age,'tel':tel,'pwd':pwd}
                print('更新用户成功')
            else:
                print('更新用户失败, 错误原因: 用户名不存在')

        elif action == 'find':
            # 查找用户
            name = input('请输入你要查询的用户名:')
            is_exist = False
            print(user_info_header)
            for user in users.values():
                if user['name'].find(name) != -1:
                    print(user_info_tpl.format(user['name'], user['age'], user['tel'],'*'*len(user['pwd'])))
                    is_exist = True
            if not is_exist:
                print('没有该用户信息')
            
        elif action == 'list':
            #罗列所有用户  
            sort_item = input('请输入要进行排序的字段（name/age/tel): ').lower()
            if sort_item in ('name','age','tel'):
                sort_users = sorted(users.values(), key = lambda x:x[sort_item]) #使用sorted针对字典数据进行排序
                #print(sort_users)
            else:
                print('Key error, try again.')
                continue
            print(user_info_header)
            for user in sort_users:
                print(user_info_tpl.format(user['name'], user['age'], user['tel'],'*'*len(user['pwd'])))

        elif action == 'exit':
            #退出程序
            fhandler = open('users.txt','wt')

            for user in users.values():
                fhandler.write(save_format.format(user['name'], user['age'], user['tel'],user['pwd']))
            fhandler.close()
            print('exit and save')

            break
        else:
            print('命令错误')
