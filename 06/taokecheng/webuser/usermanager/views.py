from django.shortcuts import render, render_to_response
from django.http import HttpResponse,HttpResponseRedirect
from .models  import *
import time,datetime

# Create your views here.

def index(requst):
	users = get_users()
	for user in users:
		user['password'] = '*' * len(user['password'])
	list_msg = '用户列表信息：'
	if requst.method == 'POST':
		sort_type =  requst.POST.get('sort_type')
		search_name = requst.POST.get('search_name')
		if sort_type:
			users = sort_user(sort_type,users)
			list_msg = '用户排序后的列表信息：'
		elif search_name:
			users = search_user(search_name, users)
			list_msg = '搜索到的用户列表信息：'

	if users:
		context = {'users': users,'list_msg':list_msg}
	else:
		context = {'error': True}
	return render(requst, 'usermanager/index.html', context)

def add(requst):
	context = {'action':'添加用户','type':'add_user'}
	return render(requst, 'usermanager/add.html',context)
def addUser(requst):
	users = get_users()
	username = requst.POST.get('username','')
	age = requst.POST.get('age','')
	tel = requst.POST.get('tel','')
	password = requst.POST.get('password','')
	action = requst.POST.get('action','')
	mtime = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
	# publish_date = time.strftime('%Y-%m-%d %H:%M:%S',time.localtime())
	print('更新用户或者添加用户',action)
	print('#############',username,age,tel,password,action)
	if action == 'add_user':
		msg,status = check_user_add(username, age, tel, password, users)
		action_msg = '添加用户成功!'
	elif action == 'update_user':
		msg,status,user_index = check_update_user(username, age, tel, password, users)

	if status :
		if action == 'add_user':
			save_user(username,age,tel,password,mtime,users)
		elif action == 'update_user':
			users[user_index] = {'username':username,'age':age,'password':password,'tel':tel,'mtime':mtime}
			action_msg = '更新用户成功!'
			save_user(None, None, None, None, None, users)
		return HttpResponse('{} <br><br><a href="index.html">返回用户主页</a>'.format(action_msg))
	else:
		return HttpResponse(msg+'<br><br><a href="index.html">返回用户主页</a>')


def delete(requst):
	return render(requst,'usermanager/delete.html')

def delUser(requst):
	users = get_users()
	username = requst.POST.get('username','')
	msg,status,user_index = check_del_user(username,users)
	if status :
		users = del_user(user_index,users)
		save_user(None,None,None,None,None, users)
	return HttpResponse('{} <br><br><a href="index.html">返回用户主页</a>'.format(msg))

def listUser(requst):
 	return render(requst,'usermanager/list.html')

def update(requst):
	context = {'action': '更新用户', 'type': 'update_user'}
	return render(requst, 'usermanager/add.html',context)

def search(requst):
	return render(requst,'usermanager/search.html')



