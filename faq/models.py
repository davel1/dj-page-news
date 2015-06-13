from django.db import models

# Create your models here.


class question(models.Model):
    q = models.TextField('Question')
    q_date = models.DateTimeField('Date insert')
    
class answer(models.Model):
    r = models.TextField('Answer')
    r_date = models.DateTimeField('Date add answer')
    public = models.BooleanField('Public')
    child = models.ForeignKey(question)