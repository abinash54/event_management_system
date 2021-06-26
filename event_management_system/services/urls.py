from django.urls import path
from . import views

urlpatterns = [
    path('service_details_form/', views.detail_intake, name="service_details_form"),
    

]