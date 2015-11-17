from django.shortcuts import render_to_response
from django.template import RequestContext
from django.views.generic import ListView
from questions.models import Question
from django.contrib.auth.decorators import login_required


class QuestionsAll(ListView):
    def get_queryset(self):
        if 'sort' in self.request.GET.keys():
            if self.request.GET['sort']=='title':
                return Question.get_query_sorted_by_title()
            if self.request.GET['sort']=='date':
                return Question.get_query_sorted_by_publish_date()
            if self.request.GET['sort']=='likes':
                return Question.get_query_sorted_by_likes()
        return Question.objects.all()
    model = Question
    paginate_by = '15'
    context_object_name = "questions"
    template_name='search.html'
