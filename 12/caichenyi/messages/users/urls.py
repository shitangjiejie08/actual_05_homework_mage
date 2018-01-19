# encoding: utf-8
# Author: Cai Chenyi
from django.conf.urls import url, include
from django.contrib import admin
from . import views

urlpatterns = [
    url(r'^hello/$', views.hello),
    url(r'^login/$', views.userlogin),
    url(r'^logout/$', views.userlogout),
    url(r'^create/$', views.UserCreate.as_view()),
    url(r'^list/$', views.UserList.as_view()),
    # url(r'^modify_info/$', views.modify_info),
    # url(r'^modify_passwd/$', views.modify_passwd),
    # url(r'^delete_user/$', views.delete_user),
    url(r'^modify_info/$', views.UserModify.as_view()),
    url(r'^modify_passwd/$', views.UserModify.as_view()),
    url(r'^delete_user/$', views.UserModify.as_view()),
]