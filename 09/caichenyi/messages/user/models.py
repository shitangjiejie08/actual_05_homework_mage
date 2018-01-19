#encoding: utf-8

# import json
#
# from utils import dbutil
#
# SQL_USER_LOGIN = 'select id, username, age, tel from user where username=%s and password=md5(%s)'
# SQL_USER_LIST = 'select id, username, age, tel from user'
# SQL_USER_DELETE = 'delete from user where id=%s'
# SQL_USER_FIND_BY_NAME = 'select * from user where username=%s'
# SQL_USER_CREATE = 'insert into user(username, age, tel, password) values (%s, %s, %s, md5(%s))'
# SQL_USER_FIND_BY_ID = 'select * from user where id=%s'
# SQL_USER_MODIFY = 'update user set username=%s, age=%s, tel=%s where id=%s'
# SQL_USER_MODIFY_PASSWORD = 'update user set password=md5(%s) where id=%s'
#
# def validate_login(name, password):
#     return dbutil.execute_fetch(SQL_USER_LOGIN, (name, password), True)
#
# def get_users():
#     return dbutil.execute_fetch(SQL_USER_LIST)
#
#
# def validate_add_user(name, age, tel, password):
#     if len(name) < 0 or len(name) > 8:
#         return False, '用户名必须在0到8个字符之间'
#
#     if not(age.isdigit() and int(age) > 0 and int(age) < 100):
#         return False, '年龄必须是1到100的整数'
#
#     #从数据库中根据名称查询，如果查询到就名字重复
#
#     user = get_user_by_username(name)
#     if user:
#         return False, '添加用户失败, 失败原因: 用户名已存在'
#
#     return True, ''
#
#
# def get_user_by_username(username):
#     return dbutil.execute_fetch(SQL_USER_FIND_BY_NAME, (username, ), True)
#
#
# def add_user(name, age, tel, password):
#     dbutil.execute_commit(SQL_USER_CREATE, (name, age, tel, password))
#
#
# def delete_user(uid):
#     dbutil.execute_commit(SQL_USER_DELETE, (uid,))
#
#
# def get_user_by_id(uid):
#     return dbutil.execute_fetch(SQL_USER_FIND_BY_ID, (uid, ), True)
#
#
# def validate_modify_user(uid, name, age, tel):
#     user = get_user_by_id(uid)
#     if user is None:
#         return False, '用户不存在'
#
#     user = get_user_by_username(name)
#     if user and user['id'] != int(uid):
#         return False, '用户名已存在'
#
#     if not(age.isdigit() and int(age) > 0 and int(age) < 100):
#         return False, '年龄必须是1到100的整数'
#
#     return True, ''
#
#
# def modify_user(uid, name, age, tel):
#     dbutil.execute_commit(SQL_USER_MODIFY, (name, age, tel, uid))
#
# def validate_modify_password(uid, name, age, tel, password):
#     if len(password) < 8:
#         return False, '密码长度需要大于8位'
#     else:
#         return True, ''
#
# def modify_password(uid, password):
#     dbutil.execute_commit(SQL_USER_MODIFY_PASSWORD, (password, uid))

import json

from utils import dbutil

class User(object):

    SQL_USER_LOGIN = 'select id, username, age, tel from user where username=%s and password=md5(%s)'
    SQL_USER_LIST = 'select id, username, age, tel from user'
    SQL_USER_CREATE = 'insert into user(username, age, tel, password) values (%s, %s, %s, md5(%s))'
    SQL_USER_DELETE = 'delete from user where id=%s'
    SQL_USER_FIND_BY_ID = 'select * from user where id=%s'
    SQL_USER_MODIFY = 'update user set username=%s, age=%s, tel=%s where id=%s'
    SQL_USER_MODIFY_PASSWORD = 'update user set password=md5(%s) where id=%s'
    SQL_USER_FIND_BY_NAME = 'select * from user where username=%s'

    def __init__(self, id=None, username=None, password=None, age=None, tel=None):
        self.id = id
        self.username = username
        self.password = password
        self.age = age
        self.tel = tel

    @classmethod
    def all(cls):
        users = []
        lines = dbutil.execute_fetch(cls.SQL_USER_LIST)
        for user in lines:
            obj = User(id=user['id'], username=user['username'], age=user['age'], tel=user['tel'])
            users.append(obj)
        return users

    def login(self):
        args = (self.username, self.password)
        return dbutil.execute_fetch(self.SQL_USER_LOGIN, args, True)

    def find(self):
        args = (self.id,)
        user = dbutil.execute_fetch(self.SQL_USER_FIND_BY_ID, args, True)
        return user

    def create(self):
        args = (self.username, self.age, self.tel, self.password)
        dbutil.execute_commit(self.SQL_USER_CREATE, args)

    def delete(self):
        args = (self.id)
        print(args)
        dbutil.execute_commit(self.SQL_USER_DELETE, args)

    def modify_user(self):
        args = (self.username, self.age, self.tel, self.id)
        dbutil.execute_commit(self.SQL_USER_MODIFY, args)

    def modify_password(self):
        args = (self.password, self.id)
        dbutil.execute_commit(self.SQL_USER_MODIFY_PASSWORD, args)

    @staticmethod
    def __get_user_by_username(username):
        args = (username,)
        return dbutil.execute_fetch(SQL_USER_FIND_BY_NAME, args, True)

    def validate_add_user(self):
        if len(self.username) < 0 or len(self.username) > 8:
            return False, '用户名必须在0到8个字符之间'
        if len(self.password) < 8:
            return False, '密码必须大于8位'
        if not (self.age.isdigit() and int(self.age) > 0 and int(self.age) < 100):
            return False, '年龄必须是1到100的整数'
        if self.__get_user_by_username(self.username):
            return False, '添加用户失败, 失败原因: 用户名已存在'
        return True, ''

    def get_user_by_id(self):
        args = (self.id,)
        return dbutil.execute_fetch(self.SQL_USER_FIND_BY_ID, args, True)

    def validate_modify_user(self):
        if self.get_user_by_id() is None:
            return False, '用户不存在'
        user = self.__get_user_by_username(self.username)
        if user and user['id'] != int(self.id):
            return False, '用户名已存在'
        if not(self.age.isdigit() and int(self.age) > 0 and int(self.age) < 100):
            return False, '年龄必须是1到100的整数'
        return True, ''

    def validate_modify_password(self):
        if len(self.password) < 8:
            return False, '密码长度需要大于8位'
        else:
            return True, ''
