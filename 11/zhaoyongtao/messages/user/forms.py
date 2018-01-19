#encoding: utf-8
 
from django import forms
from django.core.exceptions import ObjectDoesNotExist
from . import models
from utils import crypt

class LoginForm(forms.Form):
    username = forms.CharField(label="用户名", required=False)
    password = forms.CharField(widget=forms.PasswordInput, label="密  码", required=False)
 
    def clean(self):
        cleaned_data = super(LoginForm, self).clean()
 
        username = cleaned_data.get('username', '')
        password = cleaned_data.get('password', '')
        if username == '' or password == '':
            raise forms.ValidationError('用户名或密码为空')
 
        password = crypt.CryptUtils.md5(password)
        count = models.User.objects.filter(username=username, password=password).count()
        if count == 0:
            raise forms.ValidationError("用户名或密码错误")
        return cleaned_data
 
 
class CreateUserForm(forms.Form):
    username = forms.CharField(label="用户名", error_messages={"required" : "用户名不能为空"})
    password = forms.CharField(label="密码", widget=forms.PasswordInput, error_messages={"required" : "密码不能为空"})
    other_password = forms.CharField(label="确认密码", required=False, widget=forms.PasswordInput)
    age = forms.CharField(label="年龄", error_messages={"required" : "年龄不能为空"})
    tel = forms.CharField(label="电话号码", error_messages={"required" : "手机号不能为空"})
 
    def clean_username(self):
        username = self.cleaned_data.get('username', '')
        #models.User.filter(username=username).count()
        try:
            models.User.objects.get(username=username)
            raise forms.ValidationError("名字已经存在")
        except ObjectDoesNotExist as e:
            pass
 
        return username
 
    def clean_password(self):
        return self.cleaned_data.get('password', '')
 
    def clean_other_password(self):
        password = self.cleaned_data.get('password', '')
        other_password = self.cleaned_data.get('other_password', '')
 
        if password != other_password:
            raise forms.ValidationError("两次密码不一致")
 
        return other_password
 
    def clean_age(self):
        age = self.cleaned_data.get('age', 0)
        if not str(age).isdigit():
            raise forms.ValidationError("年龄必须是10到80的数字")
 
        age = int(age)
        if age < 10 or age > 80:
            raise forms.ValidationError("年龄必须是10到80的数字")
 
        return age
 

class ModifyUserForm(forms.Form):
    id = forms.CharField(widget=forms.HiddenInput)
    username = forms.CharField(label="用户名", error_messages={"required" : "用户名不能为空"})
    age = forms.CharField(label="年龄", error_messages={"required" : "年龄不能为空"})
    tel = forms.CharField(label="电话号码", error_messages={"required" : "手机号不能为空"}) 
 
 
class PassForm(forms.Form):
    id = forms.CharField(widget=forms.HiddenInput, required=False)
    old_pass = forms.CharField(widget=forms.PasswordInput, label="旧密码", error_messages={'required' : "旧密码不能为空"})
    new_pass = forms.CharField(label="新密码", widget=forms.PasswordInput, error_messages={"required" : "新密码不能为空"})
    confirm_pass = forms.CharField(label="确认密码", widget=forms.PasswordInput, error_messages={"required" : "确认密码不能为空"})

    def clean_old_pass(self): 
        if not models.User.objects.filter(pk=self.cleaned_data.get('id', ''),password=crypt.CryptUtils.md5(self.cleaned_data.get('old_pass', ''))):
            raise forms.ValidationError("旧密码不正确")
 
        return self.cleaned_data.get('old_pass', '')
 
    def clean_confirm_pass(self):
        new_pass = self.cleaned_data.get('new_pass', '')
        confirm_pass = self.cleaned_data.get('confirm_pass', '')
        print('new',new_pass,'confirm',confirm_pass)
        if new_pass != confirm_pass:
            raise forms.ValidationError("两次密码不一致")
        if len(new_pass)<6 or len(new_pass)>12 or len(confirm_pass)<6 or len(confirm_pass)>12:
            raise forms.ValidationError("密码长度在6至12位之间")        
        return confirm_pass


