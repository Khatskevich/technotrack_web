from django.db import models
from loginsys.models import User
from tag.models import Tag
from django.utils.translation import ugettext_lazy as _

class Question(models.Model):
    title   = models.CharField( max_length=20)
    likes   = models.IntegerField(default=0)
    text    = models.TextField( )
    user = models.ForeignKey(User)
    date    = models.DateTimeField( auto_now_add=True, blank=True )
    tags = models.ManyToManyField( Tag)
    @staticmethod
    def get_query_sorted_by_publish_date():
        return Question.objects.order_by('-date')
    @staticmethod
    def get_query_sorted_by_title():
        return Question.objects.order_by('-title')
    @staticmethod
    def get_query_sorted_by_likes():
        return Question.objects.order_by('-likes')
    def __unicode__(self):
        return  self.title


