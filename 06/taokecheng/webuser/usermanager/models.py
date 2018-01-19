from django.db import models
# Create your models here.
import json
USER_FILE = 'users.json'
def get_users():
	fhandler = open(USER_FILE,'rt')
	cxt = fhandler.read()
	fhandler.close()
	json_data = json.loads(cxt)
	return json_data

def save_user(username,age,tel,password,mtime,users):
	if username:
		user = {"username":username,"age":age,"tel":tel,'password':password,'mtime':mtime}
		users.append(user)
	fhandler = open(USER_FILE,'w')
	fhandler.write(json.dumps(users))
	fhandler.close()
	return  True

def check_user_add(name, age, tel, password, users):
	if len(name) < 0 or len(name) > 8:
	    msg = '错误！用户名必须在0到8个字符之间。'
	    status = False
	elif not(age.isdigit() and int(age) > 0 and int(age) < 150):
	    msg = '错误！年龄必须是1到150的整数。'
	    status = False
	elif name in [ u['username'] for u in users ]:
	    msg = '添加用户失败, 失败原因: 用户名已存在。'
	    status = False
	else:
		msg = ''
		status = True
	return msg,status


def check_update_user(name, age, tel, password, users):
	name_list = [u['username'] for u in users]
	user_index = None
	if not name in name_list:
		msg = '更新用户失败, 失败原因: 用户不存在。'
		status = False
		return msg, status,user_index
	else:
		user_index = name_list.index(name)
	if len(name) < 0 or len(name) > 8:
	    msg = '错误！用户名必须在0到8个字符之间。'
	    status = False
	elif not(age.isdigit() and int(age) > 0 and int(age) < 150):
	    msg = '错误！年龄必须是1到150的整数。'
	    status = False
	else:
		msg = ''
		status = True
	return msg,status,user_index

def check_del_user(name,users):
	user_index = None
	name_list = [ u['username'] for u in users ]
	if not name in name_list :
		msg = '删除用户失败, 失败原因: 用户不存在。'
		status = False
	else:
		msg = '删除用户成功！'
		user_index = name_list.index(name)
		status = True
	return msg,status,user_index

def del_user(user_index,users):
	print('Userdel:::{}{}'.format(user_index,type(users)))
	users.pop(user_index)
	return users

#排序
def sort_user(sort_type, users):
	listData = users
	if sort_type == 'username':
		listData.sort(key=lambda x: x[sort_type])
	else:
		listData.sort(key=lambda x: int(x[sort_type]))
	return listData

#搜索
def search_user(search_name,users):
	name_list = [u['username'] for u in users]
	search_rs = []
	for name in name_list:
		if name.find(search_name) != -1:
			user_index = name_list.index(name)
			search_rs.append(users[user_index])

	return search_rs

#登录认证
def validate_login(username, password, users):
	users_list = [u for u in users]
	for user in users_list:
		if user['username'] == username and user['password'] == password:
			return True

	return False
