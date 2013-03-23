from django.conf.urls.defaults import patterns, url
from dummy.demo import views

urlpatterns = patterns('',
    url(r'^$', views.Index),
    url(r'^location/(?P<locationslug>.*)/$', views.Index_Location),
)