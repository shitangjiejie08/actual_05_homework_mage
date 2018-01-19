from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect

# Create your views here.

from . import models

def index(request):
    # return HttpResponse('Hello Django')
    print(models.get_messages())
    context = {"messages": models.get_messages()}
    return render(request, 'online/index.html', context)

def create(request):
    return render(request, 'online/create.html')

def save(request):
    username = request.POST.get('username', '')
    title = request.POST.get('title', '')
    content = request.POST.get('content', '')
    if username and title and content:
        models.save_message(username, title, content)
        return HttpResponseRedirect('/online/')
    else:
        context = {'username': username, 'title': title, 'content': content, 'error': '用户名，标题，内容不能为空'}
        return render(request, 'online/create.html', context)