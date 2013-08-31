from django.conf.urls import patterns, url

from venues import views

urlpatterns = patterns('',
    url(r'^$', views.index, name='index'),
    url(r'^(?P<venue_id>\d+)/$', views.detail, name='detail')
)
