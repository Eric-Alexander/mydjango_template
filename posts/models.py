from __future__ import unicode_literals

from django.db import models

class Post(models.Model):
    title = models.CharField(max_length=222)
    content = models.TextField()
    updated_at = models.DateTimeField(auto_now=True, auto_now_add=False)
    created_at = models.DateTimeField(auto_now=False, auto_now_add=True)

#python 2.7
    def __unicode__(self):
        return self.title

#python 3
    def __str__(self):
        return self.title
