from django.db import models
from django.db.models.signals import post_save
from django.contrib.auth.models import User
# Create your models here.

class MyUser( models.Model):
    user = models.OneToOneField(User)
    nickName = models.CharField(max_length=50)

    def __unicode__(self):
        return  self.nickName

def create_MyUser_with_User( sender, instance, **kwargs):
    myUser, new = MyUser.objects.get_or_create(user=instance)
post_save.connect( create_MyUser_with_User, User)