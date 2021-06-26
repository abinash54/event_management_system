from django.shortcuts import render, redirect
from django.template.context_processors import csrf
from django.http import JsonResponse
from django.template import RequestContext
from .forms import *

# Create your views here.
def detail_intake(request):
    form = CompanyDetailsIntakeForm()

    if request.method=='POST':
        form = CompanyDetailsIntakeForm(request.POST)
        
        if form.is_valid():
            form.save()
            #messages.success(request, 'Data has been saved successfully!',extra_tags='supply_data')
            return redirect('service_details_form')
        else:
            #messages.warning(request, 'Data not saved',extra_tags='supply_data')
            return redirect('service_details_form')

    context = {'form':form}
    
    return render(request, 'services/serviceDetailsForm.html', context)



