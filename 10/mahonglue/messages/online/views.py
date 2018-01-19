from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect
from django.utils import timezone
from datetime import  datetime
from .forms import MessageForm
from . import models


def index(request):
    if not request.session.get('user'):
        return redirect('/user/require_login/')

    messages = models.Message2.objects.order_by("-publish_date")
    print(messages)
    context = {'messages' : messages}
    return render(request, 'online/index.html', context)


def create(request):
    if not request.session.get('user'):
        return redirect('/user/require_login/')
    form = MessageForm()
    return render(request, 'online/create.html',{"form":form})


def save(request):
    if not request.session.get('user'):
        return redirect('/user/require_login/')
    form = MessageForm(request.POST)
    if form.is_valid():
        form.cleaned_data.get("username","")
        message = models.Message2(title=form.cleaned_data.get("title",""), content=form.cleaned_data.get("content",""), username=form.cleaned_data.get("username",""), publish_date=timezone.now())
        print(message)
        message.save()
        return HttpResponseRedirect('/online/')
    else:
        return render(request, 'online/create.html',{"form":form})
