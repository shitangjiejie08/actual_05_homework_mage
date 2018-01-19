#encoding: utf-8
import datetime, time
import json, os


from django.conf import settings
from django.utils import timezone

from django.shortcuts import render
from django.views.generic import View, FormView
from django.views.generic.base import TemplateResponseMixin
from django.http import JsonResponse, HttpResponse, HttpResponseRedirect
from django.core.exceptions import ObjectDoesNotExist
from django.urls import reverse

from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout

from django.core.mail import send_mail
from django.db import transaction
from django.contrib import messages

from .models import UserExt
from .forms import RegisterForm, LoginForm, \
    ResetPasswordForm, ResetPasswordConfirmForm, ChangePasswordForm, \
    UserExtBaseForm, UserExtAvatarForm, UserExtAddrForm

from .decorator import login_required
from django.utils.decorators import method_decorator

from .mixins import LoginRequiredMixin

class RegisterView(View):

    def post(self, request, *args, **kwargs):
        form = RegisterForm(request.POST)
        return self._register(form)


    def _register(self, form):
        if form.is_valid():
            username = form.cleaned_data.get('username', '')
            password = form.cleaned_data.get('password', '')
            email = form.cleaned_data.get('email', '')

            try:
                with transaction.atomic():
                    user = User.objects.create_user(username=username, password=password, email=email)
                    validkey = UserExt.gen_validkey()
                    exprie_time = timezone.now() + datetime.timedelta(days=1)
                    user_ext = UserExt.objects.create(user=user, realname='', birthday=datetime.date(1945, 1, 1), \
                                                nickname=username, avatar='default', telephone='', logintime=timezone.now(), validkey=validkey, exprie_time=exprie_time, addr='')

                    content = '欢迎注册[CaiCY的商城], 请点击此处进行激活用户: http://192.168.6.15:8000/account/active/?username={username}&validkey={validkey}'.format(username=username, validkey=validkey)
                    send_mail('[CaiCY的商城]用户注册', content, settings.EMAIL_HOST_USER, [user.email])
            except BaseException as e:
                return JsonResponse({'status': 500, 'errors': ['服务器错误']})
            return JsonResponse({'status': 200})
        else:
            return JsonResponse({'status': 400, 'errors': json.loads(form.errors.as_json()), 'result': ''})


    def get(self, request, *args, **kwargs):
        form = RegisterForm(request.GET)
        return self._register(form)


class ActiveView(View):

    def get(self, request, *args, **kwargs):
        username = request.GET.get('username', '')
        validkey = request.GET.get('validkey', '')

        #objectdoesnotexists
        try:
            user = User.objects.get(username=username)
            if user.userext.exprie_time < timezone.now():
                messages.add_message(request, messages.ERROR, '验证码超时，请查收邮箱并重新激活')
                validkey = UserExt.gen_validkey()
                user.userext.validkey = validkey
                user.userext.exprie_time = timezone.now() + datetime.timedelta(days=1)
                user.userext.save()
                content = '欢迎注册[CaiCY的商城], 请点击此处进行激活用户: http://192.168.6.15:8000/account/active/?username={username}&validkey={validkey}'.format(username=username, validkey=validkey)
                send_mail('[CaiCY的商城]用户注册重新激活', content, settings.EMAIL_HOST_USER, [user.email])
            elif user.userext.status == 0 and user.userext.validkey != '':
                if user.userext.validkey == validkey:
                    user.userext.status = 1
                    user.userext.validkey = ''
                    user.userext.save()
                    messages.add_message(request, messages.INFO, '激活成功，请登录')
                else:
                    messages.add_message(request, messages.ERROR, '激活失败，用户名或验证码不正确')
            else:
                messages.add_message(request, messages.ERROR, '激活失败，用户名或验证码不正确')
        except ObjectDoesNotExist as e:
            pass
            #跳转到页面
        return HttpResponseRedirect(reverse('index'))
        # return HttpResponse("用户不存在")


