from django.db import models

# Create your models here.


class quote(models.Model):
    q = models.TextField()
    q_date = models.DateTimeField('data quote')
    r = models.TextField()
    r_date = models.DateTimeField('data request')
    public = models.BooleanField()
    