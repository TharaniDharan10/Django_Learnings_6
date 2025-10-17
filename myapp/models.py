from django.db import models

# Create your models here.
class User(models.Model):
    name=models.CharField(max_length=255)
    city=models.CharField(max_length=255)

class Profile(models.Model):
    user=models.OneToOneField(User, on_delete=models.CASCADE)
    bio=models.TextField()

class Book(models.Model):
    # one to many 
    author=models.ForeignKey(User, on_delete=models.CASCADE)
    title=models.CharField(max_length=100)