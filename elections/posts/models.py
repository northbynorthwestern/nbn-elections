from django.db import models
# from tinymce.models import HTMLField
from localflavor.us.models import USStateField
from datetime import datetime
import statestyle

class Author(models.Model):
    name = models.CharField(max_length=100, unique=True)

    def __unicode__(self):
    	return self.name


class Post(models.Model):
    DRAFT = 'd'
    README = 'r'
    EDITED = 'e'
    PUBLISHED = 'p'
    STATUS_CHOICES = (
        (DRAFT, 'Draft'),
        (README, 'Read Me'),
        (EDITED, 'Edited'),
        (PUBLISHED, 'Published'),
    )

    title = models.CharField(max_length=100, unique=True, null=True)
    slug = models.SlugField(max_length=100, unique=True, null=True)
    author = models.ManyToManyField('Author', null=True, blank=True)
    state = USStateField(null=True)
    body = models.TextField(null=True)
    posted_datetime = models.DateTimeField(auto_now_add=True, db_index=True, null=True)
    status = models.CharField(max_length=1,
                            choices=STATUS_CHOICES,
                            default=DRAFT, null=True)

    def __unicode__(self):
    	return self.title

    def is_published(self):
        return self.status == self.PUBLISHED

    @property
    def stateface(self):
        a = statestyle.get(self.state)
        return a.stateface

