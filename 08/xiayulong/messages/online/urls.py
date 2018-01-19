# encoding:utf-8


from django.conf.urls import url
from . import views

urlpatterns=[
    url(r'^$',views.index,name='index'),
    url(r'^comment/$',views.comment,name='comment'),
    url(r'^save/$',views.save,name='save'),
]
