from django.shortcuts import render
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
        # posts = Post.objects.all()
        context['posts'] = posts
        return context
