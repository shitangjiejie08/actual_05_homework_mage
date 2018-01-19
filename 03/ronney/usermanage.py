#用户管理：增删改查，列出所有用户的list
#1.创建一个users，列表，列表中元素user用列表表示三个元素：name，age，sex
#   用户输入，根据输入来判断用户进行的操作
#2.增add，先进行判断users中是否存在用户user根据user name，存在不添加，进行更新操作；
#  不存在，再添加
#3.删delete，进行判断users中是否存在用户user根据user name，存在，则删除，不存在则不变
#4.查，即判断user是否存在users中，根据user name ，存在即打印用户信息，不存在即提示不存在
#5.打印users中所有用户信息，格式化输出

# users = []
users = {}
user_info_temp = '|{0:^10}|{1:^5}|{2:^10}|'   #格式化字符串模板，key+样式
keys = ("name","age","sex")
user_header = user_info_temp.format(keys[0],keys[1],keys[2])
while True:
    user_input= input("pls your command like add/delete/update/find/exit/list:")
    user_input = user_input.strip()
    if user_input == "add":
        # name = input("pls input your name:")
        # age = input("pls input your age:")
        # sex = input("pls input you sex:")
        user_text = input('请依次输入姓名、年龄、性别，中间以冒号分隔：')
        user_dict = dict(zip(keys,user_text.split(':')))
        user_name = user_dict.get('name')
        if user_name in users:
            print("user %s is existed" % user_name)
        else:
            users[user_name] = user_dict
            print("add user %s success" % user_name)
            print(users)

        # is_exists = False
        # for user in users:
        #     if user[0] == name:
        #         print("user exist,add fail")
        #         is_exists = True
        #         break
        # if not is_exists:      #非在上面的if接着判断，而是根据上面is_existsc重新赋值了
        #     users.append([name,int(age),sex])        #再进行判断
        #     print("add user successfully")


    elif user_input == "delete":
        user_name = input("请输入要删除的用户名：").strip()
        if users.pop(user_name,None):     #取代下面的，省一行代码，字典的pop方法，user_name存在，就弹出users字典里user_name为键的键值对，不存在就返回None，不执行打印
       # if user_name in users:
            #users.pop(user_name)
            print("user %s delete successfully" % user_name)
        else:
            print("user %s not existed,delete fail" % user_name)
            print(users)

        # name = input("pls input your name:")
        # age = input("pls input your age:")
        # sex = input("pls input you sex:")
        # user = [name,int(age),sex]
        # is_exists = False
        # for user in users:
        #     if user[0] == name:
        #         is_exists = True
        #         users.remove(user)
        #         print("delete user successfully")
        #         break
        # if not is_exists:      #非在上面的if接着判断，而是根据上面is_existsc重新赋值了
        #                                        #再进行判断
        #     print("user:%s not exist" % name)
    elif user_input == "update":
        user_text = input('请依次输入姓名、年龄、性别，中间以冒号分隔：')
        user_dict = dict(zip(keys,user_text.split(':')))
        user_name = user_dict.get('name')
        if user_name not in users:
            print("user %s not existed" % user_name)
        else:
            users[user_name] = user_dict
            print("update user %s success" % user_name)
            print(users)
        # name = input("pls input your name:")
        # age = input("pls input your age:")
        # sex = input("pls input you sex:")
        # is_exists = False
        # for user in users:
        #     if user[0] == name:
        #         is_exists = True
        #         users.remove(user)
        #         break
        # if is_exists:  # 非在上面的if接着判断，而是根据上面is_existsc重新赋值了
        #     # 再进行判断
        #     users.append([name,age,sex])
        #     print("update successfully")
    elif user_input == "find":
        name = input("请输入要查询的名字：").strip()
        print(user_header)
        for user_name,user in users.items():
            if user_name.find(name) != -1:
                print(user_info_temp.format(user["name"],user["age"],user["sex"]))

            else:
                print("user:%s not exist" % user_name)
        # name = input("pls input your name:")
        # age = input("pls input your age:")
        # sex = input("pls input you sex:")
        # is_exists = False
        # for user in users:
        #     is_exists = True
        #     print(user_header)
        #     print(user_info_temp.format(user[0],user[1],user[2]))
        # if not is_exists:  # 非在上面的if接着判断，而是根据上面is_existsc重新赋值了
        #     # 再进行判断
        #     print("user:%s not exist" % name)

    elif user_input == "list":
        print(user_header)
        for user in users.values():
            print(user_info_temp.format(user["name"], user["age"], user["sex"]))
    elif user_input == "exit":
        print("logout")
        break
    else:
        print("command not found")



'''
功能ok， 继续加油
1. 代码中的调试语句可以精简就删掉，或者用版本管理，多次修改，最后保证代码整洁度
'''
