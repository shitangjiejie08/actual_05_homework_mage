#encoding: utf-8
from django import forms

from django.contrib.auth.models import User
from django.core.exceptions import ObjectDoesNotExist

class RegisterForm(forms.Form):
    username = forms.CharField(widget=forms.TextInput, error_messages={'required' : '用户名不能为空'})
    password = forms.CharField(widget=forms.PasswordInput, error_messages={'required' : '密码不能为空'})
    password2 = forms.CharField(widget=forms.PasswordInput, required=False)
    email = forms.EmailField(error_messages={'required' : '邮箱不能为空', 'invalid' : '邮箱格式不正确'})

    def clean_username(self):
        username = self.cleaned_data.get('username', '')
        if len(username) < 6 or len(username) > 16:
            raise forms.ValidationError('用户名必须为6位到16位')
        try:
            User.objects.get(username=username)
            raise forms.ValidationError('用户名已经存在')
        except ObjectDoesNotExist as e:
            pass

        return username


    def clean_password(self):
        password = self.cleaned_data.get('password', '')
        if len(password) < 6 or len(password) > 32:
            raise forms.ValidationError('密码必须为6位到32位')
        return password

    def clean_password2(self):
        password = self.cleaned_data.get('password', '')
        password2 = self.cleaned_data.get('password2', '')
        if password != password2:
            raise forms.ValidationError('两次密码不一致')

        return password2

    def clean_email(self):
        email = self.cleaned_data.get('email', '')
        try:
            User.objects.get(email=email)
            raise forms.ValidationError('邮件已注册')
        except ObjectDoesNotExist as e:
            pass

        return email
