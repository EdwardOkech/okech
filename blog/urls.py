from django.conf.urls import patterns, include, url
from blog import views

##admin.autodiscover()

urlpatterns = patterns('',
   
             url(r'^$', views.main, name='main'),
##             url(r'^list/$', views.list, name='list'),
            url(r'^post(\d+)/$',views.post, name='post'),
            url(r'^add_comment/(\d+)/$','add_comment'),
            url(r'^month/(\d+)/(\d+)/$',views.month, name='month'),
    
)
