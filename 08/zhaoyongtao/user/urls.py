from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^login/',views.login,name='login'),
    url(r'^auth_login/',views.auth_login,name='auth_login'),
    url(r'^list/',views.user_list,name='user_list'),
    url(r'^add/',views.add,name='add'),
    url(r'^add_save/',views.add_save,name='add_save'),
    url(r'^edit/',views.edit,name='edit'),
    url(r'^edit_save/',views.edit_save,name='edit_save'),
    url(r'^edit_pass/',views.edit_pass,name='edit_pass'),
    url(r'^edit_pass_save/',views.edit_pass_save,name='edit_pass_save'),
    url(r'^delete/',views.delete,name='delete'),
    url(r'^logout/',views.logout,name='logout'),
]

