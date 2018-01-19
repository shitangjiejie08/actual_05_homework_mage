#! /usr/bin/env python
# -*- coding:utf-8 -*-
from django.conf.urls import url
from . import views

urlpatterns = [
    url(r"^$", views.login, name="login"),
    url(r"^register/$", views.register, name="register"),
    url(r"^index/$", views.index, name="index"),
    url(r"^control/create/$",views.create, name="create"),
    url(r"^delete_user/$",views.delete_user, name="delete_user"),
    url(r"^update_user/$",views.update_user, name="update_user"),
    url(r"^find_user/$",views.find_user, name="find_user"),
    url(r"^messages/$", views.messages, name="messages"),
    url(r"^control/$", views.control, name="control"),
    url(r"^control/add/$", views.add, name="add"),
    url(r"^control/delete/$", views.deleter, name="delete"),
    url(r"^control/update/$", views.update, name="update"),
    url(r"^control/find/$", views.find, name="find"),
]