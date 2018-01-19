#encoding: utf-8
from django.conf.urls import url

from . import views


urlpatterns = [
    url(r'^require_login/', views.require_login, name='require_login'),
    url(r'^login/', views.login, name='login'),
    url(r'^list_user', views.list_user, name='list_user'),
    url(r'^delete_user/', views.delete_user, name='delete_user'),
    url(r'^add_user/', views.add_user, name='add_user'),
    url(r'^modify_user/', views.modify_user, name='modify_user'),

]
