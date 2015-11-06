from django.db import models

class Question(models.Model):
    title   = models.CharField( max_length=20)
    slug    = models.SlugField( unique=True)
    likes   = models.IntegerField(default=0)
    text    = models.CharField( max_length=1000)
    date    = models.DateTimeField( auto_now_add=True, blank=True )
    def __unicode__(self):
        return  self.title

class Answer(models.Model):
    title   = models.CharField( max_length=20)
    slug    = models.SlugField( unique=True)
    question = models.ForeignKey( "Question")
    likes   = models.IntegerField(default=0)
    text    = models.CharField( max_length=1000)
    date    = models.DateTimeField( auto_now_add=True, blank=True )
    def __unicode__(self):
        return  self.title