class LoginView2(View):
    def post(self, request, *args, **kwargs):
        form = LoginForm(request.POST)
        if form.is_valid():
            login(request, form.cached_user)
            return JsonResponse({'status': 200, 'errors': {}, 'result': {}})
        else:
            return JsonResponse({'status': 400, 'errors': json.loads(form.errors.as_json()), 'result': []})


class LoginView(FormView):
    form_class = LoginForm

    def form_valid(self, form):
        login(self.request, form.cached_user)
        return JsonResponse({'status': 200, 'errors': {}, 'result': {}})

    def form_invalid(self, form):
        return JsonResponse({'status': 400, 'errors': json.loads(form.errors.as_json()), 'result': []})


class LogoutView(View):
    def get(self, request, *args, **kwargs):
        logout(request)
        return HttpResponseRedirect(reverse('index'))


class ModifyPasswordView(View):
    def get(self, request, *args, **kwargs):
        if request.user.is_authenticated():
            return HttpResponse('success')
        else:
            # return HttpResponse('fail')
            return HttpResponseRedirect(reverse('index'))


class ResetPasswordView(FormView):
    template_name = 'account/reset_password.html'
    form_class = ResetPasswordForm

    def form_valid(self, form):
        try:
            with transaction.atomic():
                user = form.cached_user
                validkey = user.userext.gen_validkey()
                user.userext.validkey = validkey
                user.userext.exprie_time = timezone.now() + datetime.timedelta(days=1)
                user.userext.save()
                content = '欢迎使用[CaiCY的商城], 请点击此处进行重置密码: http://192.168.6.15:8000/account/reset_password_confirm/?username={username}&validkey={validkey}'.format(username=user.username, validkey=validkey)
                send_mail('[CaiCY的商城]用户重置密码', content, settings.EMAIL_HOST_USER, [user.email])
                messages.add_message(self.request, messages.INFO, '重置密码邮件已发送，请查收邮件进行密码重置')
        except BaseException as e:
            messages.add_message(self.request, messages.ERROR, '重置密码邮件发送失败，请重试')

        return HttpResponseRedirect(reverse('index'))

    def form_invalid(self, form):
        return render(self.request, self.template_name, {'form': form})


class ResetPasswordConfirmView(FormView):
    template_name = 'account/reset_password_confirm.html'
    form_class = ResetPasswordConfirmForm

    def get(self, request, *args, **kwargs):
        username = request.GET.get('username', '')
        validkey = request.GET.get('validkey', '')
        form = ResetPasswordConfirmForm(initial={'username': username, 'validkey': validkey})
        try:
            user = User.objects.get(username=username)
            if user.userext.exprie_time < timezone.now():
                validkey = UserExt.gen_validkey()
                user.userext.validkey = validkey
                user.userext.exprie_time = timezone.now() + datetime.timedelta(days=1)
                user.userext.save()
                content = '欢迎使用[CaiCY的商城], 请点击此处进行重置密码: http://192.168.6.15:8000/account/reset_password_confirm/?username={username}&validkey={validkey}'.format(username=username, validkey=validkey)
                send_mail('[CaiCY的商城]用户重置密码', content, settings.EMAIL_HOST_USER, [user.email])
                messages.add_message(request, messages.ERROR, '验证码超时，请查收邮箱并重新激活')
                return HttpResponseRedirect(reverse('index'))
        except ObjectDoesNotExist as e:
            pass
            # 跳转页面
        return render(self.request, self.template_name, {'form': form})

    def get_initial(self):
        return self.request.GET

    def form_valid(self, form):
        user = form.cached_user
        password = form.cleaned_data.get('password', '')
        user.set_password(password)
        user.save()
        user.userext.validkey = ''
        user.userext.save()
        messages.add_message(self.request, messages.INFO, '重置密码成功，请重新登陆')
        return HttpResponseRedirect(reverse('index'))

    def form_invalid(self, form):
        return render(self.request, self.template_name, {'form': form})


