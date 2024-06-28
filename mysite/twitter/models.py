from django.db import models
from django.utils import timezone
from django.contrib.auth import get_user_model

# Create your models here.
    
class Post(models.Model):
    post_text = models.CharField(max_length=255)
    created_on = models.DateTimeField(default=timezone.now)
    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE, related_name='posts')

    def __str__(self):
        return self.post_text

User = get_user_model()
