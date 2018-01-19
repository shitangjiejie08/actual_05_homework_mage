#encoding: utf-8

import json
import hashlib
import MySQLdb
from MySQLdb.cursors import DictCursor

HOST = '127.0.0.1'
PORT = 3306
DB = 'dk1'
USER = 'root'
PASSWD = 'cstorfs'
CHARSET = 'utf8'

SQL_USER_LOGIN = 'select id,username,age,tel from user where username=%s and password=%s;'
SQL_USER_LIST = 'select id,username,age,tel from user;'
SQL_USER_DELETE = 'delete from user where id=%s;'
SQL_USER_INSERT = 'insert into user(username, password, age, tel) values(%s, %s, %s, %s);'
SQL_USER_GET = 'select id,username,password,age,tel from user where id=%s;'
SQL_USER_UPDATE = 'update user set age=%s,tel=%s where username=%s;'
SQL_PASSWD_UPDATE = 'update user set password=%s where id=%s;'

def strmd5(passwd):
    m = hashlib.md5()
    m.update(passwd.encode('utf-8'))
    return m.hexdigest()

def validate_login(name, password):
    conn = MySQLdb.connect(host=HOST, port=PORT, user=USER, passwd=PASSWD, db=DB, charset=CHARSET)
    cur = conn.cursor(DictCursor)
    cur.execute(SQL_USER_LOGIN, (name, password))
    line = cur.fetchone()
    cur.close()
    conn.close()
    print(line)
    return line

def get_users():
    conn = MySQLdb.connect(host=HOST, port=PORT, user=USER, passwd=PASSWD, db=DB, charset=CHARSET)
    cur = conn.cursor(DictCursor)
    cur.execute(SQL_USER_LIST)
    rt_list = cur.fetchall()
    cur.close()
    conn.close()
    print(rt_list)
    return rt_list

def delete_user(uid):
    conn = MySQLdb.connect(host=HOST, port=PORT, user=USER, passwd=PASSWD, db=DB, charset=CHARSET)
    cur = conn.cursor()
    cur.execute(SQL_USER_DELETE, (uid,))
    conn.commit()
    cur.close()
    conn.close()

def validate_add_user(name, age, tel, password):
    if len(name) < 0 or len(name) > 8:
        return False, '用户名必须在0到8个字符之间'

    if not(age.isdigit() and int(age) > 0 and int(age) < 100):
        return False, '年龄必须是1到100的整数'

    users = get_users()
    if name in [user['username'] for user in users]:
        return False, '添加用户失败, 失败原因: 用户名已存在'

    return True, ''

def add_user(name, age, tel, password):
    conn = MySQLdb.connect(host=HOST, port=PORT, user=USER, passwd=PASSWD, db=DB, charset=CHARSET)
    cur = conn.cursor()
    cur.execute(SQL_USER_INSERT, (name, password, age, tel))
    conn.commit()
    cur.close()
    conn.close()
    
def get_user_by_id(uid):
    conn = MySQLdb.connect(host=HOST, port=PORT, user=USER, passwd=PASSWD, db=DB, charset=CHARSET)
    cur = conn.cursor(DictCursor)
    cur.execute(SQL_USER_GET, (uid,))
    user = cur.fetchone()
    cur.close()
    conn.close()
    print(user)
    return user
    
def validate_modify_user(name, age, tel):
    users = get_users()
    if name not in [user['username'] for user in users]:
        return False, '更新用户失败, 失败原因: 用户名不存在'

    if not(age.isdigit() and int(age) > 0 and int(age) < 100):
        return False, '年龄必须是1到100的整数'

    return True, ''

def modify_user(name, age, tel):
    conn = MySQLdb.connect(host=HOST, port=PORT, user=USER, passwd=PASSWD, db=DB, charset=CHARSET)
    cur = conn.cursor()
    cur.execute(SQL_USER_UPDATE, (age, tel, name))
    conn.commit()
    cur.close()
    conn.close()

def validate_modify_password(passwd):
    if len(passwd) < 8:
        return False, '密码长度必须大于等于8个字符'
    
    return True, ''    

def modify_password(uid, passwd):
    conn = MySQLdb.connect(host=HOST, port=PORT, user=USER, passwd=PASSWD, db=DB, charset=CHARSET)
    cur = conn.cursor()
    cur.execute(SQL_PASSWD_UPDATE, (passwd, uid))
    conn.commit()
    cur.close()
    conn.close()


