from django.db import models

# Create your models here.


class question(models.Model):
    q = models.TextField()
    q_date = models.DateTimeField('data quote')
    
class answer(models.Model):
    r = models.TextField()
    r_date = models.DateTimeField('data request')
    public = models.BooleanField()
    child = models.ForeignKey(question)