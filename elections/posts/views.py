from django.shortcuts import render
from django.http import HttpResponse
from django.template import RequestContext, loader

from posts.models import Post, Author

def index(request):
    posts = (Post.objects.all()
            .filter(status='p')
            .select_related('author')
            .order_by('-posted_datetime'))
    template = loader.get_template('index.html')
    context = RequestContext(request, {
        'posts': posts,
    })
    return HttpResponse(template.render(context))
