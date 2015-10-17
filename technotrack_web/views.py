from django.shortcuts import render
from django.http import HttpResponse
def index( request):
    static_index_file = open(mode='r',name="technotrack_web/index.html")
    return HttpResponse( static_index_file.read() )

def question( request):
    static_index_file = open(mode='r',name="technotrack_web/question.html")
    return HttpResponse( static_index_file.read() )

def new_question( request):
    static_index_file = open(mode='r',name="technotrack_web/new_question.html")
    return HttpResponse( static_index_file.read() )

def settings( request):
    static_index_file = open(mode='r',name="technotrack_web/settings.html")
    return HttpResponse( static_index_file.read() )

def login( request):
    static_index_file = open(mode='r',name="technotrack_web/login.html")
    return HttpResponse( static_index_file.read() )

def registration( request):
    static_index_file = open(mode='r',name="technotrack_web/registration.html")
    return HttpResponse( static_index_file.read() )

def search( request):
    static_index_file = open(mode='r',name="technotrack_web/search.html")
    return HttpResponse( static_index_file.read() )
