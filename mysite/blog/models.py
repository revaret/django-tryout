'''importing modules'''
from django.db import models
from django.utils import timezone

# Create your models here.
class Post(models.Model):
    '''Model post with attributes author,title,text,
    create date and publish date and method publish'''
    author = models.ForeignKey('auth.user')
    title = models.CharField(max_length=200)
    text = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)
    published_date = models.DateTimeField(blank=True, null=True)

    def publish(self):
        ''' publish method for publishing the
        blog'''
        self.published_date = timezone.now()
        self.save

    def __str__(self):
        return self.title
