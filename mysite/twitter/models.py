from django.db import models
from django.utils import timezone

# Create your models here.
class Post(models.Model):
    post_text = models.CharField(max_length=255)
    created_on = models.DateTimeField(default=timezone.now())

class User(models.Model):
    username = models.CharField(max_length=150, unique=True)
    first_name = models.CharField(max_length=150)
    second_name = models.CharField(max_length=150)
    email = models.EmailField(unique=True)
    is_active = models.BooleanField()
    posts = models.ForeignKey(Post, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.username
