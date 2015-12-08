from django.db import models
from loginsys.models import User
from questions.models import Question


class Answer(models.Model):
    title   = models.CharField( max_length=20)
    question = models.ForeignKey( Question)
    likes   = models.IntegerField(default=0)
    user = models.ForeignKey(User)
    text    = models.TextField( )
    date    = models.DateTimeField( auto_now_add=True, blank=True )
    def __unicode__(self):
        return  self.title
