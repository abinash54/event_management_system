from django.urls import path
from . import views

urlpatterns = [
    path('', views.mang_index, name="dashboard"),


]