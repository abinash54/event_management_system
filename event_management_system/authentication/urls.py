from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name="index"),
    path('reg/', views.registration, name="reg"),
    path('login/', views.login, name="login")

]