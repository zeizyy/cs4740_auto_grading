from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'auto_grading.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^', include('grading.urls')),
)
