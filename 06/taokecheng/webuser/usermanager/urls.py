from django.conf.urls import url
from . import views
urlpatterns = [
	url(r'^$',views.index,name='index'),
	url(r'^delete.html$',views.delete,name='delete'),
	url(r'^delUser$',views.delUser,name='delUser'),
	url(r'^search.html$',views.search,name='search'),
	url(r'^update.html$',views.update,name='update'),
	url(r'^list.html$',views.listUser,name='listUser'),
	url(r'^add.html$',views.add,name='add'),
	url(r'^addUser$',views.addUser,name='addUser'),
	url(r'^index.html$',views.index,name='index'),
]
