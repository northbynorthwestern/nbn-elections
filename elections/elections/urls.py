from django.conf.urls import patterns, include, url
from django.contrib import admin

from posts import views

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'elections.views.home', name='home'),
    # url(r'^posts/', include('posts.urls')),
    # (r'^tinymce/', include('tinymce.urls')),

    url(r'^$', views.LandingView.as_view(), name='landing'),
    url(r'^post/(?P<slug>[\w-]+)/$', views.PostView.as_view(), name='post'),
    url(r'^proxy/(?P<race>.*)', views.ProxyView.as_view(), name='proxy'),

    url(r'^admin/', include(admin.site.urls)),

)
