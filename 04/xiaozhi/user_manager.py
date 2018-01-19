import os
import getpass

if not os.path.exists("user_info"):
    print("初始化用户信息")
    login_user = input("请设置用户名：")
    login_passwd = getpass.getpass("设置密码:")
    with open("user_info", 'w') as f:
        f.write("{login_user}:{login_passwd}\n".format(login_user=login_user,login_passwd=login_passwd))

users = {}
with open("users.txt") as f:
    for line in f.readlines():
        name, age, tel = line.strip().split(":")
        users[name] = {"name":name, 'age':age, 'tel':tel}

users_info_tpl = '|{name:20}|{age:20}|{tel:20}'
users_info_tpl_format = users_info_tpl.format(name='name',age='age', tel='tel' )
is_valid = False
i = 0

with open("user_info") as f:
    for line in f:
        user_name, user_passwd = line.strip().split(":")
        for num in range(3):
            name = input("请输入用户名:")
            passwd= getpass.getpass("请输入密码:")
            i = i + 1
            if user_name == name and user_passwd == passwd:
                    is_valid = True
                    break
            else:
                print("认证失败，请重试！还有 {num} 次机会".format(num=3-i))
        if is_valid:
            break
if not is_valid:
    print("已经超过最大认证次数")
else:

    while True:
        action = input("find/list/add/delete/update/exit/add_manager/update_manager:")
        if action == "add":
            user_text = input("请输入用户信息(用户名：年龄：电话):")
            name, age, tel = user_text.split(":")
            if name in users:
                print("{name} alreay exists".format(name=name))
            else:
                users[name] = {'name':name, 'age':age, 'tel':tel}
                print("{name}, {age}, {tel} add success!".format(name=name, age=age, tel=tel))
            print(users)

        elif action == "delete":
            name = input("请输入删除的用户名:")
            if users.pop(name, None):
                print("delete {name} success".format(name=name))
            else:
                print("delete fail {name}".format(name=name))
            print(users)

        elif action == "update":
            user_text = input("请输入用户信息(用户名：年龄：电话):")
            name, age, tel = user_text.split(":")
            if name in users:
                del users[name]
                print("delete {name} success".format(name=name))
                users[name] = {'name':name, 'age':age, 'tel':tel}
                print("{name}, {age}, {tel} add success!".format(name=name, age=age, tel=tel))
            else:
                print("update fail {name}".format(name=name))
            print(users)
        elif action == "find":
            name = input("输入查找的用户名:")
            print(users_info_tpl_format)
            is_exists = False
            for user in users.values():
                if user['name'].find(name) != -1:
                    print('|{name:20}|{age:20}|{tel:20}'.format(name=user['name'], age=user['age'],tel=user['tel']))
                    is_exists = True
            if not is_exists:
                print("find  fail {name}".format(name=name))
        elif action == "list":
            if len(users) != 0:
                sorted_user_ = input("默认是name排序，请输入name, age，tel 或者直接回车确认:")
                if len(sorted_user_) != 0 and sorted_user_ == 'name':
                    print(users_info_tpl_format)
                    name_results = []
                    for user_s in users.values():
                        age, name, tel = list(user_s.items())
                        name_results.append([name, age, tel])
                    for user_ in sorted(name_results):
                        if len(users) != 0:
                            user = dict(user_)
                            print('|{name:20}|{age:20}|{tel:20}'.format(name=user['name'], age=user['age'],tel=user['tel']))

                elif sorted_user_ == "age":
                    print(users_info_tpl_format)
                    age_results = []
                    for user_s in users.values():
                        age, name, tel = list(user_s.items())
                        age_results.append([age, name, tel])
                    for user_ in sorted(age_results):
                        if len(users) != 0:
                            user = dict(user_)
                            print('|{name:20}|{age:20}|{tel:20}'.format(name=user['name'], age=user['age'],tel=user['tel']))

                elif sorted_user_ == "tel":
                    print(users_info_tpl_format)
                    tel_results = []
                    for user_s in users.values():
                        age, name, tel = list(user_s.items())
                        tel_results.append([tel, name, age])
                    for user_ in sorted(tel_results):
                        if len(users) != 0:
                            user = dict(user_)
                            print('|{name:20}|{age:20}|{tel:20}'.format(name=user['name'], age=user['age'],tel=user['tel']))
        elif action == "exit":
            with open("users.txt", 'w') as f:
                for user in users:
                    f.write("{}:{}:{}\n".format(user, users[user]['age'], users[user]['tel']))
                #for user in users.values():
                    #f.write("{}:{}:{}\n".format(user['name'], [user]['age'], [user]['tel']))
            break
        elif action == "add_manager":
            with open("user_info", "a+") as f:
                name = input("请输入用户名:")
                passwd= igetpass.getpass("请输入密码:")
                f.write("{login_user}:{login_passwd}\n".format(login_user=name, login_passwd=passwd))
                print("增加用户{}成功".format(name))


        elif action == "update_manager":
            user_managers = {}
            with open("user_info") as f:
                for line in f.readlines():
                    user_name, user_passwd = line.strip().split(":")
                    user_managers[user_name] = user_passwd
                update_user_name = input("请输入要修改的用户名:")
                for name in user_managers:
                    if update_user_name == name:
                        passwd = getpass.getpass("设置密码:")
                        print("密码设置成功，当前的密码为:{}".format(("*")*len(passwd)))
                        break

                with open("user_info", 'w') as f:
                    for k, v in user_managers.items():
                            f.write("{login_user}:{login_passwd}\n".format(login_user=k, login_passwd=v))

        else:
            pass