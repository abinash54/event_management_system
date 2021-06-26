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


#service details entry


def catEntry(request):
    form = CateringForm()

    if request.method=='POST':
        form = CateringForm(request.POST)

        if form.is_valid():
            form.save()
            #send an alert
            return redirect('catering_details_entry')

        else:
            #send wrong alert
            return redirect('catering_details_entry')
    
    context={'form':form}

    return render(request, 'services/cateringDetailEntry.html', context)


def photoVideoEntry(request):
    form = PhotoVideoEntryForm()

    if request.method=='POST':
        form = PhotoVideoEntryForm(request.POST)

        if form.is_valid():
            form.save()
            #send an alert
            return redirect('photonvideo_details_entry')

        else:
            #send wrong alert
            return redirect('photonvideo_details_entry')
    
    context={'form':form}

    return render(request, 'services/photoAndVideoDetailEntry.html', context)



def vipTransportServiceEntry(request):
    form = VIPTransportServiceForm()

    if request.method=='POST':
        form = VIPTransportServiceForm(request.POST)

        if form.is_valid():
            form.save()
            #send an alert
            return redirect('vipTransport_details_entry')

        else:
            #send wrong alert
            return redirect('vipTransport_details_entry')
    
    context={'form':form}

    return render(request, 'services/vipTransportDetailEntry.html', context)

  
def decorationServEntry(request):
    form = DecorationServiceForm()

    if request.method=='POST':
        form = DecorationServiceForm(request.POST)

        if form.is_valid():
            form.save()
            #send an alert
            return redirect('decoration_service_detail_entry')

        else:
            #send wrong alert
            return redirect('decoration_service_detail_entry')
    
    context={'form':form}

    return render(request, 'services/decorationServiceDetailEntry.html', context)


