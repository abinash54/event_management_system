from django.urls import path
from . import views

urlpatterns = [
    path('management_dashboard/', views.landing, name='management_dashboard'),
    #service management
    path('view_services/', views.mang_index, name="view_services"),
    path('delete_company/<str:id>/', views.delete_company, name='delete_company'),
    path('update_approval_status/<str:id>/', views.update_approval_status, name='update_approval_status'),

    #booked event mang
    path('view_booked_events/', views.viewBookedEvents, name='view_booked_events'),
    path('update_booking_status/<str:id>/', views.updateBookingStatus, name='update_booking_status'),
    path('delete_booked_event/<str:id>/', views.deleteBookedEvent, name='delete_booked_event'),

    #manage venues
    path('view_venues/', views.venueDash, name='view_venues'),
    path('view_venue_list/', views.venueList, name='view_venue_list')


]