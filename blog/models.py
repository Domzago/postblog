from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Post(models.Model):
    title = models.CharField(max_length=200)
    intro = models.CharField(max_length=1000)
    created = models.ForeignKey(User, related_name='posts', on_delete=models.CASCADE)
    date = models.DateTimeField(auto_now_add=True)
    body = models.TextField()


    class Meta:
        ordering = ['-date']


    def __str__(self) -> str:
        return self.title
