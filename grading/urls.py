from django.conf.urls import patterns, include, url
from grading import views

urlpatterns = patterns('',
    url(r'^$', views.index, name='Index'),
    url(r'^upload/$', views.upload, name='Upload'),
)