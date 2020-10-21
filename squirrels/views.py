from django.shortcuts import render
from .models import Squirrel
import random
from django.http import HttpResponse, Http404
from django.shortcuts import get_object_or_404



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
#
#    if request.method == 'POST':
#        form = SightForm(request.POST)
#        if form.is_valid():
#            form.save()
#            return HttpResponseRedirect('/sightings/')
#    else:
#       form = SightForm()

    return render(request, 'squirrels/add_detail.html', {})

def stats(request):
    sightings = Squirrel.objects.all()
    context  = {
       'sightings': sightings,
    }
    return render(request, 'squirrels/stats.html', context)


def update(request):
    if request.method == 'POST':
        form = UpdateForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request, 'squirrels/update.html')
        
