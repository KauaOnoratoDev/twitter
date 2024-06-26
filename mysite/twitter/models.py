from django.db import models
from django.utils import timezone

# Create your models here.

class User(models.Model):
    username = models.CharField(max_length=150, unique=True)
    first_name = models.CharField(max_length=150)
    email = models.EmailField(unique=True)
    is_active = models.BooleanField()
    password = models.CharField(max_length=150)
    
    def __str__(self):
        return self.username
    
class Post(models.Model):
    post_text = models.CharField(max_length=255)
    created_on = models.DateTimeField(default=timezone.now)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='posts')

    def __str__(self):
        return self.post_text
