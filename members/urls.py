from django.urls import path
from . import views

urlpatterns = [
    path('members/', views.members, name='members'),
    path('trainers/', views.trainers, name='trainers'),
    path('courts/', views.courts, name='courts'),
    path('', views.main, name='main'),
]