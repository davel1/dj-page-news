from django.db import models
from ckeditor.fields import RichTextField

# Create your models here.

class article(models.Model):
    head = models.TextField()
    text = RichTextField()
    pub_date = models.DateTimeField(auto_now = True)
    