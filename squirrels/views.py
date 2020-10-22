from django.shortcuts import render
from .models import Squirrel
import random
from django.http import HttpResponse, Http404
from django.shortcuts import get_object_or_404
from django.http import HttpResponseRedirect
from .forms import SightForm

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
    if request.method == 'POST':
        form = SightForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(f'/sightings/')
    else:
        form = SightForm()
    context = {
            'form':form,
            }
    return render(request, 'squirrels/add_detail.html', context)

def stats(request):
    sightings = Squirrel.objects.all()
    output = []
    running_count = 0
    chasing_count = 0
    climbing_count = 0
    eating_count = 0
    foraging_count = 0
    for sighting in sightings:
        if sighting.Running == "true":
            running_count += 1
        if sighting.Chasing == "true":
            chasing_count += 1
        if sighting.Climbing == "true":
            climbing_count += 1
        if sighting.Eating == "true":
            eating_count += 1
        if sighting.Foraging == "true":
            foraging_count += 1
    output.extend([running_count, chasing_count, climbing_count, eating_count, foraging_count])
    context  = {
            "running_count": running_count,
            "chasing_count": chasing_count,
            "climbing_count": climbing_count,
            "eating_count": eating_count,
            "foraging_count": foraging_count,
    }
    return render(request, 'squirrels/stats.html', context)

def update(request,squirrel_id):
    obj = get_object_or_404(Squirrel, Unique_Squirrel_ID = squirrel_id)
    form = SightForm(request.POST or None, instance = obj)
    context = {'form':form}
    if form.is_valid():
        obj = form.save(commit=False)
        obj.save()
        return HttpResponseRedirect('/sightings/')
    else:
        context = {'form': form}
        return render(request, 'squirrels/update.html', context)
