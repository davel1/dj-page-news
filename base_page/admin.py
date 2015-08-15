from django.contrib import admin
from models import People, GroupList, GroupResource
from import_export.admin import ImportExportActionModelAdmin
# Register your models here.

class PeopleAdmin(admin.ModelAdmin):
    list_display = ('name', 'position')
    fields = ['position', 'name', 'description', 'photo']
    
    
class GroupeAdmin(ImportExportActionModelAdmin):
    list_display = ('group', 'num')
    fields = ['group', 'num', 'name', 'register']
    resource_class = GroupResource
    
admin.site.register(People, PeopleAdmin)
admin.site.register(GroupList, GroupeAdmin)