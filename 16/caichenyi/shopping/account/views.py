#encoding: utf-8
import datetime
import json


from django.conf import settings
from django.utils import timezone

from django.shortcuts import render
from django.views.generic import View
from django.http import JsonResponse, HttpResponse
from django.core.exceptions import ObjectDoesNotExist

from django.contrib.auth.models import User

from django.core.mail import send_mail

from .models import UserExt
from .forms import RegisterForm

class RegisterView(View):

    def post(self, request, *args, **kwargs):
        form = RegisterForm(request.POST)
        return self._register(form)


    def _register(self, form):
        if form.is_valid():
            username = form.cleaned_data.get('username', '')
            password = form.cleaned_data.get('password', '')
            email = form.cleaned_data.get('email', '')

            user = User.objects.create_user(username=username, password=password, email=email)
            validkey = UserExt.gen_validkey()

            user_ext = UserExt.objects.create(user=user, realname='', birthday=datetime.date(1945, 1, 1), \
                                                nickname='', avatar='default', telephone='', logintime=timezone.now(), validkey=validkey)

            content = '欢迎注册[KK的商城], 请点击此处进行激活用户: http://192.168.6.15:8000/account/active/?username={username}&validkey={validkey}'.format(username=username, validkey=validkey)
            send_mail('[KK的商城]用户注册', content, settings.EMAIL_HOST_USER, [email])

            return JsonResponse({'status': 200})
        else:
            return JsonResponse({'status': 400, 'errors': json.loads(form.errors.as_json()), 'result': ''})


    def get(self, request, *args, **kwargs):
        form = RegisterForm(request.GET)
        return self._register(form)


class  ActiveView(View):

    def get(self, request, *args, **kwargs):
        username = request.GET.get('username', '')
        validkey = request.GET.get('validkey', '')

        #objectdoesnotexists
        try:
            user = User.objects.get(username=username)
            if user.userext.status == 0 and user.userext.validkey != '':
                if user.userext.validkey == validkey:
                    user.userext.status = 1
                    user.userext.validkey = ''
                    user.userext.save()
                    return HttpResponse("激活成功")
                else:
                    return HttpResponse('验证码不正确')

            return HttpResponse("用户已经激活")
        except ObjectDoesNotExist as e:
            pass
            #跳转到页面
        return HttpResponse("用户不存在")
