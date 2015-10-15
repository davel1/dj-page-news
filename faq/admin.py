from django.contrib import admin
from models import question, answer

# Register your models here.

class AnswerInline(admin.StackedInline):
    model = answer
    extra = 1
    
class QuestionAdmin(admin.ModelAdmin):
    list_display = ('q', 'q_date')
    fields = ['q', ]
    inlines = [AnswerInline] 

admin.site.register(question, QuestionAdmin)
