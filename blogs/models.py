from pyexpat import model
from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Blog(models.Model):
    text = models.CharField(max_length=200)
    date_added = models.DateTimeField(auto_now_add=True)
    owner = models.ForeignKey(User,on_delete=models.CASCADE)
    def __str__(self):
        return self.text
class BlogPost(models.Model):
    blog = models.ForeignKey(Blog,on_delete=models.CASCADE)
    post = models.TextField()
    date_added = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return f'{self.post[:50]},,,'