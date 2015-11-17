from django.db import models
from tag.models import Tag


class Question(models.Model):
    title   = models.CharField( max_length=20)
    likes   = models.IntegerField(default=0)
    text    = models.TextField( )
    image_url = models.CharField( max_length=20)
    date    = models.DateTimeField( auto_now_add=True, blank=True )
    tags = models.ManyToManyField( Tag)
    @staticmethod
    def get_query_sorted_by_publish_date():
        return Question.objects.order_by('date')
    @staticmethod
    def get_query_sorted_by_title():
        return Question.objects.order_by('title')
    @staticmethod
    def get_query_sorted_by_likes():
        return Question.objects.order_by('likes')
    def __unicode__(self):
        return  self.title


