from django.shortcuts import render

# Create your views here.
def index(request):
    
    return render(request, 'authentication/index.html')


def registration(request):
    
    return render(request, 'authentication/signUp.html')


def login(request):
    
    return render(request, 'authentication/login.html')