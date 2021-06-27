from django.shortcuts import render, redirect
from .models import Service_Company, Event, Venue
from .forms import *

# Create your views here.
def landing(request):
    return render(request, 'management/managementLanding.html')


def mang_index(request):
    services = Service_Company.objects.all()
    
    context = {'services':services}
    return render(request, 'management/ManagerViewService.html', context)


def delete_company(request, id):
    data = Service_Company.objects.get(id=id)
    if request.method=='POST':
        try:
            data.delete()
            return redirect('view_services')

        except:
            return redirect('view_services')


def update_approval_status(request, id):
    data = Service_Company.objects.get(id=id)
    if request.method=='POST':

        try:
            if data.isApproved is True:
                data.isApproved = False
                data.save()
            else:
                data.isApproved = True
                data.save()
           
            return redirect('view_services')
        except:
            #send failure alert
            return redirect('view_services')


def viewBookedEvents(request):
    events = Event.objects.all()
    
    context = {'events':events}
    return render(request, 'management/ManageBookedEvents.html', context)


#event booking mng
def updateBookingStatus(request, id):
    data = Event.objects.get(id=id)
    if request.method=='POST':
        print('working...')
        try:
            if data.isApproved is True:
                data.isApproved = False
                data.save()
                #set alert
            else:
                data.isApproved = True
                data.save()
                #set alert
           
            return redirect('view_booked_events')
        except:
            #send failure alert
            return redirect('view_booked_events')


def deleteBookedEvent(request, id):
    data = Event.objects.get(id=id)
    if request.method=='POST':
        try:
            data.delete()
            return redirect('view_booked_events')

        except:
            return redirect('view_booked_events')


#venue show and CRUD
def venueDash(request):
    
    form = VenueAddForm()

    if request.method=='POST':
        form = VenueAddForm(request.POST)
        
        if form.is_valid():
            form.save()
            #messages.success(request, 'Data has been saved successfully!',extra_tags='supply_data')
            return redirect('view_venues')
        else:
            #messages.warning(request, 'Data not saved',extra_tags='supply_data')
            return redirect('view_venues')
    
    context = {'form':form}
    return render(request, 'management/DashboardVenues.html', context)


def venueList(request):
    venues = Venue.objects.all()
    context = {'venues':venues}

    return render(request, 'management/VenueList.html', context)
