from django import forms
from django.forms import ModelForm 

from management.models import Event


class EventBookDetail(forms.ModelForm):
    class Meta:
        model = Event
        fields = ('event_type', 'date', 'customer', 
                'phone', 'totalServices', 'service_1', 
                'service_1', 'service_2', 'service_3', 
                'service_4', 'numberOfVIPs', 'venue')

