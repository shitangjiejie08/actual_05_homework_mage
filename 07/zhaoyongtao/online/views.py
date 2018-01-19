from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect
from . import models
import datetime
# Create your views here.

def index(request):
    cxt = models.load_messages()
    content = {"messages":cxt}
    return render(request,'index.html',content)

def create(request):
    return render(request,'create.html')

def save(request):
    name = request.POST.get("name")
    title = request.POST.get("title")
    content = request.POST.get("content")
    publish_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    print(name,title,content,publish_time)
    models.create_messages(name,title,content,publish_time)
    return HttpResponseRedirect('/online/index/')
