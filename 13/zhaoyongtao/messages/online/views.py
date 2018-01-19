from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect
from django.utils import timezone

# Create your views here.
from . import models
from . import forms

def index(request):
    if not request.session.get('user'):
        return redirect('/user/require_login/')

    messages = models.Message2.objects.all()
    for m in messages:
        print(m)
    context = {'messages' : messages}
    return render(request, 'online/index.html', context)


def create(request):
    if not request.session.get('user'):
        return redirect('/user/require_login/')
    form = forms.OnlineForm()
    return render(request, 'online/create.html',{'form':form})


def save(request):
    if not request.session.get('user'):
        return redirect('/user/require_login/')
    print(timezone.now())
    form = forms.OnlineForm(request.POST) #实例化一个form对象
    if form.is_valid():
        message = models.Message2(title=form.cleaned_data['title'], \
                                    content=form.cleaned_data['content'], \
                                    username=form.cleaned_data['username'], \
                                    publish=timezone.now())

        message.save()
        return HttpResponseRedirect('/online/')
    else:
        return render(request, 'online/create.html', {'form' : form})
