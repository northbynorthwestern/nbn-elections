from django.db import models

STATUS_CHOICES = (
    ('d', 'Draft'),
    ('p', 'Read Me'),
    ('p', 'Edited'),
    ('p', 'Published'),
)

class Author(models.Model):
    name = models.CharField(max_length=100, unique=True)

    def __unicode__(self):
    	return self.name

class Post(models.Model):
    title = models.CharField(max_length=100, unique=True)
    slug = models.SlugField(max_length=100, unique=True)
    body = models.TextField()
    posted_datetime = models.DateTimeField(auto_now_add=True, db_index=True)
    author = models.ManyToManyField('Author', null=True, blank=True)
    status = models.CharField(max_length=1, choices=STATUS_CHOICES, default='d')

    def __unicode__(self):
    	return self.title
