from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    return HttpResponse("Rango says hey there partner!<br/><br/><a href='/rango/about/'>About</a>")
    #hyperlink added

# Chapter 3 Exercise
# Create the new view method:
def about(request):
    return HttpResponse("Rango says here is the about page.<br/><br/><a href='/rango/'>Index</a>")
    #hyperlink added

