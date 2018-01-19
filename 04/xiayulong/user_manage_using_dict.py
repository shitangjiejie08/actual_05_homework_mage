# encoding: utf-8
import os
import getpass
import copy

def mymap(a,b):
    return (a,b)

def users_quick_sort(users_list,left,right,sorted_field):
    '''
    users_list: [{"name":"xxx","age":18,"tel":"11234567890","passwd":"abc"},{"name":"yyy","age":18,"tel":"11234567890","passwd":"abc"}], 
               which is the result of list(users.values())
    left: the left boundary of users_list
    right: the right boundary of users_list
    sorted_field: can be name,age or tel
    '''
    if sorted_field == "age" or sorted_field == "tel":
        for i in range(len(users_list)):
            users_list[i][sorted_field] = int(users_list[i][sorted_field])
    if left < right:
        idx = group(users_list,left,right,sorted_field)
        users_quick_sort(users_list,left,idx-1,sorted_field)
        users_quick_sort(users_list,idx+1,right,sorted_field)

def group(users_list,left,right,sorted_field):
    a = users_list[left][sorted_field]
    idx = left
    for i in range(left+1,right+1):
        if users_list[i][sorted_field] <= a:
            idx += 1
            if idx != i :
                users_list[i],users_list[idx] = users_list[idx],users_list[i]
    users_list[left],users_list[idx] = users_list[idx],users_list[left]
    return idx




users = {}
"""{"xxx":{"name":"xxx","age":18,"tel":"11234567890","passwd":"abc"},"yyy":{"name":"yyy","age":18,"tel":"11234567890","passwd":"abc"}}"""

f = open("/data/code/users.txt")
for user in f:
    name,age,tel,passwd = user.strip().split(":")
    users[name] = {"name":name,"age":age,"tel":tel,"passwd":passwd}

f.close()


valid = False
for i in range(3):
    name = input("请输入用户名：")
    passwd  = getpass.getpass("请输入密码：")
    for v in users.values():
        if v["name"] == name and v["passwd"] == passwd:
            valid = True
            print("认证成功")
            break
    if not valid:
        print("认证失败，请重试")
    else:
        break

if not valid:
    print("验证次数超过限制，程序退出")
else:
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
                passwd = getpass.getpass("请设置密码：")
                info_list.append(passwd)
                users[info_list[0]] = dict(map(mymap,("name","age","tel","passwd"),info_list))
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
                passwd = getpass.getpass("请设置密码：")
                info_list.append(passwd)
                users[info_list[0]] = dict(map(mymap,("name","age","tel","passwd"),info_list))
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
            sorted_field = input("希望按照哪一列升序列出(name,age,tel)")
            users_tmp = list(users.values())
            users_list = copy.deepcopy(users_tmp)
            users_quick_sort(users_list,0,len(users_list)-1,sorted_field)
            print("用户信息\n用户名:\t年龄:\t电话:\t密码:")
            for i in range(len(users_list)):
                print("{0}\t{1}\t{2}\t{3}".format(users_list[i]["name"],users_list[i]["age"],users_list[i]["tel"],"*"*len(users_list[i]["passwd"])))
                print()
        elif action == "exit":
            fd = open("/data/code/users.txt.temp","w")
            for v in users.values():
                fd.write(":".join([v["name"],v["age"],v["tel"],v["passwd"]])+"\n")
                #print(":".join([v["name"],v["age"],v["tel"]]))
            fd.close()
            os.rename("/data/code/users.txt.temp","/data/code/users.txt")
            break
        else:
            print("输入有误")

    print(users)
