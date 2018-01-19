#encoding: utf-8

from django import forms
from django.core.exceptions import ObjectDoesNotExist

from . import models
from utils import crypt

class LoginForm(forms.Form):
    username = forms.CharField(label="用户名", required=False)
    password = forms.CharField(widget=forms.PasswordInput, label="密码", required=False)

    def clean(self):
        cleaned_data = super(LoginForm, self).clean()

        username = cleaned_data.get('username', '')
        password = cleaned_data.get('password', '')
        if username == '' or password == '':
            raise forms.ValidationError('用户名或密码为空')

        password = crypt.CryptUtils.md5(password)
        count = models.User2.objects.filter(username=username, password=password).count()
        if count == 0:
            raise forms.ValidationError("用户名或密码错误")
        # try:
        #     models.User2.objects.get(username=username, password=password)
        # except ObjectDoesNotExist as e:
        #     raise forms.ValidationError("用户名或密码错误")
        return cleaned_data


class CreatUser(forms.Form):
    username = forms.CharField(label="用户名", required=False, error_messages={'required': '用户名不能为空'})
    password = forms.CharField(widget=forms.PasswordInput, label="密码", required=False, error_messages={'required': '密码不能为空'})
    tel = forms.CharField(label="电话号码", required=False, error_messages={'required': '电话号码不能为空'})
    age = forms.IntegerField(label='年龄', required=False, error_messages={'required': '年龄不能为空'})

    def clean(self):
        cleaned_data = super(CreatUser, self).clean()

        username = cleaned_data.get('username', '')
        password = cleaned_data.get('password', '')
        tel = cleaned_data.get('tel', '')
        age = cleaned_data.get('age', '')
        if username == '' or password == '' or tel == '' or age == '':
            raise forms.ValidationError('输入不能为空')
        if len(password) < 8:
            raise forms.ValidationError('密码必须大于8位')
        if age < 0 or age > 100:
            raise forms.ValidationError('年龄必须0-100')
        if models.User2.objects.filter(username=username).count() != 0:
            raise forms.ValidationError("用户已存在")

        return cleaned_data


class ViewUser(forms.Form):
    username = forms.CharField(label="用户名", required=False, error_messages={'required': '用户名不能为空'})
    tel = forms.CharField(label="电话号码", required=False, error_messages={'required': '电话号码不能为空'})
    age = forms.IntegerField(label='年龄', required=False, error_messages={'required': '年龄不能为空'})

    def clean(self):
        cleaned_data = super(ViewUser, self).clean()
        username = cleaned_data.get('username', '')
        tel = cleaned_data.get('tel', '')
        age = cleaned_data.get('age', '')
        if username == '' or tel == '' or age == '':
            raise forms.ValidationError('输入不能为空')
        if age < 0 or age > 100:
            raise forms.ValidationError('年龄必须0-100')
        if models.User2.objects.filter(username=username).count() != 0:
            raise forms.ValidationError("用户已存在")

        return cleaned_data


class ViewPassword(forms.Form):
    password = forms.CharField(widget=forms.PasswordInput, label="密码", required=False, error_messages={'required': '输入不能为空'})

    def clean(self):
        cleaned_date = super(ViewPassword, self).clean()
        password = cleaned_date.get('password', '')
        if len(password) < 8:
            raise forms.ValidationError('密码长度不能少于8位')

        return cleaned_date

