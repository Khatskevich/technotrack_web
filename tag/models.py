from django.db import models

class Tag(models.Model):
    name   = models.CharField( unique=True ,max_length=20)
    def __unicode__(self):
        return  self.name