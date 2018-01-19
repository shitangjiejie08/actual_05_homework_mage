#! /usr/bin/env python
# -*- coding:utf-8 -*-
from django.conf.urls import url
from . import views

urlpatterns=[
    url(r"^require_login/$",views.require_login,name="require_login"),
    url(r'login/$',views.login,name="login"),
    url(r'^list_user/$',views.list_user,name="list_user"),
    url(r'^delete_user/(?P<name>\w+)/$',views.delete_user,name="delete_user"),
]