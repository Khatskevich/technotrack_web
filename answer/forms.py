from django import forms
from django.forms import ModelForm
from answer.models import Answer
from questions.models import Question


class NewAnswerForm(ModelForm):
    class Meta:
        model = Answer
        fields = ( 'title', 'text')

