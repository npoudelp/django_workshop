from django.db import models
from django.utils import timezone
from django.contrib.auth import get_user_model

# Create your models here.

User = get_user_model()

class Users(models.Model):
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    passwd = models.CharField(max_length=255)
    email = models.EmailField()
    address = models.CharField(max_length=50, null=True)

    def __str__(self):
        return self.first_name

class Blog(models.Model):
    # CHOICES = [('Published'), ('Draft'), ('Unpublished')]
    title = models.CharField(max_length=255)
    content = models.TextField()
    date = models.DateField(default=timezone.now())
    author = models.CharField(max_length=25)
    image = models.ImageField(upload_to='blog_photo')
    # status = models.CharField(choices=CHOICES, max_length=50, null=False, default='Draft')
    #author = models.ForeignKey(User, on_delete=models.SET_NULL/models.CASCADE/models.PROTECT, null=True)
    def __str__(self):
        return self.title
    
class Comment(models.Model):
    user_name = models.CharField(max_length=20)
    comment = models.CharField(max_length=255)
    date = models.DateField(default=timezone.now())

    def __str__(self):
        return self.user_name
    
