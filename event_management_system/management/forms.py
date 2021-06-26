from django import forms
from django.forms import ModelForm 
from .models import Venue

class VenueAddForm(forms.ModelForm):
    class Meta:
        model = Venue
        fields = ('name', 'owner_name', 'phone', 'cost', 'location', 'isAvailable')
