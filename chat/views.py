from django.shortcuts import render, redirect
from django.contrib.auth import login
from .forms import RegistrationForm

def chat(request):
    return render(request, 'chat/chat.html')

def sign_up(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('index')
    else:
        form = RegistrationForm()

    return render(request, 'accounts/signup.html', {"form": form})
