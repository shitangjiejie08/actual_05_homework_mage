from django.conf.urls import url

from . import user,views


urlpatterns = [
    url(r'^hello/$', views.hello),
    url(r'^login/$', user.userlogin),
    url(r'^logout/$', user.userlogout),
    url(r'^user/$', views.UserView.as_view()),  ##类视图需要加上as_view()
    # url(r'^user$', include([
    #     views.UserView.as_view(),
    #     ])),
    url(r'^userlist/$', views.UserListView.as_view()),  ##类视图需要加上as_view()
    url(r'^userlistview/$', views.UserListAsView.as_view()),  ###用listview实现

]