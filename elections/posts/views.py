import json

from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from django.template import RequestContext, loader
from django.views.generic import TemplateView, View
import requests

from elections.posts.models import Post, Author, Race


class JSONResponse(HttpResponse):
    def __init__(self, data, request, *args, **kwargs):
        super(JSONResponse, self).__init__(json.dumps(data), *args, **kwargs)

class LandingView(TemplateView):
    template_name = 'index.html'

    def get_context_data(self, **kwargs):
        context = super(LandingView, self).get_context_data(**kwargs)

        posts = (Post.objects.all()
                .filter(status='p')
                .select_related('author')
                .order_by('-posted_datetime'))
        context['posts'] = posts
        return context


class PostView(TemplateView):
    template_name = 'post.html'

    def get_context_data(self, **kwargs):
        context = super(PostView, self).get_context_data(**kwargs)
        post = get_object_or_404(Post, slug=self.kwargs['slug'])
        context['post'] = post
        return context

class ProxyView(View):
    def get(self, request, *args, **kwargs):
        url = 'http://elections.huffingtonpost.com/pollster/api/charts/' + self.kwargs['race']
        print url
        return self.handle_response(url)

    def handle_response(self, url):
        r = requests.get(url)
        return HttpResponse(json.dumps(r.json()), content_type="application/json")


class Handle404View(TemplateView):
    template_name = '404.html'

    def get_context_data(self, **kwargs):
        context = super(Handle404View, self).get_context_data(**kwargs)
        return context

