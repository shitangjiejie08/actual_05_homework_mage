# encoding: utf:8
import sys

def handlerUser(action):
    users = fhandler_r()
    tp1 = '|{:>10}|{:>5}|{:>15}|{:>16}'
    header = tp1.format('name', 'age', 'tel','pwd')

    #while True:
    try:
        #action = input('请输入操作(find/list/add/delete/update/exit):')
        action = action.strip()
        if action == 'add':
            str_data = input('请按格式输入信息，如  用户名：年龄：联系方式：密码 （用英文:分割）').strip()
            name = str_data.split(":")[0]
            age = str_data.split(":")[1]
            tel = str_data.split(":")[2]
            pwd = str_data.split(":")[3]
            # user_tuple = (name, age, tel)
            user_dict = {"name":name, "age": age, "tel":tel, "pwd":pwd}
            is_exists = False
            for user in users:
                if user['name'] == name:
                    is_exists = True
                    print('用户已存在')
                    break

            if not is_exists:
                users.append(user_dict)
                fhandler_w(users=users)
                print('添加成功')
        elif action == 'delete':
            name = input('请输入用户名：')
            is_exists = False
            for user in users:
                if name == user["name"]:
                    is_exists = True
                    users.remove(user)
                    fhandler_w(users=users)
                    print('已删除用户%s' % name)
                    break
            if not is_exists:
                print('用户不存在')
        elif action == 'update':
            str_data = input('请按格式输入信息，如  用户名：年龄：联系方式:密码 （用英文:分割）:')
            name = str_data.split(":")[0]
            is_exists = False
            for user in users:
                if name == user["name"]:
                    users.remove(user)
                    is_exists = True
                    break
            if is_exists:
                age = str_data.split(":")[1]
                tel = str_data.split(":")[2]
                pwd = str_data.split(":")[3]
                user_dict = {"name":name, "age":age, "tel":tel, "pwd":pwd}
                users.append(user_dict)
                fhandler_w(users=users)
                print("用户内容已更新")
            if not is_exists:
                print("用户信息不存在")
        elif action == 'find':
            name = input("请输入用户名：").strip()
            print(header)
            is_exists = False
            for user in users:
                if name in user["name"]:
                    password = '*' * len(user['pwd'])
                    print(tp1.format(user["name"], user["age"], user["tel"], password))
                    is_exists = True
                    continue

            if not is_exists:
                print("用户不存在")
        elif action == 'list':
            handler = input("请输入排序依据字段： name or age or tel :")
            insertionSort(l=users, handler=handler)
            print(header)
            for user in users:
                password = '*' * len(user['pwd'])
                print(tp1.format(user["name"], user["age"], user["tel"], password))
        elif action == 'exit':
            print("程序已退出")
            return 1
    except:
        print("输入有误，请重新选择并按格式输入")


def fhandler_r():
    users = []
    f = open("user.txt", "r")
    for line in f:
        if line != "":
            name = line.strip().split(":")[0]
            age = line.strip().split(":")[1]
            tel = line.strip().split(":")[2]
            pwd = line.strip().split(":")[3]
            user_dict = {"name":name, "age":age, "tel":tel, "pwd":pwd}
            users.append(user_dict)
            continue
        else:
            f.close()
            break
    return users


def fhandler_w(users):
    f = open("user.txt", "w")
    for user in users:
        name = user["name"]
        age = user["age"]
        tel = user["tel"]
        pwd = user["pwd"]
        i = str(name)+":"+str(age)+":"+str(tel)+":"+str(pwd)
        f.write(i)
        f.write("\n")
    f.close()

def fhandler_a(users):
    f = open("user.txt", "a")
    for user in users:
        name = user["name"]
        age = user["age"]
        tel = user["tel"]
        pwd = user["pwd"]
        i = str(name)+":"+str(age)+":"+str(tel)+":"+str(pwd)
        f.write(i)
        f.write("\n")
    f.close()




def insertionSort(l,handler):            ###插入排序
    for i in range(len(l)):
        min_index = i
        for j in range(i+1, len(l)):    #####循环判断得出依次次最小直的索引
            if l[min_index][handler] > l[j][handler]:
                min_index = j
        l[i], l[min_index] = l[min_index], l[i]  ####l[i] 中存放最小的值aa
    return l

i = 1
while i < 4:
    username = input("请输入用户名：")
    users = fhandler_r()
    is_exists = 0
    for user in users:
        if username == user["name"]:
            current_pwd = user["pwd"]
            is_exists = 1
            break

    if is_exists:

        n = 3
        is_logined = 0
        while n>0:
            password = input("请输入密码")
            if password == current_pwd:
                is_logined = 1
                break
            else:
                n -= 1
                print("密码不正确请重新输入,还有%s次机会" % n)
                continue

        if is_logined:
            while True:
                action = input('请输入操作(find/list/add/delete/update/exit):')
                a = handlerUser(action=action)
                if a:
                    break
                else:
                    continue

    else:
        print("用户名不存在,请重新输入,剩下%s次机会尝试登陆" %(3-i))
        i += 1
        continue




