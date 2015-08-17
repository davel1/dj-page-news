from django.db import models
from import_export import resources
from django.contrib.auth.models import AbstractUser, UserManager
# Create your models here.

class People(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=120)
    description = models.TextField()
    position = models.CharField(max_length=30)
    photo = models.FileField(upload_to='photos')
    
class GroupList(models.Model):
    group = models.CharField(max_length = 30)
    num = models.PositiveIntegerField()
    name = models.CharField(max_length = 120)
    register = models.NullBooleanField(default = False)
    def __str__(self):
        return "%s" % self.num
    
class GroupResource(resources.ModelResource):
    class Meta:
        model = GroupList
        #fields = ('group', 'num', 'name')

class MyUser(AbstractUser):
    num = models.PositiveIntegerField(default  = 0)
