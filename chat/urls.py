from django.contrib.auth import views as auth_views
from django.urls import path
from . import views
urlpatterns = [ 

    path('', views.chat, name='chat'),
    path('sign_up', views.sign_up, name='sign-up'),
    path('login/', auth_views.LoginView.as_view(template_name='accounts/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
   
]