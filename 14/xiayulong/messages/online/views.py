from django.shortcuts import render

from .models import get_messages,set_messages,message2
from django.http import HttpResponseRedirect,HttpResponse,JsonResponse
from django.utils import timezone
from .form import MessageForm,MessageForm2
import json

# Create your views here.
JsonResponse
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

def save_ajax(request):
    if request.session.get("user") is None:
        return JsonResponse({"status":403,"result":"user not login"})
    print(request.session)
    f = MessageForm2(request.POST)
    if f.is_valid():
        username = request.session.get('user')
        title = request.POST.get("title","Nulll")
        content = request.POST.get("content","Nulll")
        pubilsh_date = timezone.now()
        ms = message2(username=username,
                      title=title,
                      content=content,
                      publish_date=pubilsh_date)
        ms.save()
        return HttpResponse(json.dumps({"status":200,"result":"successfully"}))
    return JsonResponse({"status":400,"result":"","errors":json.loads(f.errors.as_json())})
    # f = MessageForm(request.POST)
    # if f.is_valid():
    #     ms = message2(username=f.cleaned_data["username"],
    #                   title=f.cleaned_data["title"],
    #                   content=f.cleaned_data["content"],
    #                   publish_date=timezone.now())
    #
    #     ms.save()
    #
    #     return HttpResponseRedirect("/online/")
    #
    # else:
    #     return render(request,"online/comment.html",{"f":f})


def get_ajax(request):
    if request.session.get("user") is None:
        return JsonResponse({"status":403,"result":"user not login"})
    messages = message2.objects.order_by("-publish_date")
    data = [message.as_dict() for message in messages]
    #return HttpResponse(json.dumps(data))
    return HttpResponse(json.dumps({"status": 200, "result": "successfully","messages":data}))

def get_ajax2(request):
    if request.session.get("user") is None:
        return JsonResponse({"status": 400, "result": "no login","data":[]})
    messages = message2.objects.order_by("-publish_date")
    data = [message.as_dict() for message in messages]
    return HttpResponse(json.dumps({"status": 200, "result": "successfully","data":data}))
    #return HttpResponse(json.dumps({"status": 200, "result": "successfully","messages":data}))




