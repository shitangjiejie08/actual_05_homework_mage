#! /usr/bin/env python
# -*- coding:utf-8 -*-

from django import forms

class MessageForm(forms.Form):
    username = forms.CharField(label="用户名", error_messages={"required":"用户名不能为空"}) #用error_messages的时候，需要关闭前端的HTML自动验证，
    # 就是把novalidate="novalidate"加上<form action="/online/save/" method="POST" novalidate="novalidate">
    title = forms.CharField(label="标题", error_messages={"required":"用户名不能为空"})
    content = forms.CharField(widget=forms.Textarea, max_length=200, min_length=10, label="内容", help_text="内容可以不写") #不写error_messages={"required":"用户名不能为空"}就代表可以为空

    # username = forms.CharField(label="用户名", error_messages={"required":"用户名不能为空"}) #用error_messages的时候，需要关闭前端的HTML自动验证，
    # # 就是把novalidate="novalidate"加上<form action="/online/save/" method="POST" novalidate="novalidate">
    # title = forms.CharField(label="标题", error_messages={"required":"用户名不能为空"})
    # content = forms.CharField(widget=forms.Textarea, label="内容", help_text="内容可以不写") #不写error_messages={"required":"用户名不能为空"}就代表可以为空

    def clean_username(self):
        username = self.cleaned_data.get("username", "")
        if len(username) >8:
            raise forms.ValidationError("用户名长度不能超过8")
        return username