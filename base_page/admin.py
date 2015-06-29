from django.contrib import admin
from models import People

# Register your models here.

class PeopleAdmin(admin.ModelAdmin):
    list_display = ('name', 'position')
    fields = ['position', 'name', 'description', 'photo']
    
admin.site.register(People, PeopleAdmin)