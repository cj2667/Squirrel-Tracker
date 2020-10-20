from django.shortcuts import render
from .models import Squirrel
import random
from django.shortcuts import get_object_or_404

def index(request):
    sightings = Squirrel.objects.all()
    context  = {
       'sightings': sightings, 
    }
    return render(request, 'squirrels/index.html', context)

def welcome(request):
    return render(request, 'squirrels/welcome.html',{})



def mapping(request):
    sightings = Squirrel.objects.all()
    chosen_list = []
    for i in range(100):
        chosen_sighting = random.choice(sightings)
        chosen_list.append(chosen_sighting)
    sightings = chosen_list
    context  = {
       'sightings': sightings,
    }
    return render(request, 'squirrels/mapping.html', context)



def id_detail(request, s_id):
    sighting = get_object_or_404(Squirrel, pk = s_id)
    
    context = {
        'sighting': sighting,
    }
    
    return render(request, 'squirrels/id_detail.html', context)

def add_detail(request):
    return render(request, 'squirrels/add_detail.html', {})

def stats(request):
    sightings = Squirrel.objects.all()
    context  = {
       'sightings': sightings,
    }
    return render(request, 'squirrels/stats.html', context)

