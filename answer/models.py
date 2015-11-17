from django.db import models
from questions.models import Question


class Answer(models.Model):
    title   = models.CharField( max_length=20)
    question = models.ForeignKey( Question)
    likes   = models.IntegerField(default=0)
    text    = models.TextField( )
    date    = models.DateTimeField( auto_now_add=True, blank=True )
    def __unicode__(self):
        return  self.title
