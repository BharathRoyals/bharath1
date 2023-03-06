from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

def flower(request):
    return HttpResponse('<h1>i propose with my rose and will propose</h1>')


def dileep(request):
    return HttpResponse('<marquee><h1> can not using inner wear</marquee></h1>')