from django.shortcuts import render
from django.shortcuts import render, render_to_response
from django.http import HttpResponse,HttpResponseRedirect

# Create your views here.
from usermanager.models  import *

def index(requst):
	return render(requst,'webuser/login.html')
def home(requst):
	if requst.method == 'POST':
		users = get_users()
		username = requst.POST.get('username','')
		password = requst.POST.get('password', '')
		status = validate_login(username,password,users)
		if status:
			return render(requst,'webuser/home.html')
		else:
			return HttpResponse('{} <br><br><a href="/">返回登录页面</a>'.format('用户名或密码错误！'))
	else:
		return render(requst, 'webuser/home.html')

def register(requst):
	return render(requst,'webuser/register.html')
