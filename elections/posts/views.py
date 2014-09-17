from django.shortcuts import render
from django.http import HttpResponse
from django.template import RequestContext, loader

from posts.models import Post, Author

def index(request):
    posts = Post.objects.all()
    template = loader.get_template('index.html')
    context = RequestContext(request, {
        'posts': posts,
    })
    return HttpResponse(template.render(context))