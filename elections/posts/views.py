from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from django.template import RequestContext, loader
from django.views.generic import TemplateView

from posts.models import Post, Author

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
