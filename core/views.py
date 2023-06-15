
from django.shortcuts import render, redirect

from .forms import SignUpForm

def frontpage(request):
    return render(request, 'chat/core/frontpage.html')

