from django.contrib import admin
from questions.models import Question

class QuestionAdmin(admin.ModelAdmin):
    list_display = ( 'title', 'likes', 'text', 'date')
    search_fields = ['title']
admin.site.register(Question, QuestionAdmin)

