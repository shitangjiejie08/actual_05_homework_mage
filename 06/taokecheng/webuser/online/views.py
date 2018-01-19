# Create your views here.
from django.shortcuts import render, render_to_response
from django.http import HttpResponse,HttpResponseRedirect
from .models  import *
import time,datetime
def index(requst):
#	print(get_messages())
	context = {'messages':get_messages()}
#	context = {}
	return render(requst,'online/index.html',context)

def create(requst):
	return render(requst,'online/create.html')

def save(request):
	username = request.POST.get('username','')
	title = request.POST.get('title','')
	content = request.POST.get('content','')
	publish_date = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
	#publish_date = time.strftime('%Y-%m-%d %H:%M:%S',time.localtime())
	text = '{}:{}:{}:{}'.format(publish_date,username,title,content)
	print(text)
	save_message(publish_date,username,title,content)
	return HttpResponseRedirect('/online/')
#	return HttpResponse(text)

