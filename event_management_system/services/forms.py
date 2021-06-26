from django import forms
from django.forms import ModelForm 
from management.models import Service_Company
from .models import Catering, Photo_n_Videography, VIP_Transport, Decoration
 
class CompanyDetailsIntakeForm(forms.ModelForm):
    class Meta:
        model = Service_Company
        fields = ('name', 'phone', 'email', 'service_type', 'address', 'license_id')



class CateringForm(forms.ModelForm):
    class Meta:
        model = Catering
        fields = ('company', 'food_item_1', 'price_1', 'food_item_2', 'price_2', 'food_item_3',
                    'price_3', 'food_item_4', 'price_4', 'license_number')




class PhotoVideoEntryForm(forms.ModelForm):
    class Meta:
        model = Photo_n_Videography
        fields = ('company', 'no_of_equipments', 'charge')




class VIPTransportServiceForm(forms.ModelForm):
    class Meta:
        model = VIP_Transport
        fields = ('company', 'no_of_vehicles', 'vehicle_1', 'charge_1',
                'vehicle_2', 'charge_2', 'vehicle_3', 'charge_3', 'vehicle_4', 'charge_4')


class DecorationServiceForm(forms.ModelForm):
    class Meta:
        model = Decoration
        fields = ('company', 'description', 'charge')

        
        