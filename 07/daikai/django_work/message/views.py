from django.shortcuts import render
from django.http import HttpResponseRedirect

# Create your views here.
from . import models
import datetime

def index(request):
    print(models.get_messages())
    context = {'messages': models.get_messages()}
    return render(request, 'message/index.html', context)


def create(request):
    return render(request, 'message/create.html')


def save(request):
    username = request.POST.get('username','')
    title = request.POST.get('title','')
    content = request.POST.get('content','')
    publish_date = datetime.datetime.now().strftime('%Y%m%d %H:%M:%S')
    #print(username, title, content)
    if username and title and content:
        models.save_messages(username, title, content, publish_date)
        return HttpResponseRedirect('/message/')
    else:
        context = {'username':username, 'title':title, 'content':content, 'error':'输入信息不能为空'}
        return render(request, 'message/create.html', context)
