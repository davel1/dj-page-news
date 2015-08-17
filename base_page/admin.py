from django.contrib import admin
from models import People, GroupList, GroupResource, MyUser
from import_export.admin import ImportExportActionModelAdmin
from django.contrib.auth.admin import UserAdmin
# Register your models here.

class PeopleAdmin(admin.ModelAdmin):
    list_display = ('name', 'position')
    fields = ['position', 'name', 'description', 'photo']
    
    
class GroupeAdmin(ImportExportActionModelAdmin):
    list_display = ('group', 'num')
    fields = ['group', 'num', 'name', 'register']
    resource_class = GroupResource
    
class MyUserAdmin(UserAdmin):
    pass

    
admin.site.register(People, PeopleAdmin)
admin.site.register(GroupList, GroupeAdmin)
admin.site.register(MyUser, MyUserAdmin)