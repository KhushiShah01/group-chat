from django.forms import ModelForm
from .models import Room

class RoomForm(ModelForm):
    class Meta:
        model = Room
        field = '__all__'
        exclude =  ['created', 'updated']