class ChangePasswordView(LoginRequiredMixin, FormView):
    form_class = ChangePasswordForm

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs['user'] = self.request.user
        return kwargs

    def form_valid(self, form):
        user = self.request.user
        password = form.cleaned_data.get('password', '')
        user.set_password(password)
        user.save()
        logout(self.request)
        return JsonResponse({'status': 200, 'errors': {}, 'result': None })

    def form_invalid(self, form):
        return JsonResponse({'status': 400, 'errors': json.loads(form.errors.as_json()), 'result': None})


class UserExtBaseView(LoginRequiredMixin, TemplateResponseMixin, View):
    template_name = 'account/user_ext.html'
    form_class = UserExtBaseForm
    form_class_avatar = UserExtAvatarForm
    form_class_addr = UserExtAddrForm

    def get(self, request, *args, **kwargs):
        return self.render_to_response({
            'form': self.form_class(instance=request.user.userext),
            'form_avatar': self.form_class_avatar(instance=request.user.userext),
            'form_addr': self.form_class_addr(instance=request.user.userext),
            'nav': 'base',
        })

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST, instance=request.user.userext)
        if form.is_valid():
            model = form.save(commit=False)
            model.save()
        return self.render_to_response({
            'form': form,
            'form_avatar': self.form_class_avatar(instance=request.user.userext),
            'form_addr': self.form_class_addr(instance=request.user.userext),
            'nav': 'base',
        })


class UserExtAvatarView(LoginRequiredMixin, TemplateResponseMixin, View):
    template_name = 'account/user_ext.html'
    form_class = UserExtBaseForm
    form_class_avatar = UserExtAvatarForm
    form_class_addr = UserExtAddrForm

    def get(self, request, *args, **kwargs):
        return self.render_to_response({
            'form': self.form_class(instance=request.user.userext),
            'form_avatar': self.form_class_avatar(instance=request.user.userext),
            'form_addr': self.form_class_addr(instance=request.user.userext),
            'nav': 'avatar',
        })

    def post(self, request, *args, **kwargs):
        form_avatar = self.form_class_avatar(request.POST, files=request.FILES, instance=request.user.userext)
        if form_avatar.is_valid():
            avatar = request.FILES.get('avatar', None)
            if avatar:
                name = '{pk}_{ctime}.{suffix}'.format(pk=request.user.pk, ctime=int(time.time() * 1000), suffix=avatar.name.split('.')[-1])
                path = os.path.join(settings.MEDIA_ROOT, 'avatar', name)
                with open(path, 'wb') as fhandler:
                    for chunk in avatar.chunks():
                        fhandler.write(chunk)
                model = form_avatar.save(commit=False)
                model.avatar = name
                model.save()
        return self.render_to_response({
            'form': self.form_class(instance=request.user.userext),
            'form_avatar': form_avatar,
            'form_addr': self.form_class_addr(instance=request.user.userext),
            'nav': 'avatar',
        })


class UserExtAddrView(LoginRequiredMixin, TemplateResponseMixin, View):
    template_name = 'account/user_ext.html'
    form_class = UserExtBaseForm
    form_class_avatar = UserExtAvatarForm
    form_class_addr = UserExtAddrForm

    def get(self, request, *args, **kwargs):
        return self.render_to_response({
            'form': self.form_class(instance=request.user.userext),
            'form_avatar': self.form_class_avatar(instance=request.user.userext),
            'form_addr': self.form_class_addr(instance=request.user.userext),
            'nav': 'addr',
        })

    def post(self, request, *args, **kwargs):
        form_addr = self.form_class_addr(request.POST, instance=request.user.userext)
        if form_addr.is_valid():
            model = form_addr.save(commit=False)
            model.save()
        return self.render_to_response({
            'form': self.form_class(instance=request.user.userext),
            'form_avatar': self.form_class_avatar(instance=request.user.userext),
            'form_addr': form_addr,
            'nav': 'addr',
        })
