from django.contrib import admin
from models import People, GroupList, GroupResource, MyUser, Honors, ModDate
from import_export.admin import ImportExportActionModelAdmin
from django.contrib.auth.admin import UserAdmin
from django.utils.translation import ugettext, ugettext_lazy as _

# Register your models here.

class PeopleAdmin(admin.ModelAdmin):
    list_display = ('name', 'position')
    fields = ['position', 'name', 'description', 'photo']
    
    
class GroupeAdmin(ImportExportActionModelAdmin):
    list_display = ('group', 'num')
    fields = ['group', 'num', 'name', 'register']
    resource_class = GroupResource

class MyUserAdmin(UserAdmin):
    fieldsets = (
        (None, {'fields': ('username', 'password')}),
        (_('Personal info'), {'fields': ('first_name', 'last_name', 'email')}),
        (_('Student info'), {'fields': ('stud_full_name', 'num', 'student')}),      
        (_('Permissions'), {'fields': ('is_active', 'is_staff', 'is_superuser',
                                       'groups', 'user_permissions')}),
        (_('Important dates'), {'fields': ('last_login', 'date_joined')}),
    )

    
admin.site.register(People, PeopleAdmin)
admin.site.register(GroupList, GroupeAdmin)
admin.site.register(MyUser, MyUserAdmin)
admin.site.register(Honors)
admin.site.register(ModDate)