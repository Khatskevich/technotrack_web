from django.db import models
from answer.models import Answer
from loginsys.models import User
from questions.models import Question


class LikeQuestion(models.Model):
    question = models.ForeignKey(Question)
    user = models.ForeignKey(User)

class LikeAnswer(models.Model):
    answer = models.ForeignKey(Answer)
    user = models.ForeignKey(User)
