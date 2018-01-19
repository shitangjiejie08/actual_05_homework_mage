#encoding: utf-8
from django.conf.urls import url
from . import views

urlpatterns = [
    url("^require_login/",views.require_login,name="require_login"),
    url("^login/",views.login,name="login"),
    url("^list_users/",views.list_users,name="list_users"),
    url("^delete_users/",views.delete_users,name="delete_users"),
    url("^view_users/",views.view_users,name="view_users"),
    url("^view_users_passwd/",views.view_users_passwd,name="view_users_passwd"),
    url("^modify/",views.modify,name="modify"),
    url("^modify_passwd/",views.modify_passwd,name="modify_passwd"),
    url("^edit_user_info/",views.edit_user_info,name="edit_user_info"),
    url("^create_users/",views.create_users,name="create_users"),
    url("^logout/",views.logout,name="logout"),
    url("^get_list_ajax/",views.get_list_ajax,name="get_list_ajax"),
    url("^createuser_ajax/",views.createuser_ajax,name="createuser_ajax"),
    url("^edituserbasicinfo_ajax/",views.edituserbasicinfo_ajax,name="edituserbasicinfo_ajax"),
    url("^edituserpasswordinfo_ajax/",views.edituserpasswordinfo_ajax,name="edituserpasswordinfo_ajax"),
    
]
