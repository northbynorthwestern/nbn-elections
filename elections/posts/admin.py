from django.contrib import admin

from elections.posts.models import Author, Post

admin.site.register(Post)
admin.site.register(Author)
