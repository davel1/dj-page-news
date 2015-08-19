from django.db import models
from import_export import resources
from django.contrib.auth.models import AbstractUser, UserManager
from django.conf import settings
import datetime
from django.utils import timezone
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
    def __unicode__(self):
        return "%s: %s" % (self.group, self.name)
    
class GroupResource(resources.ModelResource):
    class Meta:
        model = GroupList
        #fields = ('group', 'num', 'name')

class MyUser(AbstractUser):
    num = models.PositiveIntegerField(default  = 0)
    stud_full_name = models.CharField(max_length = 120)
    student = models.BooleanField(default = False)
    
    def __unicode__(self):
        if self.student:
            return self.stud_full_name
        return self.get_full_name()
        
    def is_student(self):
        if self.student:
            return True
        return False
    
class Honors(models.Model):
    student = models.ForeignKey(GroupList)
    photo = models.FileField(upload_to='honors')
    article = models.CharField(max_length = 60)
    description = models.TextField()
    date_event = models.DateTimeField()
    def __unicode__(self):
        return self.article
    
class ModDate(models.Model):
    current_date = models.DateField()
    mod = models.BooleanField()
    
    def __unicod__(self):
        if self.mod:
            return str('numerator')
        return str('denominator')
    
    def get_mod(self):
      #  if (timezone.now() - self.current_date) > datetime.date(day = 7):
      #      self.mod = not self.mod
        return self.__unicod__()
    
    