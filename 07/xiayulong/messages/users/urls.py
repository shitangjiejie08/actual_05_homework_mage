#encoding: utf-8
from django.conf.urls import url
from . import views

urlpatterns = [
    url("^require_login/",views.require_login,name="require_login"),
    url("^login/",views.login,name="login"),
    url("^list_users/",views.list_users,name="list_users"),
    url("^delete_users/",views.delete_users,name="delete_users"),
    url("^view_users/",views.view_users,name="view_users"),
    url("^modify/",views.modify,name="modify"),
    url("^edit_user_info/",views.edit_user_info,name="edit_user_info"),
    url("^create_users/",views.create_users,name="create_users"),
]
