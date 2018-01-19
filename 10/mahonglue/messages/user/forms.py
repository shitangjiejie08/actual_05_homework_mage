#! /usr/bin/env python
# -*- coding:utf-8 -*-
from django import forms
from .models import User2
from utils import crypt

class LoginForm(forms.Form):
    username = forms.CharField(label="用户名", error_messages={"required":"用户名不能为空"}) #如果想让错误信息中的required生效，必须在html中<form>属性加上 ： novalidate="novalidate"
    password = forms.CharField(label="密码", widget=forms.PasswordInput, error_messages={"required":"用密码不能为空"})

    def clean(self):
        cleaned_data = super(LoginForm,self).clean()
        username = cleaned_data.get("username","")
        password = cleaned_data.get("password","")
        password = crypt.md5(password)
        # rt = User2.objects.filter(username=username, password=password)
        try:
            User2.objects.get(username=username, password=password)
        except :
            raise forms.ValidationError("用户名或密码错误")
        return cleaned_data


class CreateForm(forms.Form):
    username = forms.CharField(label="用户名", error_messages={"required":"用户名不能为空"})
    password = forms.CharField(label="密码", widget=forms.PasswordInput, error_messages={"required":"密码不能为空"})
    age = forms.IntegerField(label="年龄", error_messages={"required":"年龄不能为空"})
    tel = forms.CharField(label="电话号码", error_messages={"required":"电话号码不能为空"})

    def clean_username(self):
        username = self.cleaned_data.get("username")
        rt = User2.objects.filter(username=username)
        if rt:
            raise forms.ValidationError("用户名已存在，无需注册")
        return username

class ViewForm(forms.Form):
    username = forms.CharField(label="用户名", error_messages={"required":"用户名不能为空"})
    age = forms.IntegerField(label="年龄", error_messages={"required":"年龄不能为空"})
    tel = forms.CharField(label="电话号码", error_messages={"required":"电话号码不能为空"})


