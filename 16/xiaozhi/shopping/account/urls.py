from django.conf.urls import url
from .views import ReisterView, ActiveView
app_name = "account"

urlpatterns = [
    url(r'^register/', ReisterView.as_view(), name='register'),
    url(r'^active/', ActiveView.as_view(), name='active'),
]
