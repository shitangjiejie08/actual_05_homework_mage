#! /usr/bin/env python
# -*- coding:utf-8 -*-
from django import forms

class LoginForm(forms.Form):
    user = forms.CharField(max_length=12,min_length=9,widget=forms.TextInput(),error_messages={"required":"用户名不能为空"})
    password = forms.CharField(widget=forms.PasswordInput())
    tel = forms.CharField(max_length=11,min_length=11,widget=forms.TextInput())
    age = forms.IntegerField(widget=forms.TextInput())