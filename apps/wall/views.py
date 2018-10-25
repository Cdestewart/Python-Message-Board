from django.shortcuts import render, HttpResponse, redirect
from django.contrib import messages
from ..first_app.models import User
from .models import Message, Comment
import bcrypt


def index(request):
    if(request.session.get('user_id')):
        request.session['user_id']
        messages = Message.objects.all().order_by('-created_at')
        comments = Comment.objects.all().order_by('created_at')
        return render(request, "wall/index.html",{'messages' :messages, 'comments': comments})
    else:
        return redirect('/login')

def post(request):
    Message.objects.create(messages = request.POST['message'], poster = User.objects.get(id=request.session['user_id']))
    return redirect('/wall/')

def comment(request):
    Comment.objects.create(comments = request.POST['comments'], poster = User.objects.get(id=request.session['user_id']), message_id = Message.objects.get(id =request.POST['message_id']))
    return redirect('/wall/')

def deletecomm(request):
    Comment.objects.get(id = request.POST['comment_id']).delete()
    return redirect('/wall/')

def logout(request):
    request.session.clear()
    return redirect('/login')