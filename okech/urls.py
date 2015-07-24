from django.conf.urls import patterns, include, url
from django.contrib.flatpages import views

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'okech.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^pages/', include('django.contrib.flatpages.urls')),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^teddy/', include('teddy.urls', namespace="teddy")),
)
