from django.shortcuts import render
from . import models
# Create your views here.

def index(request):
    print(models.get_messages())
    context = {'messages':models.get_messages()}
    return render(request,'online/index.html', context)

def create(request):
    return render(request,'online/create.html')

def save(request):
    username = request.GET.get('username','')
    title = request.GET.get('title','')
    content = request.GET.get('content','')
    print(username,title,content)
    models.save_message(username,title,content)
