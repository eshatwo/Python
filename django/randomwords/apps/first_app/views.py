from django.shortcuts import render, redirect, HttpResponse
from django.utils.crypto import get_random_string

# Create your views here.
def index(request):
    random = {
        "word": get_random_string(length=14)
        } 
    if 'count' in request.session:
        request.session['count'] += 1
    else:
        request.session['count'] = 1
    print(request.session)
    return render(request, "first_app/index.html", random)

def reset(request):
    request.session.pop('count')
    return redirect("/random_word")