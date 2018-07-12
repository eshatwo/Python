from django.shortcuts import render, HttpResponse, redirect

def index(req):
    response = "placeholder to later display all the list of blogs"
    return HttpResponse(response)

def new(req):
    response = "placeholder to display a new form to create a new blog"
    return HttpResponse(response)

def create(req):
    return redirect("/")

def show(req, number):
    response = f'placeholder to display blog {number}'
    return HttpResponse(response)

def edit(req, number):
    response = f'placeholder to edit blog {number}'
    return HttpResponse(response)

def destroy(req, number):
    return redirect("/")



