from django.db import models
from django.contrib.auth.models import User
from django.conf import settings

# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=100, verbose_name="Post Title")
    image = models.ImageField(upload_to='static/', verbose_name="Post Image")
    content = models.TextField(verbose_name="Post Content")
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, verbose_name="Author")
    date_posted = models.DateTimeField(auto_now_add=True, verbose_name="Date Posted")
    date_updated = models.DateTimeField(auto_now=True, verbose_name="Last Updated")

    class Meta:
        ordering = ('-date_posted',)
        verbose_name = "Blog Post"
        verbose_name_plural = "Blog Posts"

    def __str__(self):
        return self.title
    

