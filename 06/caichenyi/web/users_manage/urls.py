# encoding: utf-8
# Author: Cai Chenyi

from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^index', views.index, name='index'),
    url(r'^login', views.login, name='login'),
    url(r'^home', views.home, name='home'),
    url(r'^add', views.add, name='add'),
    url(r'^delete', views.delete, name='delete'),
    url(r'^modify', views.modify, name='modify'),
    url(r'^list', views.list, name='list'),
    url(r'^find', views.find, name='find'),
]