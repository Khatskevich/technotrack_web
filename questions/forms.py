from django import forms
from django.forms import ModelForm
from questions.models import Question


class NewQuestionForm(ModelForm):
    tags = forms.CharField(required=False)
    class Meta:
        model = Question
        fields = ( 'title', 'text', 'tags',)

