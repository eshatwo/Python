from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Job, JobManager, User, UserManager
from datetime import datetime

# Create your views here.
def welcome(request):
    if not 'user_id' in request.session:
        messages.add_message(request, messages.INFO, "Please make an account or register first", extra_tags = 'login')
        return redirect ('/')
    context = {
        'jobs': User.objects.get(id=request.session['user_id']).jobs.all(),
        'all_jobs': Job.objects.exclude(users__id = request.session['user_id']),
        'user': User.objects.get(id=request.session['user_id'])
    }
    return render (request, 'helper/welcome.html', context)

def add(request):
    if not 'user_id' in request.session:
        messages.add_message(request, messages.INFO, "Please make an account or register first", extra_tags = 'login')
        return redirect ('/')
    return render (request, 'helper/add.html')

def adding(request):
    errors = Job.objects.job_validator(request.POST)
    if len(errors):
        for tag,error in errors.items():
            messages.error(request, error, extra_tags=tag)
        return redirect ('/add')
    else:
        job = Job.objects.create(title = request.POST['title'], description = request.POST['description'], location = request.POST['location'], creator=User.objects.get(id=request.session['user_id']))
        return redirect('/welcome')

def job(request, number):
    if not 'user_id' in request.session:
        messages.add_messgae(request, messages.INFO, "Please make an account or register first", extra_tags = 'login')
        return redirect ('/')
    job = Job.objects.get(id=number)
    context = {
        'title': job.title,
        'description': job.description,
        'location': job.location,
        'creator': job.creator,
        'all_users': job.users.all(),
    }
    return render (request, 'helper/job.html', context)

def join(request, number):
    job = Job.objects.get(id=number)
    job.save()
    newuser = User.objects.get(id=request.session['user_id'])
    newuser.save()
    job.users.add(newuser)
    return redirect ('/welcome')

def cancel(request, number):
    job = Job.objects.get(id=number)
    job.save()
    user = User.objects.get(id=request.session['user_id'])
    user.save()
    job.users.remove(user)
    if not job.users.all():
        job.delete()
    return redirect ('/welcome')

def delete(request, number):
    job = Job.objects.get(id=number)
    job.delete()
    return redirect('/welcome')

def edit(request, number):
    job_to_edit = Job.objects.get(id=number)
    return render(request, 'helper/edit.html', {'job': job_to_edit})

def update(request, number):
    job = Job.objects.get(id=number)
    job.title = request.POST['title']
    job.description = request.POST['description']
    job.location = request.POST['location']
    job.save()
    return redirect ('/welcome')