user_info = {}
user_list = []


def display(user_info):
    if type(user_info) is dict:
        print("用户名|年龄|联系方式")
        print("{:^6}|{:^4} |{:^10}".format(user_info["name"], user_info["age"], user_info['contact']))
    else:
        print("用户名|年龄|联系方式")
        for user in user_info:
            print("{:^6}|{:^4} |{:^10}".format(user["name"], user["age"], user['contact']))

list_txt = "find/dict/add/delete/update/exit:"
while True:
    entry = input("plz: {}".format(list_txt))
    list_txt = "find/dict/add/delete/update/exit:"
    if entry == 'add':
        usernames = input("请按照以下要求输入： name：age：contact,中间用冒号分割：").strip()
        len_format = usernames.split(":")
        if len(len_format) == 3:
            username, age , contact = len_format
            user_info = dict([('name', username), ('age',age), ('contact', contact)])
            if len(user_list) > 0:
                user_name_result = [user_name["name"] for user_name in user_list]
                if user_info['name'] not in user_name_result:
                    user_list.append(user_info)
                else:
                    print("{username} already exits!".format(username=user_name["name"]))
            else:
                user_list.append(user_info)
        else:
            print("格式不符合要求，请重新选择，再添加!".format(username=usernames))

    elif entry == "delete":
        if len(user_list) != 0:
            del_ = input("plz delete username:")
            for username in user_list:
                user_name_result = [user_name["name"] for user_name in user_list]
                if user_info['name'] in user_name_result:
                    user_list.remove(username)
                    print("用户:{}已经删除成功".format(del_))
                    break
                else:
                    print("{del_} not exits".format(del_=del_))
        else:
            print("当前信息为空，无需删除 ")

    elif entry == 'dict':
        if len(user_list) > 0:
            display(user_list)
        else:
            print("当前信息为空，请先添加")
    elif entry == 'update':
        update__ = input("请按照以下要求输入： name：age：contact,中间用冒号分割：").strip()
        username, age , contact = update__.split(":")
        user_info = dict([('name', username), ('age',age), ('contact', contact)])
        for user in user_list:
            if user_info['name'] == user['name']:
                index_ = user_list.index(user)
                user_list[index_] = user_info
                print("用户信息更新成功")
                display(user_info)
                break
        else:
            print("用户不存在请重新选择")

    elif entry == 'find':
        find_ = input("请输入要查找的用户名称").strip()
        username = find_
        if len(username) > 0:
            user_name_result = [user_name["name"] for user_name in user_list]
            if username in user_name_result:
                for user_info in user_list:
                    if username == user_info['name']:
                        print("找到要查询的用户")
                        display(user_info)
                        break
            else:
                print("用户不存在请重新选择")
        else:
            print("用户不存在请重新选择")
    elif entry == "exit":
        break

    else:
        pass



'''
功能稍微有些问题, 继续坚持，加油
1. 删除逻辑有点问题呢，并非根据用户名删除用户信息
2. users如果修改为dict, 考虑下使用什么属性作为key，value如何存储，如何完成用户管理
3. 考虑代码简化update和find部分，看看循环能不能减少，逻辑更加清晰（列表推到式也是循环）
'''
