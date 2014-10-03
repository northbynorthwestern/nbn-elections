from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.views.generic.base import RedirectView

from posts import views

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'elections.views.home', name='home'),
    # url(r'^posts/', include('posts.urls')),

    (r'^elections/tinymce/', include('tinymce.urls')),

    url(r'^elections/2014/post/(?P<slug>[\w-]+)/$', views.PostView.as_view(), name='post'),
    url(r'^elections/2014', views.LandingView.as_view(), name='landing'),
    url(r'^elections/', RedirectView.as_view(url='/elections/2014/'), name='redirect-to-landing'),
    url(r'^elections/proxy/(?P<race>.*)', views.ProxyView.as_view(), name='proxy'),

    url(r'^elections/admin/', include(admin.site.urls)),
)
