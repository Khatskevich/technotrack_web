"""technotrack_web URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.8/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
from django.conf.urls import include, url
from django.contrib.auth.decorators import login_required
from django.views.generic import TemplateView
from django.views.generic import ListView
from django.contrib import admin
from . import hello_world_view
from . import views
from . import templates
from loginsys.views import MyUserRegistration, LoginRequest, LogoutRequest
import questions
from questions.views import QuestionsAll
urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'^template/', templates.Index.as_view()),
    url(r'^hw/', hello_world_view.index, name='index'),
    url(r'^$', login_required(QuestionsAll.as_view()), name="search"),
    url(r'^question/', views.Question.as_view(), name='question'),
    url(r'^new_question/', views.NewQuestion.as_view(), name='new_question'),
    url(r'^settings/', views.Settings.as_view(), name='settings'),
    #url(r'^login/', views.Login.as_view(), name='login'),
    url(r'^login/', LoginRequest, name='login'),
    #url(r'^search/', views.Search.as_view(), name='search'),
    url(r'^search/', login_required(QuestionsAll.as_view()), name="search"),

    #url(r'^registration', views.Registration.as_view(), name='registration'),
    url(r'^registration', MyUserRegistration, name='registration'),
    url(r'^logout/', LogoutRequest, name='logout'),
]
