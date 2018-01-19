from django.shortcuts import render

from .models import get_messages,set_messages,message2
from django.http import HttpResponseRedirect
from django.utils import timezone
from .form import MessageForm

# Create your views here.

def index(request):
    messages = message2.objects.order_by("-publish_date")
    #context = {'messages': get_messages() }
    context = {'messages': messages }
    print(context)
    return render(request, 'online/index.html',context)

def comment(request):
    f = MessageForm()
    context = {'f': f }    
    return render(request, 'online/comment.html', context)

# def save(request):
#     username = request.POST.get('username')
#     title = request.POST.get('title')
#     content = request.POST.get('content')
#     if username and title and content:
#         #message = { 
#         #            "username": username,
#         #            "title": title,
#         #            "content": content
#         #           }
#         #set_messages(message)
#         ms = message2(username=username,title=title,content=content,publish_date=timezone.now())
#         ms.save()

#         return HttpResponseRedirect("/online/")

#     else:
#         print('xxxxx')
#         f = MessageForm()
#         context = {'f': f }
#         context = { 
#                     "username": username,
#                     "title": title,
#                     "content": content,
#                     "error": "输入信息不能为空",
#                     "f": f
#                    }
#         print(context)
#         return render(request,"online/comment.html",context)

def save(request):
    f = MessageForm(request.POST)
    if f.is_valid():
        ms = message2(username=f.cleaned_data["username"],
                      title=f.cleaned_data["title"],
                      content=f.cleaned_data["content"],
                      publish_date=timezone.now())

        ms.save()

        return HttpResponseRedirect("/online/")

    else:
        return render(request,"online/comment.html",{"f":f})





