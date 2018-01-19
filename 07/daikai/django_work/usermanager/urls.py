#encoding:utf-8

from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^require_login/', views.require_login, name='require_login'),
    url(r'^login/', views.login, name='login'),
    url(r'^list_user/', views.list_user, name='list_user'),
    url(r'^delete_user/', views.delete_user, name='delete_user'),
    url(r'^edit_user/', views.edit_user, name='edit_user'),
    url(r'^update/', views.update, name='update'),
    url(r'^create_user/', views.create_user, name='create_user'),
    url(r'^save_user/', views.save_user, name='save_user'),
]
