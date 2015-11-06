from django.shortcuts import render_to_response
from django.template import RequestContext
from django.views.generic import ListView
from questions.models import Question, Answer
from django.contrib.auth.decorators import login_required


class QuestionsAll(ListView):
    model = Question
    paginate_by = '5'
    queryset = Question.objects.all()
    context_object_name = "questions"
    template_name='search.html'
