from django.contrib import admin
from likes.models import LikeQuestion, LikeAnswer


class LikeQuestionAdmin(admin.ModelAdmin):
    list_display = ( 'user', 'question')
class LikeAnswerAdmin(admin.ModelAdmin):
    list_display = ( 'user', 'answer')

admin.site.register(LikeQuestion, LikeQuestionAdmin)
admin.site.register(LikeAnswer, LikeAnswerAdmin)