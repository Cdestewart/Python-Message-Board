from django.shortcuts import render, HttpResponse, redirect
from django.contrib import messages
from .models import User
import bcrypt
def index(request):
    content = User.objects.all().values()
    return render(request, "first_app/index.html", {'content':content})

def new(request):
    print('first')
    errors = User.objects.validator(request.POST)
    print('new')
    if len(errors):
        for key, value in errors.items():
            print("key", key, "value", value)
            messages.error(request, value)
        return redirect('/')
    else:   
        User.objects.create(fname = request.POST['fname'], lname = request.POST['lname'], email = request.POST['email'], password = bcrypt.hashpw(request.POST['password'].encode(), bcrypt.gensalt()))
        content = User.objects.all()
        request.session['user_id'] = User.objects.get(email =request.POST['email']).id
        return redirect('/success',content)

def login(request):
    errors = User.objects.existing(request.POST)
    if len(errors):
        for key, value in errors.items():
            messages.error(request, value)
        return redirect('/')
    request.session['user_id'] = User.objects.get(email =request.POST['email']).id
    return redirect('/wall/')

def success(request):
    content = User.objects.get(id = request.session['user_id'])
    return redirect('/wall/')