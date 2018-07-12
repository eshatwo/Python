from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Quote, QuoteManager, User, UserManager
from datetime import datetime

# Create your views here.
def welcome(request):
    if not 'user_id' in request.session:
        messages.add_message(request, messages.INFO, "Please make an account or register first", extra_tags = 'login')
        return redirect ('/')
    context = {
        'my_likes': User.objects.get(id=request.session['user_id']).my_likes.all(),
        'all_quotes': Quote.objects.exclude(users_liked = request.session['user_id']),
        'user': User.objects.get(id=request.session['user_id']),
        'creator': Quote.objects.get(id=request.session['user_id']).creator,
        'likes': User.objects.count()
    }
    return render (request, 'quote/welcome.html', context)

def add(request):
    if not 'user_id' in request.session:
        messages.add_message(request, messages.INFO, "Please make an account or register first", extra_tags = 'login')
        return redirect ('/')
    return render (request, 'quote/add.html')

def adding(request):
    errors = Quote.objects.quote_validator(request.POST)
    if errors:
        for tag,error in errors.items():
            messages.error(request, error, extra_tags=tag)
        return redirect ('/add')
    else:
        quote = Quote.objects.create(author = request.POST['author'], content = request.POST['content'], creator=User.objects.get(id=request.session['user_id']))
        return redirect('/welcome')

def profile(request, number):
    if not 'user_id' in request.session:
        messages.add_messgae(request, messages.INFO, "Please make an account or register first", extra_tags = 'login')
        return redirect ('/')
    quote = Quote.objects.get(id=number)
    context = {
        'author': quote.author,
        'content': quote.content,
        'creator': quote.creator
    }
    return render (request, 'quote/profile.html', context)

def delete(request, number):
    quote = Quote.objects.get(id=number)
    quote.delete()
    return redirect('/welcome')

def edit(request):
    user_to_edit = User.objects.get(id=request.session['user_id'])
    return render(request, 'quote/edit.html', {'user': user_to_edit})

def update(request):
    user = User.objects.get(id=request.session['user_id'])
    user.first_name = request.POST['first_name']
    user.last_name = request.POST['last_name']
    user.email = request.POST['email']
    user.save()
    return redirect ('/welcome')