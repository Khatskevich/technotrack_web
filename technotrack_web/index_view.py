from django.shortcuts import render
from django.http import HttpResponse
def index( request):
    static_index_file = open(mode='r',name="technotrack_web/index.html")
    return HttpResponse( static_index_file.read() )

    # Create your views here.