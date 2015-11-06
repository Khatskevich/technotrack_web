from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import TemplateView

class Search(TemplateView):
    template_name = "search.html"

class Registration(TemplateView):
    template_name = "registration.html"

class Login(TemplateView):
    template_name = "login.html"
    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super(Login, self).get_context_data(**kwargs)
        # Add in a QuerySet of all the books
        context['login_error'] = "Hay there!"
        return context

class Settings(TemplateView):
    template_name = "settings.html"

class NewQuestion(TemplateView):
    template_name = "new_question.html"

class Question(TemplateView):
    template_name = "question.html"

class Index(TemplateView):
    template_name = "index.html"