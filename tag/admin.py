from django.contrib import admin
from tag.models import Tag


class TagAdmin(admin.ModelAdmin):
    list_display = ( 'pk', 'name')
    search_fields = ['title']



admin.site.register(Tag, TagAdmin)
