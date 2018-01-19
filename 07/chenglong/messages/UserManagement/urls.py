#encoding:utf-8
from django.conf.urls import url
from . import views


urlpatterns = [
    url(r'^require_login/', views.require_login, name='require_login'),
    url(r'^login/', views.login, name='login'),
    url(r'^list_user/', views.list_user, name='list_user'),
    url(r'^add_user/', views.add_user, name='add_user'),
    url(r'^del_user/', views.del_user, name='del_user'),
    url(r'^chg_user/', views.chg_user, name='chg_user')

]