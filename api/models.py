from django.db import models

# Create your models here.

class blood_doner(models.Model):
    name = models.CharField(max_length=20)
    age = models.IntegerField(max_length=3)
    bGroup = models.CharField(max_length=10)
    phone = models.IntegerField(max_length=13)
    
    def __str__(self):
        return self.name