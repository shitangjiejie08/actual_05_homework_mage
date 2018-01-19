from django.shortcuts import render

# Create your views here.
from django.views.generic import View
from django.contrib.auth.models import User
from .models import UserExt
import datetime
from django.utils import timezone
from django.http import JsonResponse,HttpResponse
from django.core.mail import send_mail
from django.conf import settings
from django.core.exceptions import ObjectDoesNotExist

class RegisterView(View):
    #获取数据并且存储，并发送邮件
    def post(self,request,*args,**kwargs):
        username = request.POST.get('userName','')
        password = request.POST.get('password','')
        email = request.POST.get('email','')

        user = User.objects.create_user(username=username, password=password, email=email)

        validkey = UserExt.gen_validkey()
        user_ext = UserExt.objects.create(user=user, realname='', birthday=datetime.date(1990,3,13),\
                                         nickname='', avatar='default', telephone='', logintime=timezone.now(), validkey=validkey)
        return JsonResponse({'status':'200'})


    def get(self,request,*args,**kwargs):
        #创建第一条数据存储数据，并且发送邮件
        username = request.GET.get('userName','')
        password = request.GET.get('password','')
        password2 = request.GET.get('password2', '')
        email = request.GET.get('email','')
        if username == '' or password == '' or password2 == '' or email == '':
            return JsonResponse({'status': 400, 'errors': ['内容填写不完整']})
        if password != password2:
            return JsonResponse({'status': 400, 'errors': ['两次输入密码不同']})
        else:
            try:
                user = User.objects.get(username=username)
                return JsonResponse({'status':400, 'errors':['该用户已经被注册']})
            except ObjectDoesNotExist as e:

                user = User.objects.create_user(username=username, password=password, email=email)

                validkey = UserExt.gen_validkey()
                user_ext = UserExt.objects.create(user=user, realname='', birthday=datetime.date(1990,3,13),\
                                                nickname='', avatar='default', telephone='', logintime=timezone.now(), validkey=validkey)
                content = 'http://127.0.0.1:8000/account/active/?username={username}&validkey={validkey}"点击此处'.format(username=username,validkey=validkey)
                send_mail('User Register OK', content,settings.EMAIL_HOST_USER,[email])
                return JsonResponse({'status': 200, 'result': '已向{email}邮箱发送激活链接'.format(email=email)})

class ActiveView(View):
    #验证数据是否正常
    def get(self,request,*args,**kwargs):
        username = request.GET.get('username','')
        validkey = request.GET.get('validkey','')
        try:
            user = User.objects.get(username=username)
            if user.userext.status == 0:
                if validkey == validkey:
                    user.userext.status = 1
                    user.userext.save()
                    return HttpResponse("激活成功")
                else:
                    return HttpResponse('验证码不正确')
            return HttpResponse('验证码错误')
        except ObjectDoesNotExist as e:
            pass
        return HttpResponse("用户不存在")

def save_ajax(response):
    userName = response.POST.get('userName','')
    password = response.POST.get('password','')
    password2 = response.POST.get('password2','')
    email = response.POST.get('email','')
    if userName == '' or password == '' or password2 == '' or email == '':
        return JsonResponse({'status':400, 'errors':['内容填写不完整']})
    if password != password2:
        return JsonResponse({'status':400,'errors':['两次输入密码不同']})
    else:
        return JsonResponse({'status':200, 'result':'已向{email}邮箱发送激活链接'.format(email=email)})
