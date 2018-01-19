#!/usr/bin/env python3
#coding=utf-8
"""
# Author: huangyisan
# Created Time : 六  5/13 12:19:16 2017
# File Name: models.py
# Description:

"""
#encoding: utf-8

import json

'''
1. 每一个用户存储信息修改为字典
{
    xx : {name : xxx, age : xxxx, tel: xxx, 'password' : 'xxx'},
    xxx: {}
}
2. 用户输入了三次，修改为一次，使用:分隔用户信息
3. 查找的时候使用包含关系，name包含查找的字符串
'''

path = 'users.txt'


def load_users(path):
    fhandler = open(path, 'rt')
    users = json.loads(fhandler.read())
    fhandler.close()
    return users

def dump_users(path, users):
    fhandler = open(path, 'wt')
    fhandler.write(json.dumps(users))
    fhandler.close()


def validate_login(name, password):
    users = load_users(path)
    for user in users.values():
        if user['name'] == name and user['password'] == password:
            return True
    return False

def get_messages():
    fhandler = open(path,'rt')
    cxt = fhandler.read()
    fhandler.close()
    return json.loads(cxt)

def save_message(username,title,content):
    messages = get_messages()
    messages.append({"username":username,"title":title,"content":content,"publish_date":""})
    fhandler = open(path,'wt')
    fhandler.write(json.dumps(messages))
    fhandler.close()
    return True

def delete_user(name):
    users = load_users(path)
    users.pop(name, None)
    dump_users(path,users)

def modify_user(name, age, tel, password, users):
    users[name] = {'name' : name, 'age' : age, 'tel' : tel, 'password' : password}
    dump_users(path,users)

