from django.shortcuts import render, HttpResponse, redirect
from datetime import datetime
import random

# Create your views here.
def process(request):
    if 'gold' in request.session:
        print(request.session['gold'])
    elif 'activities' not in request.session:
        request.session['activities'] = []
        request.session['gold']= 0
    return render(request, 'first_app/index.html' )

def money(request):
    now = datetime.now().strftime("%Y/%m/%d %I:%M%p")
    if 'farm' in request.POST:
        rand = random.randrange(10,21)
        print('rand')
        request.session['gold'] += rand
        phrase = f"<p class='green'>You have earned {rand} golds from the farm {now}</p>"
        request.session['activities'] = request.session['activities'] + [phrase]
    if 'cave' in request.POST:
        rand = random.randrange(5,11)
        print('rand')
        request.session['gold'] += rand
        phrase = f"<p class='green'>You have earned {rand} golds from the farm {now}</p>"
        request.session['activities'] = request.session['activities'] + [phrase]
    if 'house' in request.POST:
        rand = random.randrange(2,6)
        print('rand')
        request.session['gold'] += rand
        phrase = f"<p class='green'>You have earned {rand} golds from the farm {now}</p>"
        request.session['activities'] = request.session['activities'] + [phrase]
    if 'casino' in request.POST:
        luck = random.randrange(0,3)
        rand = random.randrange(0,51)
        if luck == 0:
            request.session['gold'] += rand
            phrase = f"<p class='green'> Entered casino and earned {rand} gold {now}</p>"
            request.session['activities'] += [phrase]
        else:
            if request.session['gold'] - rand < 0:
                request.session['gold'] = 0
                phrase = f"<p class='red'> Entered casino and lost all of your gold {now}</p>"
                request.session['activities'] += [phrase]
            else:
                request.session['gold'] -= rand
                phrase = f"<p class='red'> Entered casino and lost {rand} gold.. OUch...  {now}</p>"
                request.session['activities'] += [phrase]
    return redirect('/')

def clear(request):
    request.session.clear()
    return redirect('/')

