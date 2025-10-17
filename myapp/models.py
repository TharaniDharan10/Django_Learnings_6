from django.db import models

# Create your models here.
class User(models.Model):
    name=models.CharField(max_length=255)
    city=models.CharField(max_length=255)

class Profile(models.Model):
    user=models.OneToOneField(User, on_delete=models.CASCADE)
    bio=models.TextField()