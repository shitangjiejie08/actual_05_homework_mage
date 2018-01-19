# _*_ coding: utf-8 _*_
import os
import sys
import json
"""
人员管理 增删改查
"""

# users = {'hug': {'age': 12, 'name': 'hug', 'tel': 13, 'password': '123456'}, 'had': {'age': 1, 'name': 'had', 'tel': 2, 'password': '123456'}}


def load_user_data(target):
    '''
    从文件中读取用户数据信息
    '''
    if os.path.isfile(target):
        with open(target, 'rt') as f:
            return json.loads(f.read())


def save_user_data(target):
    """保存用户信息到文件中"""
    global users
    if os.path.isfile(target):
        with open(target, 'w') as f:
            f.write(json.dumps(users))
    return True


def verify_user_data(users_data, user_name, user_pass):
    """
    验证用户名密码
    """
    for user in users_data.values():
        if user['name'] == user_name and user['password'] == user_pass:
            return True
    return False


def add_user(user_name, user_tel, user_age, user_pass):
    """
    添加用户
    """
    global users
    if user_name not in users:
        users[user_name] = {'name': user_name, 'age': int(user_age), 'tel': int(user_tel), 'password': user_pass}
        return True
    return False


def delete_user(user_name):
    """删除用户"""
    global users
    if user_name in users:
        if users.pop(user_name):
            return True
    return False


def split_user_input(input_data):
    user = input_data.strip().split(':')
    if len(user) == 4:
        return user
    return False


def update_user(user_name, user_age, user_tel, user_pass):
    global users
    if name in users:
        users[user_name] = {'name': user_name, 'age': int(user_age), 'tel': int(user_tel), 'password':  user_pass}
        return True
    return False


def find_user(user_name):
    global users
    result = {}
    for name in users.keys():
        if name.find(user_name) != -1:
            result[name] = users[name]
    return result


def show_user(show_data, sort_row='name'):
    user_info_split = '- ' * 40
    user_info_tpl = '|{name:20} |{age:20} |{tel:20}|{password:20}'
    user_info_tpl_format = user_info_tpl.format(name='name', age='age', tel='tel', password='password')
    print(user_info_tpl_format)
    print(user_info_split)
    for user in sorted(show_data.values(), key=lambda u: u[sort_row]):
        print(user_info_tpl.format(name=user['name'], age=user['age'], tel=user['tel'],
                                   password='*' * len(user['password'])))


def main():
    users_db = "users.db"
    auth_times = 3
    is_auth = False
    global users
    users = load_user_data(users_db)
    while auth_times > 0:
        name_auth = input("name>>")
        pass_auth = input("password>>")
        if verify_user_data(users_data=users,  user_name=name_auth, user_pass=pass_auth):
            is_auth = True
            print("认证通过!")
            break
        else:
            auth_times -= 1
            print("认证失败,请重试,还剩{}次".format(auth_times))
    if not is_auth:
        sys.exit(1)

    while True:
        action = input("find/list/add/delete/update/exit:")
        if action == "add":
            while True:
                input_data = input("name:age:tel:password >>")
                user = split_user_input(input_data)
                if user:
                    break
                else:
                    print("数据格式有误,请重新输入")
            name, age, tel, password = user
            if add_user(name, tel, age, password):
                print("用户加成功")
            else:
                print("用户添加失败")
        elif action == "delete":
            name = input("delete user name:")
            if delete_user(name):
                print("用户删除成功")
            else:
                print("用户删除失败")
        elif action == "update":
            while True:
                input_data = input("name:age:tel:password >>")
                user = split_user_input(input_data)
                if user:
                    break
                else:
                    print("数据格式有误,请重新输入")
            name, age, tel, password = user
            if update_user(name, age, tel, password):
                print("用户信息更新成功")
            else:
                print("用户信息更新失败")
        elif action == "find":
            find_name = input("find name:")
            find_users = find_user(find_name)
            if find_users:
                show_user(find_users)
            else:
                print("未找到任何相关用户")
        elif action == "list":
            while True:
                sort_row = input("请输入需要排序的列name or age or tel>>")
                if sort_row in ['name', 'age', 'tel']:
                    break
                else:
                    print("输入的排序列名不正确!")
            show_user(users, sort_row)
        elif action == "exit":
            if save_user_data(users_db):
                print("数据保存成功, 程序正常退出")
                sys.exit(0)
        else:
            print("指令输入错误, 请输入正确的指令!")


if __name__ == "__main__":
    main()