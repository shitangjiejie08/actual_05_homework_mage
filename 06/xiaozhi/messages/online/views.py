from django.shortcuts import render
from django.http import HttpResponseRedirect
from . import models

def index(request):
    print(models.get_messages())
    context = {'messages':models.get_messages}
    #context = {'messages':None}
    return render(request, 'online/index.html', context)


def create(request):
    return render(request, 'online/create.html')


def save(request):
   username = request.POST.get("username", '')
   title = request.POST.get("title", '')
   content = request.POST.get("content", '')
   models.save_message(username, title, content)
   return HttpResponseRedirect('/online/')

