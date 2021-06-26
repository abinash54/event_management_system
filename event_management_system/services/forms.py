from django import forms
from django.forms import ModelForm 
from management.models import Service_Company

class CompanyDetailsIntakeForm(forms.ModelForm):
    class Meta:
        model = Service_Company
        fields = ('name', 'phone', 'email', 'service_type', 'address', 'license_id')

        