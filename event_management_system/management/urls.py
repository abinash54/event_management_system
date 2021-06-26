from django.urls import path
from . import views

urlpatterns = [
    path('view_services/', views.mang_index, name="view_services"),
    path('delete_company/<str:id>/', views.delete_company, name='delete_company'),


]