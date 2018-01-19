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
import MySQLdb
from MySQLdb.cursors import DictCursor

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

MESSAGE_FILE = 'messages.json'
HOST = '127.0.0.1'
PORT = 3306
USER = 'root'
PASSWD = ''
CHARSET = 'utf8'
DB = 'huangyisan'

SQL_USER_LOGIN = 'select id,username,age,tel from user where username=%s and password=md5(%s)'
SQL_USER_LIST = 'select id,username,age,tel from user'
SQL_USER_SINGLE = 'select username,age,tel,password from user where username=%s'
SQL_USER_DELETE = 'delete from user where username=%s'
SQL_USER_ADD = 'insert into user (username,age,tel,password) values(%s,%s,%s,md5(%s))'
SQL_USER_UPDATE = 'update user set age=%s,tel=%s,password=%s where username=%s'
SQL_USER_EXIST_JUDEG = 'select count(username) from user where username=%s' 
SQL_USER_EXIST_COUNT= 'select count(*) from user' 

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
    conn = MySQLdb.connect(host=HOST,port=PORT, user=USER, passwd=PASSWD, db=DB, charset=CHARSET)
    #使用dict存储，之后用于添加session
    cur = conn.cursor(DictCursor)
    cur.execute(SQL_USER_LOGIN,(name,password))
    line= cur.fetchone()
    cur.close()
    conn.close()
    return line
    '''
    users = load_users(path)
    for user in users.values():
        if user['name'] == name and user['password'] == password:
            return True
    return False
    '''


def get_messages():
    conn = MySQLdb.connect(host=HOST,port=PORT, user=USER, passwd=PASSWD, db=DB, charset=CHARSET)
    cur = conn.cursor(DictCursor)
    cur.execute(SQL_USER_LIST)
    rt_list = cur.fetchall()
    cur.close()
    conn.close()
    #print('数据库信息输出：',rt_list,type(rt_list))
    return rt_list
    '''
    fhandler = open(path,'rt')
    cxt = fhandler.read()
    fhandler.close()
    return json.loads(cxt)
    '''

def get_single_message(username):
    conn = MySQLdb.connect(host=HOST,port=PORT, user=USER, passwd=PASSWD, db=DB, charset=CHARSET)
    cur = conn.cursor(DictCursor)
    cur.execute(SQL_USER_SINGLE,(username,))
    rt_list = cur.fetchall()
    cur.close()
    conn.close()
    return rt_list

def get_exist_users_count():
    conn = MySQLdb.connect(host=HOST,port=PORT, user=USER, passwd=PASSWD, db=DB, charset=CHARSET)
    cur = conn.cursor()
    cur.execute(SQL_USER_EXIST_COUNT)
    rt_list = cur.fetchone()[0]
    cur.close()
    conn.close()
    return rt_list

def judege_user_exist(username):
    conn = MySQLdb.connect(host=HOST,port=PORT, user=USER, passwd=PASSWD, db=DB, charset=CHARSET)
    cur = conn.cursor()
    cur.execute(SQL_USER_EXIST_JUDEG,(username,))
    rt_list = cur.fetchone()[0]
    cur.close()
    conn.close()
    print('rt_list',rt_list)
    return rt_list

def save_message(username,title,content):
    messages = get_messages()
    messages.append({"username":username,"title":title,"content":content,"publish_date":""})
    fhandler = open(path,'wt')
    fhandler.write(json.dumps(messages))
    fhandler.close()
    return True

def add_user(username,age,tel,password):
    conn = MySQLdb.connect(host=HOST,port=PORT, user=USER, passwd=PASSWD, db=DB, charset=CHARSET)
    cur = conn.cursor()
    cur.execute(SQL_USER_ADD,(username,age,tel,password))
    conn.commit()
    cur.close()
    conn.close()
    

def delete_user(username):
    '''
    users = load_users(path)
    users.pop(name, None)
    dump_users(path,users)
    '''
    conn = MySQLdb.connect(host=HOST,port=PORT, user=USER, passwd=PASSWD, db=DB, charset=CHARSET)
    cur = conn.cursor(DictCursor)
    cur.execute(SQL_USER_DELETE,(username,))
    conn.commit()
    cur.close()
    conn.close()

def modify_user( age, tel, password, username):
    conn = MySQLdb.connect(host=HOST,port=PORT, user=USER, passwd=PASSWD, db=DB, charset=CHARSET)
    cur = conn.cursor()
    cur.execute(SQL_USER_UPDATE,(age,tel,password,username))
    conn.commit()
    cur.close()
    conn.close()


