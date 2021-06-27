from django.urls import path
from . import views

urlpatterns = [
    path('service_details_form/', views.detail_intake, name="service_details_form"),
    path('company_dashboard/<str:id>/', views.dashboard, name='company_dashboard'),
    #service detail entry forms
    path('catering_details_entry/', views.catEntry, name='catering_details_entry'),
    path('photonvideo_details_entry/', views.photoVideoEntry, name='photonvideo_details_entry'),
    path('vipTransport_details_entry/', views.vipTransportServiceEntry, name='vipTransport_details_entry'),
    path('decoration_service_detail_entry/', views.decorationServEntry, name='decoration_service_detail_entry'),
]