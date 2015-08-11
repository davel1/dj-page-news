from django.db import models

# Create your models here.

class article(models.Model):
    head = models.TextField()
    text = models.TextField()
    pub_date = models.DateTimeField('data publishing')
    