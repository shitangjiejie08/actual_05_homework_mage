from django.shortcuts import render

# Create your views here.

from . import models

from django.http import HttpResponseRedirect

def index(request):

	print (models.get_messages())

	context = {'messages' : models.get_messages()}	

	return render(request,'online/index.html',context)


def create(request):
	
	return render(request,'online/create.html')


def save(request):
	
	print(request.GET)
	print(request.POST)

	username = request.GET.get('username','')
	title = request.GET.get('title','')
	content = request.GET.get('content','')

	print(username,title,content)

	models.save_message(username,title,content)

	return HttpResponseRedirect('/online/')
	#pass
