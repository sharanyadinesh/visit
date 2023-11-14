

from django.db import models

# Create your models here.
class Visit(models.Model):
    Place=models.CharField(max_length=250)
    Photo=models.ImageField(upload_to='image')
    Wrt=models.TextField()

class Team(models.Model):
    Name=models.CharField(max_length=250)
    Picture=models.ImageField(upload_to='foto')
    About=models.TextField()

class Company(models.Model):
    Travel=models.CharField(max_length=250)
    File=models.ImageField(upload_to='jpg')
    Doc=models.TextField()