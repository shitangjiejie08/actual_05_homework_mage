from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect
from django.utils import timezone
from django.urls import reverse

# Create your views here.
from . import models
from . import forms


def index(request):
    if not request.session.get('user'):
        return redirect(reverse('user:require_login'))

    messages = models.Message2.objects.order_by('-publish_date')
    print(messages)
    context = {'messages' : messages}
    return render(request, 'online/index.html', context)


def create(request):
    if not request.session.get('user'):
        return redirect(reverse('user:require_login'))

    form = forms.MessageForm()
    print('form ', form)
    print('form type ', type(form))
    return render(request, 'online/create.html', {'form' : form})


def save(request):
    if not request.session.get('user'):
        return redirect(reverse('user:require_login'))

    form = forms.MessageForm(request.POST)
    if form.is_valid():
        message = models.Message2(title=form.cleaned_data['title'], \
                                    content=form.cleaned_data['content'], \
                                    username=form.cleaned_data['username'], \
                                    publish_date=timezone.now())
        print(message)
        message.save()
        return HttpResponseRedirect(reverse('online:index'))
    else:
        return render(request, 'online/create.html', {'form' : form})
