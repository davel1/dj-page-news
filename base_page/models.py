from django.db import models

# Create your models here.

class People(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=120)
    description = models.TextField()
    position = models.CharField(max_length=30)
    photo = models.FileField(upload_to='photos')
    
