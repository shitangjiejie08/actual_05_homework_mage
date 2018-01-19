from django.shortcuts import render

from .models import get_messages,set_messages
from django.http import HttpResponseRedirect

# Create your views here.

def index(request):
    context = {'messages': get_messages() }
    return render(request, 'online/index.html',context)

def comment(request):
    return render(request, 'online/comment.html')

def save(request):
    username = request.GET.get('username')
    title = request.GET.get('title')
    content = request.GET.get('content')
    if username and title and content:
        message = { 
                    "username": username,
                    "title": title,
                    "content": content
                   }
        set_messages(message)
        return HttpResponseRedirect("/online/")

    else:
        print('xxxxx')
        context = { 
                    "username": username,
                    "title": title,
                    "content": content,
                    "error": "输入信息不能为空"
                   }
        print(context)
        return render(request,"online/comment.html",context)
