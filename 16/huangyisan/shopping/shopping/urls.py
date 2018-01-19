from django.conf.urls import url, include
from django.contrib import admin
from django.views.generic import RedirectView,TemplateView

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', TemplateView.as_view(template_name='index.html')),
    url(r'^account/', include('account.urls')),
    url(r'^goods/', include('goods.urls')),
    url(r'^report/', include('report.urls')),

]
