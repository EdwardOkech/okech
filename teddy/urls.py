from django.conf.urls import patterns, include, url
from django.contrib.flatpages import views
from teddy import views



urlpatterns = patterns('django.contrib.flatpages.views',
   
            
             url(r'^$', views.index, name='index'),
##             url(r'^about/$', 'flatpage', {'url':'/about/'}, name='about'),
            url(r'^about/$', views.about, name='about'),
            url(r'^projects/$', views.projects, name='projects'),
            url(r'^hobbies/$', views.hobbies, name='hobbies'),
            url(r'^hire/$', views.hire, name='hire'),
            url(r'^thanks/$', views.hire, name='thanks'),
)

