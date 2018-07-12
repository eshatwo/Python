from django.shortcuts import render, HttpResponse

# Create your views here.
def index(request):
    words = "Hello Yellow"
    return HttpResponse(words)