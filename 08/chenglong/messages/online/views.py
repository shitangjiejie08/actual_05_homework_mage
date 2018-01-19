from django.shortcuts import render
from . import  models
from django.http import HttpResponseRedirect
import time


# Create your views here.

def index(request):
    print(models.get_messages())
    context = {'messages':models.get_messages()}
    return render(request, 'online/index.html', context)

def create(request):
    return render(request, 'online/create.html')


def save(request):
    publish_date = time.strftime('%Y%m%d %H:%M:%S:',time.localtime(time.time()))
    username = request.GET.get('username', '')
    title = request.GET.get('title', '')
    content = request.GET.get('content', '')
    print(content)
    models.save_messages(username=username,title=title,content=content)
    return HttpResponseRedirect('/online/')
