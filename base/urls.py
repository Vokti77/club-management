from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('about/', views.about, name='about'),
    path('event/', views.event, name='event'),
    path('contact/', views.contact, name='contact'),
    path('questions/', views.questions, name='questions'),
    
]