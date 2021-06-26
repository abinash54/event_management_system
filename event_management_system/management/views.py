from django.shortcuts import render

# Create your views here.
def mang_index(request):
    
    return render(request, 'management/dashboard.html')
