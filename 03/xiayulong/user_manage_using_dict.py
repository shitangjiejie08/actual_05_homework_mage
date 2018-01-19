# encoding: utf-8


users = {"xxx":{"name":"xxx","age":18,"tel":"11234567890"},"yyy":{"name":"yyy","age":18,"tel":"11234567890"}}
"""{"xxx":{"name":"xxx","age":18,"tel":"11234567890"},"yyy":{"name":"yyy","age":18,"tel":"11234567890"}}"""

def mymap(a,b):
    return (a,b)


while True:
    action = input("Your input (add/delete/update/find/list/exit)")
    action = action.lower()
    if action == "add":
        info = input("请输入用户名、年龄、电话，并且用英文冒号分隔，例如 Tony:22:12345678  ")
        info = info.strip()
        info_list = info.split(":")
        if len(info_list) != 3:
            print("输入信息不匹配要求，添加失败！")
            continue
        if info_list[0] not in users:
            users[info_list[0]] = dict(map(mymap,("name","age","tel"),info_list))
        else:
            print("用户已存在,添加失败")


    elif action == "delete":
        name = input("请输入删除的用户名：")
        if name in users:
            users.pop(name)
            print("用户",name,"删除成功！")
        else:
            print("用户",name,"已经存在,删除失败！")


    elif action == "update":
        info = input("请输入将要更新的用户名、年龄、电话，并且用英文冒号分隔，例如 Tony:22:12345678  ")
        info = info.strip()
        info_list = info.split(":")
        if len(info_list) != 3:
            print("输入信息不匹配要求，更新失败！")
            continue
        if info_list[0] in users:
            users[info_list[0]] = dict(map(mymap,("name","age","tel"),info_list))
            print("更新成功！")
        else:
            print("用户不存在,更新失败!")

    elif action == "find":
        name = input("请输入查找的用户名：")
        if name in users:
            print("用户信息如下：")
            for k,v in users[name].items():
                print("{0:<10}:{1:<10}".format(k,v))
        else:
            print("用户不存在")
    elif action == "list":
        print("用户信息\n用户名:\t年龄:\t电话:\t")
        for user in users:
            print("{0}\t{1}\t{2}".format(users[user]["name"],users[user]["age"],users[user]["tel"]))
            print()
    elif action == "exit":
        break
    else:
        print("输入有误")

print(users)



'''
功能ok， 继续坚持，加油
1. 考虑查询用户名只要存在查找的字符串就显示
2. 可以考虑代码有什么地方可以优化减少代码冗余
'''
