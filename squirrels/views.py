from django.shortcuts import render
from .models import Squirrel


def index(request):
    sightings = Squirrel.objects.all()
    context  = {
       'sightings': sightings, 
    }
    return render(request, 'squirrels/index.html', context)

def welcome(request):
    return render(request, 'squirrels/welcome.html',{})



def mapping(request):
    return render(request, 'squirrels/mapping.html', {})



def id_detail(request):
    return render(request, 'squirrels/id_detail.html', {})

def add_detail(request):
    return render(request, 'squirrels/add_detail.html', {})

def stats(request):
    return render(request, 'squirrels/stats.html', {})



