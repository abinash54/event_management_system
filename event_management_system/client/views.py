from django.shortcuts import render, redirect
from .forms import *

# Create your views here.

def getEventDetails(request):
    form = EventBookDetail()

    if request.method == 'POST':
        form = EventBookDetail(request.POST)

        if form.is_valid():
            form.save()
        
            return redirect('event_detail_form')

        else:
            return redirect('event_detail_form')

    

    context = {'form':form}
    return render(request, 'client/eventDetails_form.html', context)