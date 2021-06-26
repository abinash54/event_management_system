from django.shortcuts import render, redirect
from .models import Service_Company

# Create your views here.
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
            if data.getStatus is True:
                data.isApproved = False
            else:
                data.isApproved = True
           
            return redirect('view_services')
        except:
            #send failure alert
            return redirect('view_services')

