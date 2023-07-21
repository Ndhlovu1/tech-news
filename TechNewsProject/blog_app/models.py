from django.db import models
from django.db.models.query import QuerySet
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse

#Create a specific model
class PublishedManager(models.Manager):
    def get_queryset(self):
        return super(PublishedManager,self).get_queryset().filter(status='published')


#POST TABLE
class Post(models.Model):
    STATUS_CHOICES = (
        ('draft', 'Draft'),
        ('published', 'Published'),
    )
    
    title = models.CharField(max_length=250)
    slug = models.SlugField(max_length = 250, unique_for_date='publish')
    author = models.ForeignKey(User, related_name='blog_app', on_delete=models.CASCADE)
    body = models.TextField()
    publish = models.DateTimeField(default = timezone.now)
    created = models.DateTimeField(auto_now_add = True)
    updated = models.DateTimeField(auto_now = True)
    status = models.CharField(max_length = 10, choices = STATUS_CHOICES, default = 'draft')
        
    objects = models.Manager()#Default Manager
    published = PublishedManager()#Our custom manager
    
    #Used to link specific posts
    def get_absolute_url(self):
        return reverse(
            'blog_app:post_detail',
            args=[
                self.publish.year,
                self.publish.month,
                self.publish.day,
                self.slug]
        )
    
    
    # The class below has meta data and it is requiring django to sort results by the publish field
    class Meta:
        ordering = ('-publish',)
        
    def __str__(self):
        return self.title
    
    
    

