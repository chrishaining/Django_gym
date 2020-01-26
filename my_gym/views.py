from django.shortcuts import render, redirect
from django.http import HttpResponse
from my_gym.models import *
from .forms import MemberForm 
from .forms import SessionForm 

# Create your views here.

def index(request):
    members = Member.objects.all()
    sessions = Session.objects.all()
    return render(request, "my_gym/index.html", locals())

def member_new(request):
    if request.method == "POST":
        form = MemberForm(request.POST)
        if form.is_valid():
            member = form.save(commit=False)
            member.save()
            return redirect('index') 
    else:
        form = MemberForm()
        return render(request, 'my_gym/member_form.html', {'form': form})

def session_new(request):
    if request.method == "POST":
        form = SessionForm(request.POST)
        if form.is_valid():
            session = form.save(commit=False)
            session.save()
            return redirect('index') 
    else:
        form = SessionForm()
        return render(request, 'my_gym/session_form.html', {'form': form})

