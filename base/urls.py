from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('about/', views.about, name='about'),
    path('event/', views.event, name='event'),
    path('initiative/', views.initiative, name='initiative'),
    path('questions/', views.questions, name='questions'),
    path('contact/', views.contact, name='contact'),
    path('gallery/', views.gallery, name='gallery'),
    path('contact_success/', views.contact_success, name='contact_success'),
    
    
]