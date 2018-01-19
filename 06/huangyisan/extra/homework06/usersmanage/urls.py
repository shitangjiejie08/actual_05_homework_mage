from django.conf.urls import url
from . import views
urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^home/', views.home, name='home'),
    url(r'^usersinfo/', views.usersinfo, name='usersinfo'),
    url(r'^create/', views.create, name='create'),
    url(r'^delete/', views.delete, name='delete'),
    url(r'^search/', views.search, name='search'),
    url(r'^save_create/', views.save_create, name='save_create'),
    url(r'^save_delete/', views.save_delete, name='save_delete'),
    url(r'^searchinfo/', views.search_info, name='searchinfo'),
]
