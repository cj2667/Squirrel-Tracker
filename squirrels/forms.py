  
from django.forms import ModelForm

from .models import Squirrel


class UpdateForm(ModelForm):
    class Meta:
        model = Squirrel
        fields = "__all__"


class SightForm(ModelForm):
    class Meta:
        model = Squirrel
        fields = '__all__'
