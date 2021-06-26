from django.urls import path
from . import views


urlpatterns = [
    path('event_detail_form/', views.getEventDetails, name="event_detail_form"),


]