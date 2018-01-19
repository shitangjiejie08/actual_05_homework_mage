#! /usr/bin/env python
# -*- coding:utf-8 -*-
from django.conf.urls import url
from . import views

urlpatterns=[
    url(r"^$", views.index, name="index"),
    url(r"^detail/(?P<day>\w{4}-\w{2}-\w{2})/$",views.detail, name="detail"),
]