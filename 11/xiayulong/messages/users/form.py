# encoding: utf-8

from django import forms
from .models import auth_user_v2

class loginForm(forms.Form):
    name = forms.CharField(label="账号",error_messages={'required':"不能为空"})
    passwd = forms.CharField(label="密码",error_messages={'required':"不能为空"},widget=forms.PasswordInput)

    def clean(self):
        cleaned_data = super(loginForm,self).clean()
        return cleaned_data

    def clean_name(self):
        name = self.cleaned_data.get("name")

        if len(name) == 0:
            raise forms.validationError("用户名不能为空!!!!!")

        return name

    def clean_passwd(self):
        passwd = self.cleaned_data.get("passwd")

        if len(passwd) < 6:
            raise forms.ValidationError("密码不能少于6位!!!!")

        return passwd

class modifyuserbasicinfoForm(forms.Form):
    name = forms.CharField(label="用户名",error_messages={'required':"不能为空"},widget=forms.HiddenInput,required=True)
    tel = forms.CharField(label="电话",error_messages={'required':"电话和年龄不能同时为空"},required=False)
    age = forms.CharField(label="年龄",error_messages={'required':"电话和年龄不能同时为空"},required=False)

    def clean(self):
        cleaned_data = super(modifyuserbasicinfoForm,self).clean()
        if len(cleaned_data.get("tel")) == 0 and len(cleaned_data.get("age")) == 0:
            raise forms.ValidationError("电话和年龄不能同时为空！！！！")
        return cleaned_data

    def clean_name(self):
        name = self.cleaned_data.get("name")

        if len(name) == 0:
            raise forms.ValidationError("用户名不能为空!!!!")

        return name


class modifyuserpasswdinfoForm(forms.Form):
    name = forms.CharField(label="用户名",error_messages={'required':"不能为空"},widget=forms.HiddenInput,required=True)
    old_passwd = forms.CharField(label="旧密码",error_messages={'required':"密码不能少于6位"},widget=forms.PasswordInput)
    new_passwd = forms.CharField(label="新密码",error_messages={'required':"密码不能少于6位"},widget=forms.PasswordInput)
    confirm = forms.CharField(label="确认",error_messages={'required':"两次键入密码不同"},widget=forms.PasswordInput)

    # def clean(self):
    #     cleaned_data = super(modifyuserpasswdinfoForm,self).clean()
    #     if len(cleaned_data.get("old_passwd")) < 6 or len(cleaned_data.get("new_passwd")) < 6:
    #         raise forms.ValidationError("密码不能少于6位！！！！")
    #     return cleaned_data

    def clean_name(self):
        name = self.cleaned_data.get("name")

        if len(name) == 0:
            raise forms.ValidationError("用户名不能为空!!!!!")

        return name

    def clean_old_passwd(self):
        if len(self.cleaned_data.get("old_passwd")) < 6:
            raise forms.ValidationError("密码不能少于6位!!!!")
        return self.cleaned_data.get("old_passwd")

    def clean_new_passwd(self):
        if len(self.cleaned_data.get("new_passwd")) < 6:
            raise forms.ValidationError("密码不能少于6位!!!!")
        return self.cleaned_data.get("new_passwd") 

    def clean_confirm(self):
        new_passwd = self.cleaned_data.get("new_passwd")
        confirm = self.cleaned_data.get("confirm")

        if new_passwd != confirm:
            raise forms.ValidationError("两次键入密码不同!!!!")
        return confirm

class createuserinfoForm(forms.Form):
    name = forms.CharField(label="用户名",error_messages={'required':"不能为空"})
    tel = forms.CharField(label="电话",error_messages={'required':"电话不能为空"})
    age = forms.CharField(label="年龄",error_messages={'required':"年龄不能为空"})
    passwd = forms.CharField(label="密码",error_messages={'required':"不能少于6位"},widget=forms.PasswordInput)

    def clean_name(self):
        name = self.cleaned_data.get("name")

        if len(name) == 0:
            raise forms.validationError("用户名不能为空!!!!!")

        return name

    def clean_passwd(self):
        passwd = self.cleaned_data.get("passwd")

        if len(passwd) < 6:
            raise forms.ValidationError("密码不能少于6位!!!!!")

        return passwd

    def clean_tel(self):
        tel = self.cleaned_data.get("tel")

        if len(tel) == 0:
            raise forms.validationError("电话不能为空!!!!!")

        return tel

    def clean_age(self):
        age = self.cleaned_data.get("age")

        if len(age) == 0:
            raise forms.validationError("年龄不能为空!!!!!!")

        return age