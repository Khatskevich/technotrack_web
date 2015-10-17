from django.shortcuts import render
from django.http import HttpResponse
def index( request):
    return HttpResponse("Hi, valera!" + request.GET.get("q", "") + request.GET.get("y", "") )

# Create your views here.