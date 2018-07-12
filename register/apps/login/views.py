from django.shortcuts import render, HttpResponse, redirect
from django.contrib import messages
from django.contrib.messages import get_messages
from .models import *
import bcrypt

# Create your views here.
def index(request):
    return render (request, 'login/index.html')

def register(request):
    print (request.POST)
    msg = User.objects.basic_validator(request.POST)
    if len(msg):
        hashedpw = bcrypt.hashpw(request.POST['password'].encode(), bcrypt.gensalt())
        User.objects.create(first_name = request.POST['first_name'], last_name = request.POST['last_name'], email = request.POST['email'], password = hashedpw)
        user = User.objects.last()
        request.session['logged_in'] = user.id
        return redirect('/success')
    return redirect('/')   

def login(request):
	msg = User.objects.login_validator(request.POST)
	if len(msg):
		print (msg)
	else:
		user = User.objects.get(email=request.POST['email'])
		request.session['logged_in'] = user.id
		return redirect('/success')
	return redirect('/')

def success(request):
    if User.objects.get(id=request.session['logged_in']) == User.objects.last():
        status = 'Signed Up'
    else:
        status = 'Logged In'

    context = {'user': User.objects.get(id=request.session['logged_in']), 'status': status}
    return render(request, 'login/success.html', context)


