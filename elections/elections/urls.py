from django.conf.urls import patterns, include, url
from django.contrib import admin

from posts import views

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'elections.views.home', name='home'),
    # url(r'^posts/', include('posts.urls')),
    # (r'^tinymce/', include('tinymce.urls')),

    url(r'^$', views.index, name='index'),
    url(r'^admin/', include(admin.site.urls)),
)
