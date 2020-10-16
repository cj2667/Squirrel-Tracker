from django.shortcuts import render
from .models import Squirrel


def index(request):
    squirrels = Squirrel.objects.all()
    context  = {
       'sighting_3000': squirrels, 
    }
    return render(request, 'squirrels/index.html', context)




