#! /usr/bin/env python
# -*- coding:utf-8 -*-
from django.conf.urls import url
from . import views

urlpatterns = [
    url(r"^$",views.index, name="index"),
    url(r"^login/$",views.login, name="login"),
    url(r"^regist/$",views.regist,name="regist"),
    url(r"^list/$",views.list, name="list"),
    url(r"^edit/?P<user>(\w+)/$",views.edit,name="edit"),
    url(r"^edit_before/$",views.edit_before,name="edit_before"),
    url(r"^add/$",views.add,name="add"),
    url(r"^delete/?P<user>(\w+)/$",views.delete,name="delete"),
]