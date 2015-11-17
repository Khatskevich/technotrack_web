from django.contrib import admin
from answer.models import Answer

class AnswerAdmin(admin.ModelAdmin):
    list_display = ( 'title', 'likes', 'text', 'date')
    search_fields = ['title']



admin.site.register(Answer, AnswerAdmin)
