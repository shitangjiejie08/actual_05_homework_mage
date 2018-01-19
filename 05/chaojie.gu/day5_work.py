#encoding: utf-8

'''

'''

'''users ={}
user_info_tpl = '|{0:>20}|{1:>5}|{2:>20}||{3:>20}'
user_info_header = user_info_tpl.format('name', 'age', 'telephone','passwd')
path='users.txt'
fhander=open(path,'rt')
'''
import json
import sys
users={}
user_info_tpl = '|{0:>20}|{1:>5}|{2:>20}||{3:>20}'
user_info_header = user_info_tpl.format('name', 'age', 'telephone','passwd')
fhander=open('user.txt','rt')

for line in fhander:
    name,age,tel,passwd=line.strip().split(':')
    users[name]={'name':name,'age':age,'tel':tel,'passwd':passwd}

fhander.close()


def user_confirm():
    is_valid = False
    for i in range(3):
        name=input('请输入用户名：')
        passwd=input('请输入密码：')
        for user in users.values():
            if user['name']==name and user['passwd']==passwd:
                is_valid=True
                break
        if is_valid:
            break
        else:
            print('认证失败，请重试')
    if not is_valid:
        print('已超过最大认证次数，程序退出')


def user_add():
    #增加用户
    user_txt = input('请输入用户信息(用户名:年龄:电话):')
    name, age, tel,passwd = user_txt.split(':')
    if name in users:
        print('添加用户失败，用户已存在')
    else:
        users[name]={'name':name,'age':age,'tel':tel,'passwd':passwd}

def user_delete():
    #删除用户
    name = input('请输入你要删除的用户名:')
    if users.pop(name,None):
        print('删除用户成功')
    else:
        print('删除失败，用户不存在')
    #print(users)

def user_update():
    user_txt = input('请输入用户信息(用户名:年龄:电话):')
    name, age, tel = user_txt.split(':')
    if name in users:
        users[name]={'name':name,'age':age,'tel':tel,'passwd':passwd}
        print('更新用户成功')
    else:
        print('更新用户失败, 错误原因: 用户名不存在')

def user_find():
    # 查找用户
    name = input('请输入你要查询的用户名:')
    print(user_info_header)
    for user in users.values():
        if user['name'].find(name) != -1:
            print(user_info_tpl.format(user['name'], user['age'], user['tel'],'*' * len(user['passwd'])))
        else:
            print('查找用户失败，用户不存在')

def user_list():
    #罗列所有用户
    print(user_info_header)
    field=input('请输入需要排序的列：name,age,tel:')
    list_users=list(users.values())
    for i in range(len(list_users)-1):
        for j in range(len(list_users)-1):
            if list_users[i][field] < list_users[i + 1][field]:
                list_users[i], list_users[i + 1] = list_users[i + 1], list_users[i]
    for user in list_users:
        print(user_info_tpl.format(user['name'], user['age'], user['tel'],'*' * len(user['passwd'])))

def user_exit():
    fhander=open('user.txt','wt')
    for user in users.values():
        json.dumps(fhander.write('{0}:{1}:{2}:{3}\n'.format(user['name'],user['age'],user['tel'],user['passwd'])))
    fhander.close()
    sys.exit('退出程序，欢迎下次再来！')
user_confirm()

while True:
    ACTION = input('请输入你需要的操作(find/dict/add/delete/update/exit): ')
    ACTION = ACTION.strip()
    if ACTION == 'add':
        user_add()

    elif ACTION == 'delete':
        user_delete()

    elif ACTION == 'update':
        user_update()

    elif ACTION == 'find':
        user_find()

    elif ACTION == 'list':
        user_list()

    elif ACTION == 'exit':
        user_exit()

    else:
        print('命令错误,请重新选择！')
