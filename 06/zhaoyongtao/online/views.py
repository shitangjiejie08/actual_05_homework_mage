from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect
# Create your views here.
from .models import *

import datetime

def index(request):
    context = {"messages" : get_messages()}
    return render(request,'online/index.html',context) 

def create(request):
    return render(request,'online/create.html')

def save(request):
    publish = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    username = request.GET.get("username")
    title = request.GET.get("title")
    content = request.GET.get("content")
    text = '{}:{}:{}'.format(username,title,content)
    save_messages(publish,username,title,content)
    print(username,title,content)
    return HttpResponseRedirect("/online/")
