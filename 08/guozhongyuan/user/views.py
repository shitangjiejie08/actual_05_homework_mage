from django.shortcuts import render


from . import models

from django.http import HttpResponse ,HttpResponseRedirect
# Create your views here.

def require_login(request):
	return render(request,'user/login.html')

def login(request):
	
	username = request.POST.get('username','')
	password = request.POST.get('password','')
	print (username,password)
	print (models.validate_login(username,password))

	#return HttpResponse('login')

	rt = models.validate_login(username, password)
	if rt:
		#return HttpResponse('success')
		return HttpResponseRedirect('/user/list_user/')
	else:
		context = {'error' : '用户名或密码错误', 'username' : username, 'password' : password}
		return render(request, 'user/login.html', context)


def list_user(request):

	#文件
	#users = models.load_users(models.path)
	#数据库
	users = models.load_user_db()
	print (users)
	print ('--------view------------')
	users = list(users.values())

	return render(request,'user/list.html',{'users':users})

def delete_user(request):
	name = request.GET.get('name','')
	print (name)
	models.delete_user(name)
	return HttpResponseRedirect('/user/list_user/')	


#创建用户
def create_user(request):
	return render(request, 'user/create.html')


#保存用户
def save_user(request):
	username = request.POST.get('username', '')
	password = request.POST.get('password', '')
	age = request.POST.get('age', '')
	tel = request.POST.get('tel', '')

        #rt    返回 true false
	#error 返回 报错内容
	rt, error = models.validate_add_user(username, age, tel, password)
	if rt:
        #验证成功
		#models.add_user(username, age, tel, password)
                #修改为调用数据库
		models.save_user_db(username,password,age,tel)
		return HttpResponseRedirect('/user/list_user/')
	else:
		context = {}
		context['error'] = error
		context['username'] = username
		context['password'] = password
		context['age'] = age
		context['tel'] = tel

		return render(request, 'user/create.html', context)

#
def view_user(request):
	username = request.GET.get('name', '')
	user = models.get_user_by_name(username)
	return render(request, 'user/view.html', user)



#编辑用户
def modify_user(request):
	username = request.POST.get('username', '')
	password = request.POST.get('password', '')
	age = request.POST.get('age', '')
	tel = request.POST.get('tel', '')

	rt, error = models.validate_modify_user(username, age, tel, password)
	if rt:
        #验证成功
		models.modify_user(username, age, tel, password)
		return HttpResponseRedirect('/user/list_user/')
	else:
		context = {}
		context['error'] = error
		context['name'] = username
		context['password'] = password
		context['age'] = age
		context['tel'] = tel

		return render(request, 'user/view.html', context)














