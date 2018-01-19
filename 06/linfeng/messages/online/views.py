from django.shortcuts import render
from . import models
from django.http import HttpResponse, HttpResponseRedirect 
# Create your views here.
def index(request):
    context = {"messages":models.get_messages()}
    return render(request,'online/index.html',context)
def create(request):
    return render(request,'online/create.html')
def save(request):
    username = request.POST.get('username','')
    title = request.POST.get('title','')
    content = request.POST.get('content','')
    if username and title and content:
        models.save_messages(username,title,content)
        return HttpResponseRedirect('/online/')
    else:
        context = {"username":username,"title":title,"content":content,"error":"输入信息不能为空"}
        return render(request,'online/create.html',context)	
