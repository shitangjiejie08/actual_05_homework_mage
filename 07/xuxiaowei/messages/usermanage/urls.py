#encoding: utf-8
from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^find/$',views.find, name='find'),
    url(r'^find_save/$',views.find_save, name='find_save'),
    url(r'^add/$',views.add, name='add'),
    url(r'^add_save/$',views.add_save, name='add_save'),
#    url(r'^save/$',views.save, name='save') 
]