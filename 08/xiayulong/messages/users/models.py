from django.db import models

# Create your models here.

# encoding: utf-8
import os
import getpass
import copy
import json
import MySQLdb
from MySQLdb.cursors import DictCursor

user = 'root'
passwd = 'redhat'
host = '127.0.0.1'
db = 'message'
login_sql = 'select * from tbl_user where name = %s and passwd = md5(%s)'
show_users_sql = 'select * from tbl_user'
del_user_sql = 'delete from tbl_user where name = %s'
add_user_sql = 'insert into tbl_user(name,age,tel,passwd) values(%s,%s,%s,md5(%s))'
update_user_passwd_sql = 'update tbl_user set passwd = md5(%s) where name = %s and passwd = md5(%s)'

def mymap(a,b):
    return (a,b)



# initializing global variable "users"
def init_users(path):
    #global users
    f = open(path)
    str_json = f.read()
    users = json.loads(str_json)

    f.close()
    return users

# authenticating users
def auth_user():
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
    return valid 

def auth_user_v2(username,password):
    valid = False
    conn = MySQLdb.connect(host=host,user=user,passwd=passwd,db=db,charset='utf8')
    cursor = conn.cursor()
    result = cursor.execute(login_sql,(username,password))
    if result != 0 :
        valid = True
    cursor.close()
    conn.close()
    return valid    

def show_users():
    conn = MySQLdb.connect(host=host,user=user,passwd=passwd,db=db,charset='utf8')
    cursor = conn.cursor(DictCursor)
    cursor.execute(show_users_sql)
    users = cursor.fetchall()
    cursor.close()
    conn.close()
    print(users)
    return users

# adding user
def add_user(info_list,users):
    '''
    return n:
             0: successfully
             1: user_exists
             2: information user input does not match the format like "Tony:22:12345678"
    '''
    if len(info_list) != 3:
        print("输入信息不匹配要求，添加失败！")
        return 2
    if info_list[0] not in users:
        passwd = getpass.getpass("请设置密码：")
        info_list.append(passwd)
        users[info_list[0]] = dict(map(mymap,("name","age","tel","passwd"),info_list))
        return 0
    else:
        print("用户已存在,添加失败")
        return 1

def add_user_v2(user_info):
    conn = MySQLdb.connect(host=host,user=user,passwd=passwd,db=db,charset='utf8')    
    cursor = conn.cursor()
    cursor.execute(add_user_sql,(user_info["name"],user_info["age"],user_info["tel"],user_info["passwd"]))
    conn.commit()
    cursor.close()
    conn.close()
    return users 

# deleting user
def del_user(name):
    conn = MySQLdb.connect(host=host,user=user,passwd=passwd,db=db,charset='utf8')
    cursor = conn.cursor()
    cursor.execute(del_user_sql,(name,))
    conn.commit()
    cursor.close()
    conn.close()

# updating user
def update_user(info_list,users):
    if len(info_list) != 3:
        print("输入信息不匹配要求，更新失败！")
        return "err_info",1
    if info_list[0] in users:
        passwd = getpass.getpass("请设置密码：")
        info_list.append(passwd)
        users[info_list[0]] = dict(map(mymap,("name","age","tel","passwd"),info_list))
        print("更新成功！")
        return "successfully",0
    else:
        print("用户不存在,更新失败!") 
        return "user_not_exist",1

def update_user_v2(user_info):
    conn = MySQLdb.connect(host=host,user=user,passwd=passwd,db=db,charset='utf8')
    cursor = conn.cursor()
    if user_info.get("tel") is not None:
        cursor.execute("update tbl_user set tel = %s where name = %s",(user_info["tel"],user_info["name"]))
    if user_info.get("age") is not None:
        cursor.execute("update tbl_user set age = %s where name = %s",(user_info["age"],user_info["name"]))
    conn.commit()
    cursor.close()
    conn.close()

def update_user_passwd(user_info):
    conn = MySQLdb.connect(host=host,user=user,passwd=passwd,db=db,charset='utf8')
    cursor = conn.cursor()
    cursor.execute(update_user_passwd_sql,(user_info['new_passwd'],user_info['name'],user_info['old_passwd']))
    conn.commit()
    cursor.close()
    conn.close()


# finding user
def find_user(name,users):
    if name in users:
        print("用户信息如下：")
        for k,v in users[name].items():
            print("{0:<10}:{1:<10}".format(k,v))
        return "successfully",0
    else:
        print("用户不存在")
        return "user_not_exist",1

def find_user_v2(name):
    conn = MySQLdb.connect(host=host,user=user,passwd=passwd,db=db,charset='utf8')
    cursor = conn.cursor(DictCursor)
    cursor.execute("select name from tbl_user where name = %s",(name,))
    user_info = cursor.fetchall()[0]
    cursor.close()
    conn.close()
    return user_info

# sort_key
def sort_key(x):
    if sorted_field == "age":
        return int(x[sorted_field])
    else:
        return x[sorted_field]


# save user info in json to file
def save_json(path,users):
    fd = open(path+".temp","w")
    fd.write(json.dumps(users))
    fd.close()
    os.rename(path+".temp",path)

users = {}
"""{"xxx":{"name":"xxx","age":18,"tel":"11234567890","passwd":"abc"},"yyy":{"name":"yyy","age":18,"tel":"11234567890","passwd":"abc"}}"""

users = init_users("/data/code/users.txt")


def main():
    if not auth_user():
        print("验证次数超过限制，程序退出")
    else:
        while True:
            action = input("Your input (add/delete/update/find/list/exit)")
            action = action.lower()
            if action == "add":
                info = input("请输入用户名、年龄、电话，并且用英文冒号分隔，例如 Tony:22:12345678  ")
                info = info.strip()
                info_list = info.split(":")
                add_user(info_list,users)


            elif action == "delete":
                name = input("请输入删除的用户名：")
                del_user(name,users)


            elif action == "update":
                info = input("请输入将要更新的用户名、年龄、电话，并且用英文冒号分隔，例如 Tony:22:12345678  ")
                info = info.strip()
                info_list = info.split(":")
                update_user(info_list,users)

            elif action == "find":
                name = input("请输入查找的用户名：")
                find_user(name,users)

            elif action == "list":
                sorted_field = input("希望按照哪一列升序列出(name,age,tel)")
                users_list = list(users.values())
                print(users_list)
                users_list.sort(key=sort_key) #sort_key is above
                print("用户信息\n用户名:\t年龄:\t电话:\t密码:")
                for i in range(len(users_list)):
                    print("{0}\t{1}\t{2}\t{3}".format(users_list[i]["name"],users_list[i]["age"],users_list[i]["tel"],"*"*len(users_list[i]["passwd"])))
                    print()
            elif action == "exit":
                save_json("/data/code/users.txt",users)
                break
            else:
                print("输入有误")

print(__name__)
if __name__ == '__main__':
    main()
