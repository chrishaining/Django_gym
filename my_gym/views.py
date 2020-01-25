from django.shortcuts import render
from django.http import HttpResponse
from my_gym.models import *
# Create your views here.


def index(request):
    sessions = Session.objects.all()
    return render(request, "my_gym/index.html", locals())


