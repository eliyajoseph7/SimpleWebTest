from django.db import models

# Create your models here.
class Author(models.Model):
    user_name = models.CharField(max_length=20)
    password = models.CharField(max_length=11)
    email = models.CharField(max_length=25)
    
class parallaxImg(models.Model):
    image = models.ImageField()
 