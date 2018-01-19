from django.conf.urls import url
from . import views

urlpatterns = [
    url('^index/',views.index,name='index'),
    url('^create/',views.create,name='create'),
    url('^save/',views.save,name='save'),
]
