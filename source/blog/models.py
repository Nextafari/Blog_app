from django.db import models
from django.urls import reverse

# Create your models here.
class Post(models.Model):
    """These are going to be contents of each blog post and also columns on the database"""
    title = models.CharField(max_length=255)
    slug = models.SlugField(max_length=255, unique=True)
    summary = models.CharField(max_length=300)
    content = models.TextField()
    published = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True)
    image = models.ImageField(upload_to='img', default='placeholder.png')
		    
    def __unicode__(self):
        return u'%s'% self.title        #this makes the characters in the post show

    class Meta:
        ordering = ["-created"]    #This will help sort the blogpost according to when they were created.


    def get_absolute_url(self):
		#This tells django to come up with urls to the blog posts without the need to hard code the url."""
        return reverse('blog.views.post', args=[self.slug])