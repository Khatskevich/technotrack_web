from django.contrib import admin
from questions.models import Question, Answer

class QuestionAdmin(admin.ModelAdmin):
    prepopulated_fields = { 'slug': ('title',)}
    list_display = ( 'title', 'likes', 'text', 'date')
    search_fields = ['title']

class AnswerAdmin(admin.ModelAdmin):
    prepopulated_fields = { 'slug': ('title',)}
    list_display = ( 'title', 'likes', 'text', 'date')
    search_fields = ['title']

admin.site.register(Question, QuestionAdmin)
admin.site.register(Answer, AnswerAdmin)