from django.shortcuts import render, redirect,  HttpResponse
from .models import people
from django.contrib import messages

def index(request):
    context = {
        "all_people": people.objects.all(),
    }
    return render(request, "index.html", context)

def create_user(request):
    errors = people.objects.basic_validator(request.POST)

    if len(errors) > 0:

        for key, value in errors.items():
            messages.error(request, value)

        return redirect("/")
    else:

        people.objects.create(first_name=request.POST['fname'], last_name=request.POST['lname'], favorite_color=request.POST['favcolor'], more_about_you=request.POST['more'])

        return redirect("/")

def delete_user(request, id):
    c = people.objects.get(id=id)
    c.delete()
    return redirect("/")

def info(request, id):
    context = {
        'person': people.objects.get(id=id)
    }
    
    return render(request, "info.html", context)

# Create your views here.
