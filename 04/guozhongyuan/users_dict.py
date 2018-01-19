#encoding: utf-8

'''
1. 每一个用户存储信息修改为字典
{name : xxx, age : xxxx, tel: xxx}
2. 用户输入了三次，修改为一次，使用:分隔用户信息
3. 查找的时候使用包含关系，name包含查找的字符串
'''


'''
修改： 改变存储数据结构为
       {
        name1 : {name1 : xxx, age : xxxx, tel: xxx }
        name2 : {name2 : xxx, age : xxxx, tel: xxx }
       }


'''
#users = []
#


'''
2017-04-17
修改  
1.增加用户密码
2.用户密码显示为*
3.用户验证 账户名密码

郭中源 

'''

users = {}
user_info_tpl = '|{0:>20}|{1:>5}|{2:>20}|{3:>20}|'
user_info_header = user_info_tpl.format('name', 'age', 'telephone','password')

path='users.txt'

cunchu = open('users.txt')
for line in cunchu:
    name,age,tel,password = line.strip().split(':')
    users[name] = {'name' : name, 'age' : age, 'tel' : tel ,'password':password }
cunchu.close()

#验证用户账户
#

while True:
    action = input('please input(yourname:password):')
    print (action)
    name,passwordin = action.split(':')
    is_exists =False
    #遍历字典
    for user in users:
        if name == user:
            #字典
            usersdict= {}
            usersdict = users[user]
            print('---')
            if passwordin == usersdict['password']:
                print ('完成验证')
                is_exists = True
                break

    if not is_exists:
        print ('账号密码不正确')
    else:
        break


while True:
    action = input('please input(find/list/add/delete/update/exit):')
    print(action)
    if action == 'add':
        #增加用户
        user_txt = input('请输入用户信息(用户名:年龄:电话:密码):')
        name, age, tel,password = user_txt.split(':')
        is_exists = False
        for user in users:
            if name == user:
                print('添加用户失败, 失败原因: 用户名已存在')
                is_exists = True
                break

        if not is_exists:
            #users.append({'name' : name, 'age' : age, 'tel' : tel})
            users[name] = {'name' : name, 'age' : age, 'tel' : tel,'password':password}
            print('添加用户成功')
        #print(users)

    elif action == 'delete':
        #删除用户
        name = input('请输入你要删除的用户名:')
        if users.pop(name, None):
            print ('删除成功')
        else:
            print ('删除失败，用户不存在')

    elif action == 'update':
        # 更改用户
        user_txt = input('请输入用户信息(用户名:年龄:电话:密码):')
        name, age, tel,password = user_txt.split(':')
        is_exists = False
        for user in users:
            if name == user:
                users.pop(user)
                is_exists = True
                break

        if is_exists:
            #users[name]={'name' : name, 'age' : age, 'tel' : tel,'password':password}
            users.update({'name':{'name' : name, 'age' : age, 'tel' : tel,'password':password}})
            print('更新用户成功')
            #print(users)
        else:
            print('更新用户失败, 错误原因: 用户名不存在')
    elif action == 'find':
        # 查找用户
        name = input('请输入你要查询的用户名:')
        is_exists = False
        print(user_info_header)
        #字典
        for user in users.values():
            #user{}
            if  user['name'].find(name) != -1:
                print(user_info_tpl.format(user['name'], user['age'], user['tel'],len(user['password'])*'*'))
                is_exists = True

        if not is_exists:
            print('没有该用户信息')

    elif action == 'list':
        #罗列所有用户
        print(user_info_header)
        #keys = sorted(users.items(),key=lambda d:d[0])
        #dict(keys)
        for user in users:
            uservalue = users[user]
            #print(user_info_tpl.format(user['name'], user['age'], user['tel']))
            #print(user_info_tpl.format(uservalue['name'], uservalue['age'], uservalue['tel'],uservalue['password']))
            print(user_info_tpl.format(uservalue['name'], uservalue['age'], uservalue['tel'],len(uservalue['password'])*'*'))

    elif action == 'exit':
        writefile = open('users.txt','wt')
        for user in users:
            uservalue = users[user]
            writefile.write('{0}:{1}:{2}:{3}\n'.format(uservalue['name'], uservalue['age'], uservalue['tel'],uservalue['password']))
            writefile.flush()


        writefile.close()
        #退出程序
        break
    else:
        print('命令错误')












'''
#写文件函数
def writefile():
    writefile = open(path,'wt')
    for user in users.values():
        writefile.write('{0}:{1}:{2}\n'.format(uservalue['name'], uservalue['age'], uservalue['tel'],uservalue['password']))
    writefile.close()
'''


