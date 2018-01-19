#!/usr/bin/env python3
#coding=utf-8
"""
# Author: huangyisan
# Created Time : 六  5/13 11:21:29 2017
# File Name: urls.py
# Description:

"""
from django.conf.urls import url
from . import views
urlpatterns = [
    url(r'^$', views.require_login, name='require_login'),
    url(r'^require_login/', views.require_login, name='require_login'),
    url(r'^login/', views.login, name='login'),
    url(r'^list_user/', views.list_user, name='list_user'),
    url(r'^delete_user/', views.delete_user, name='delete_user'),
    url(r'^edit_user/', views.edit_user, name='edit_user'),
    url(r'^modify_user/', views.modify_user, name='modify_user'),
    url(r'^add_user/', views.add_user, name='add_user'),
    url(r'^unauth_error/', views.unauth_error, name='unauth_error'),
    url(r'^exit_user/', views.exit_user, name='exit_user'),
]
