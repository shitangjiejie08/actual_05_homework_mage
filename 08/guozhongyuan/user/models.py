#encoding: utf-8

import json
import MySQLdb

#使用数据库保存留言板信息
HOST = '127.0.0.1'
PORT = 3306
DB = 'gzy'
USER = 'root'
PASSWD = '123456'
CHARSET = 'utf8'

SQL_USER_LIST_COLUMNS= ['username','password','age','tel']
SQL_USER_LIST = 'select username,password,age,tel from user order by id desc;'
SQL_USER_INSERT = 'insert into user (username,password,age,tel) values( %s, %s, %s, %s)'
SQL_USER_DROP = 'delete from user where username=%s;' 
SQL_USER_UPDATE = 'update user set username=%s,password=%s,age=%s,tel=%s where username=%s;'


path = 'users.txt'

user_info_tpl = '|{0:>20}|{1:>5}|{2:>20}|{3:>20}|'
user_info_header = user_info_tpl.format('name', 'age', 'telephone', 'password')

def load_users(path):
    fhandler = open(path, 'rt')
    users = json.loads(fhandler.read())
    fhandler.close()
    return users

#读取用户列表-数据库
def load_user_db():
    conn = MySQLdb.connect(host=HOST,port=PORT,user=USER,passwd=PASSWD,db=DB,charset=CHARSET)
    cur = conn.cursor()
    cur.execute(SQL_USER_LIST)
    lines = cur.fetchall()
    cur.close()
    conn.close()
    #rt_list = []
    rt_list = {}
    for line in lines:
        message = dict(zip(SQL_USER_LIST_COLUMNS,line))
        print (message)
        print ('----models----')
        rt_list[message['username']]=message
    return rt_list



def dump_users(path, users):
    fhandler = open(path, 'wt')
    fhandler.write(json.dumps(users))
    fhandler.close()

#保存用户信息-数据库
def save_user_db(username,password,age,tel):
    conn = MySQLdb.connect(host=HOST,port=PORT,user=USER,passwd=PASSWD,db=DB,charset=CHARSET)
    cur= conn.cursor()
    cur.execute(SQL_USER_INSERT,(username,password,age,tel))
    conn.commit()
    cur.close()
    conn.close()

#验证用户身份
def validate_login(name, password):
    #users = load_users(path)
    users = load_user_db()
    for user in users.values():
        if user['name'] == name and user['password'] == password:
            return True

    return False


'''
return True/False, ''
'''
#user
def validate_add_user(name, age, tel, password):
    if len(name) < 0 or len(name) > 8:
        return False, '用户名必须在0到8个字符之间'

    if not(age.isdigit() and int(age) > 0 and int(age) < 100):
        return False, '年龄必须是1到100的整数'

    #users = load_users(path)
    users = load_user_db()
    if name in users:
        return False, '添加用户失败, 失败原因: 用户名已存在'

    return True, ''


def add_user(name, age, tel, password):
    users = load_users(path)
    users[name] = {'name' : name, 'age' : age, 'tel' : tel, 'password' : password}
    dump_users(path, users)

def validate_delete_user(name, users):
    user = users.get(name)
    if user:
        return True, ''
    else:
        return False, '删除用户失败, 失败原因: 用户名不存在'

#删除 用户 信息 -数据库
def delete_user(name):
    #users = load_users(path)
    #users.pop(name, None)
    #dump_users(path,users)
    conn = MySQLdb.connect(host=HOST,port=PORT,user=USER,passwd=PASSWD,db=DB,charset=CHARSET)
    cur= conn.cursor()
    cur.execute(SQL_USER_DROP,name)
    conn.commit()
    cur.close()
    conn.close()   

#验证用户名正确性(修改用户时)
def validate_modify_user(name, age, tel, password):
    #users = load_users(path)
    users = load_user_db()
    print (name)
    print (users)
    if name not in users:
        return False, '更新用户失败, 错误原因: 用户名不存在'

    if len(password) < 8:
        return False, '密码长度必须大于等于8个字符'

    if not(age.isdigit() and int(age) > 0 and int(age) < 100):
        return False, '年龄必须是1到100的整数'

    return True, ''

#user修改编辑 user
def modify_user(username, age, tel, password):
    #users = load_users(path)
    #users[name] = {'name' : name, 'age' : age, 'tel' : tel, 'password' : password}
    #dump_users(path, users)
    #save_user_db(username,password,age,tel)

    conn = MySQLdb.connect(host=HOST,port=PORT,user=USER,passwd=PASSWD,db=DB,charset=CHARSET)
    cur= conn.cursor()
    cur.execute(SQL_USER_UPDATE,(username,password,age,tel,username))
    conn.commit()
    cur.close()
    conn.close()



def find_user(name, users):
    rt_list = []
    for user in users.values():
        if user['name'].find(name) != -1:
            rt_list.append(user)

    return rt_list

def list_user(field, users):
    user_list = list(users.values())
    return sorted(user_list, key=lambda x: x.get(field))


#user
def get_user_by_name(name):
    #users = load_users(path)
    users = load_user_db()
    #return users.get(name, {})
    return users.get(name, {})



#if __name__ == '__main__':
#    main()





