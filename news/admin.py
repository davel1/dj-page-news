from django.contrib import admin

# Register your models here.
from models import article

class ArticleAdmin(admin.ModelAdmin):
    list_display = ('head', 'pub_date')
    fields = ['head', 'text']
    
admin.site.register(article,ArticleAdmin)
