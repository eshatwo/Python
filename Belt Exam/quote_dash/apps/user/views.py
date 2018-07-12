from django.shortcuts import render, redirect
from django.contrib import messages
from .models import *
import bcrypt

# Create your views here.

def index(request):
    return render(request, 'user/index.html')

def register(request):
    errors = User.objects.register_validator(request.POST)
    if len(errors):
        for tag,error in errors.items():
            messages.error(request, error, extra_tags=tag)
        return redirect('/')
    else:
        pwhash = bcrypt.hashpw(request.POST['password'].encode(), bcrypt.gensalt())
        user = User.objects.create(first_name = request.POST['first_name'], last_name = request.POST['last_name'], email = request.POST['email'], password = pwhash)
        request.session['name'] = request.POST['first_name']
        request.session['user_id'] = user.id
        messages.add_message(request, messages.INFO, "Hello, {}! Welcome to Trip Buddy!".format(request.session['name']), extra_tags='user')
        return redirect ('/welcome')
    return redirect('/')
        
def login(request):
    errors = User.objects.login_validator(request.POST)
    if len(errors):
        for tag,error in errors.items():
            messages.error(request, error, extra_tags=tag)
        return redirect ('/')   
    else:
        request.session['name'] = User.objects.get(email=request.POST['email']).first_name
        request.session['user_id'] = User.objects.get(email=request.POST['email']).id
        return redirect ('/welcome')
        
def logout(request):
    request.session.flush()
    messages.add_message(request, messages.INFO, "Logged Out", extra_tags= 'logout')
    return redirect ('/')