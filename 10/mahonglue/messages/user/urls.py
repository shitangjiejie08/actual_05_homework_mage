#encoding: utf-8
from django.conf.urls import url

from . import views


urlpatterns = [
    url(r'^require_login/', views.require_login, name='require_login'),
    url(r'^login/', views.login, name='login'),
    url(r'^list_user/', views.list_user, name='list_user'),
    url(r'^delete_user/', views.delete_user, name='delete_user'),
    url(r'^create_user/', views.create_user, name='create_user'),
    url(r'^view_user/', views.view_user, name='view_user'),
    url(r'^logout/', views.logout, name='logout'),

]
