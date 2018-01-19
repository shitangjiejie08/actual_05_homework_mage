# encoding: utf-8
# Author: Cai Chenyi

from django.conf.urls import url, include

from . import views

urlpatterns = [
    url(r'^index/', views.index, name='index'),
    url(r'^login/', views.login, name='login'),
    url(r'^delete/', views.delete, name='delete'),
    url(r'^require_edit/', views.require_edit, name='require_edit'),
    url(r'^edit/', views.edit, name='edit'),
    url(r'^require_list/', views.require_list, name='require_list'),
    url(r'^list/', views.list, name='list'),
    url(r'^add/', views.add, name='add'),
]