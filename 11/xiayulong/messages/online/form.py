# encoding: utf-8

from django import forms
class MessageForm(forms.Form):
    username = forms.CharField(label="用户名",error_messages={'required':"不能为空"})
    title = forms.CharField(label="标题",error_messages={'required':"不能为空"})
    content = forms.CharField(widget=forms.Textarea,label="内容",error_messages={'required':"不能为空"} )

    def clean_username(self):
        username = self.cleaned_data.get("username")
        print(username)

        if len(username) > 6:
            raise forms.ValidationError("用户名不能大于6个字符")

        return username