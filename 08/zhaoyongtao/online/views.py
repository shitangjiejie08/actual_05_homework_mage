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
    username = request.POST.get("username")
    title = request.POST.get("title")
    content = request.POST.get("content")
    publish_date = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    models.create_messages(username,title,content,publish_date)
    return HttpResponseRedirect('/online/index/')