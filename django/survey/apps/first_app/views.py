from django.shortcuts import render, redirect, HttpResponse


# Create your views here.
def survey(request):
    return render(request, 'first_app/survey.html')

def result(request):
    if 'count' in request.session:
        request.session['count'] += 1
    else:
        request.session['count'] = 1
    if request.method == "POST":
        info = {
            'name': request.POST['first_name'],
            'location': request.POST['location'],
            'language': request.POST['language'],
            'comments': request.POST['comments'],
        }
        return render(request, 'first_app/result.html', info)