from django.shortcuts import render, HttpResponse 

# Create your views here.
def index(req):
    response = 'Hello, world!'
    return HttpResponse(response)