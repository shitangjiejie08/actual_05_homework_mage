from django.db import models
import MySQLdb
from MySQLdb.cursors import DictCursor

# 将sql连接写到一个py文件中
from . import exec_sql

# Create your models here.


# 读取用户列表
def load_users():
    SQL_USER_LIST = 'select id,username,age,tel,password from tb_user'
    rt = exec_sql.exec_select(SQL_USER_LIST)
    return rt

# login
def validate_login(name, password):
    SQL_USER_LOGIN="select id,username from tb_user where username='"+name+"' and password=md5('"+password+"')"
    rt = exec_sql.exec_select(SQL_USER_LOGIN)
    return rt

# add user
def add_user(username, age, tel, password):
    SQL_USER_INSERT="insert into tb_user(username,age,tel,password) values('"+username+"','"+age+"','"+tel+"',md5('"+password+"'))"
    rt = exec_sql.exec_execute(SQL_USER_INSERT)
    return rt
'''
添加用户时验证信息
return True/False, ''
'''
def validate_add_user(username, age, tel, password):
    users = load_users()
    if len(username) < 0 or len(username) > 8:
        return False, '用户名必须在0到8个字符之间'

    if not(age.isdigit() and int(age) > 0 and int(age) < 100):
        return False, '年龄必须是1到100的整数'
    for user in users:
        if username in user["username"]:
            return False, '添加用户失败, 失败原因: 用户名已存在'
    return True, ''

# 修改信息前先根据uid获取用户信息
def get_user_info(uid):
    SQL_GET_USER_UPDATE_INFO="select id,username,age,tel from tb_user where id = '"+str(uid)+"'"
    rt = exec_sql.exec_select(SQL_GET_USER_UPDATE_INFO)
    return rt


# 修改信息验证
def validate_modify_user(name, age, tel, password):
    users = load_users()
    if name not in users:
        return False, '更新用户失败, 错误原因: 用户名不存在'


    if not(age.isdigit() and int(age) > 0 and int(age) < 100):
        return False, '年龄必须是1到100的整数'
    return True, ''
# 修改信息
def modify_user(age, tel,uid):
    SQL_USER_UPDATE="update tb_user set age='"+age+"',tel='"+tel+"' where id = '"+str(uid)+"'"
    rt = exec_sql.exec_execute(SQL_USER_UPDATE)
    return rt

# 旧密码验证
def validate_old_pass(old_pass,uid):
    SQL_USER_OLD_PASS="select password from tb_user where id='"+str(uid)+"' and password=md5('"+old_pass+"')"
    rt = exec_sql.exec_select(SQL_USER_OLD_PASS)
    if rt:
        return True, ''
    else:
        return False, '旧密码验证失败！'

# 新密码验证
def validate_pass(new_pass,confirm_pass):
    if len(new_pass) < 6 or len(new_pass)>16:
        return False, '密码长度必须位6-16个字符'
    if new_pass != confirm_pass:
        return False, '两次输入密码不一致！'
    return True, ''

# 修改密码
def edit_pass(new_pass,uid):
    SQL_USER_UPDATE_PASS="update tb_user set password=md5('"+new_pass+"') where id='"+str(uid)+"'"
    rt = exec_sql.exec_execute(SQL_USER_UPDATE_PASS)
    return rt

# 删除
def delete_user(uid):
    SQL_USER_DELETE="delete from tb_user where id = '"+str(uid)+"'"
    rt = exec_sql.exec_execute(SQL_USER_DELETE)
    return True
