from django.conf.urls import patterns, include, url

from django.contrib import admin
from ventos import views
from django.conf.urls.static import static
from django.conf import settings

admin.autodiscover()

urlpatterns = [
    # Examples:
    # url(r'^$', 'ventos.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^$', 'ventos.views.index', name='index'),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^scheduler/',include('scheduler.urls'))] 
