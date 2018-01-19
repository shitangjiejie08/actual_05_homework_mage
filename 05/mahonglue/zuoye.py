import json

path = 'users.txt'

user_info_tpl = '|{0:>20}|{1:>5}|{2:>20}|{3:>20}|'
user_info_header = user_info_tpl.format('name', 'age', 'telephone', 'password')

def read_file(path):
    users = {}
    fhandler = open(path, 'rt')
    for line in fhandler:
        name, age, tel, password = line.strip().split(':')
        users[name] = {'name': name, 'age': age, 'tel': tel, 'password': password}
    fhandler.close()
    return users


#用户认证，最多3次，用户输入用户名和电话
def login(users):
    is_valid = False
    for i in range(3):
        name = input('请输入用户名:')
        password = input('请输入密码:')
        #认证
        for user in users.values():
            if user['name'] == name and user["password"] == password:
                is_valid = True
                break
        if is_valid:
            break
        else:
            print("认证失败，请重试")
    return is_valid

def add(users):
    user_txt = input('请输入用户信息(用户名:年龄:电话:密码):')
    name, age, tel, password = user_txt.split(":")
    if name in users:
        print('添加用户失败, 失败原因: 用户名已存在')
    else:
        users[name] = {'name': name, 'age': age, 'tel': tel, 'password': password}
    return users

def delete(users):
    name = input('请输入你要删除的用户名:')
    if users.pop(name, None):
        print('删除用户成功')
    else:
        print('删除用户失败, 失败原因: 用户名不存在')
    return users

def update(users):
    user_txt = input('请输入用户信息(用户名:年龄:电话:密码):')
    name, age, tel, password = user_txt.split(':')
    if name in users:
        users[name] = {'name': name, 'age': age, 'tel': tel, 'password': password}
        print('更新用户成功')
    else:
        print('更新用户失败, 错误原因: 用户名不存在')
    return users

def find(users):
    name = input('请输入你要查询的用户名:')
    is_exists = False
    print(user_info_header)
    for user in users.values():
        if user['name'].find(name) != -1:
            print(user_info_tpl.format(user['name'], user['age'], user['tel'], '*' * len(user['password'])))
            is_exists = True
    if not is_exists:
        print('没有该用户信息')
    return 1
def list_user(users):
    field = input('请输入排序的列(name, age, tel):')
    print(user_info_header)
    list_users = list(users.values())
    if field == "name":
        sort_users = sorted(list_users,key=lambda x:x['name'])
    elif field == "age":
        sort_users = sorted(list_users, key=lambda x: x['age'])
    else:
        sort_users = sorted(list_users, key=lambda x: x['tel'])
    for user in sort_users:
        print(user_info_tpl.format(user['name'], user['age'], user['tel'], '*' * len(user['password'])))
    return 1
def exit_user(path):
    def write_file(path):
        fhandler = open(path, 'wt')
        for user in users.values():
            fhandler.write('{0}:{1}:{2}:{3}\n'.format(user['name'], user['age'], user['tel'], user['password']))
        fhandler.close()
    write_file(path)
    return 1

users = read_file(path)
if not login(users):
    print("以超过最大次数")
else:
    while True:
        action = input('please input(find/list/add/delete/update/exit):')
        if action == 'add':
            add(users)
        elif action == 'delete':
            delete(users)
        elif action == 'update':
            update(users)
        elif action == 'find':
            find(users)
        elif action == 'list':
            list_user(users)
        elif action == 'exit':
            exit_user(users)
            break
        else:
            print("命令错误")

def json_read_file(path):
    users = {}
    fhandler = open(path, 'rt')
    for line in fhandler:
        name, age, tel, password = line.strip().split(':')
        users[name] = {'name': name, 'age': age, 'tel': tel, 'password': password}
    fhandler.close()
    json_users = json.dumps(users)
    return json_users

def json_write_file(json_users,path):
    fhandler = open(path,'wt')
    for user in json.loads(json_users).values():
        fhandler.write('{0}:{1}:{2}:{3}\n'.format(user['name'], user['age'], user['tel'], user['password']))
    fhandler.close()
    return 1
