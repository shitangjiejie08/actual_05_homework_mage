from django.db import models

# Create your models here.

# encoding: utf-8
import os
import getpass
import copy
import json
import MySQLdb
from MySQLdb.cursors import DictCursor


from django.db import models
from .utils import mycrypt
from django.core.exceptions import ObjectDoesNotExist


class users(models.Model):
    name = models.CharField(max_length=255,null=True) 
    age = models.SmallIntegerField(null=True)
    tel = models.CharField(max_length=32,null=True)
    passwd = models.CharField(max_length=32,null=True)

    def as_dict(self):
        return {"name": self.name, "age": self.age, "tel": self.tel}

    def __str__(self):
        tpl = "name : {name}, age : {age}, tel : {tel}, passwd : {passwd}"
        return tpl.format(name=self.name,age=self.age,tel=self.tel,passwd=self.passwd)




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




def auth_user_v2(username,password):
    valid = False
    try:
        users.objects.get(name=username,passwd=mycrypt(password))
    except ObjectDoesNotExist as e:
        print("用户不存在")
        return valid
    valid = True
    return valid    

def show_users():
    dict_users = users.objects.all()
    print(dict_users)
    return dict_users

# adding user
def add_user_v2(user_info):
    new_user = users(name=user_info["name"],age=user_info["age"],tel=user_info["tel"],passwd=mycrypt(user_info["passwd"]))
    new_user.save()

# deleting user
def del_user(name):
    users.objects.filter(name=name).delete()


def update_user_v2(user_info):
    if user_info.get("tel") is not None:
        users.objects.filter(name=user_info['name']).update(tel=user_info["tel"])
    if user_info.get("age") is not None:
        users.objects.filter(name=user_info['name']).update(age=user_info["age"])

def update_user_passwd(user_info):
    users.objects.filter(name=user_info['name'],passwd=mycrypt(user_info['old_passwd'])).update(passwd=mycrypt(user_info['new_passwd']))  


def find_user_v2(name):
    user_info = users.objects.filter(name=name)[0]
    return user_info.name

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


