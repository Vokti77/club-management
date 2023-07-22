from django.shortcuts import render
from question.models import QuestionPaper, Solution
from django.core.mail import send_mail
from django.contrib.auth.models import User
from event.models import Event, Donate
from account.models import MemberProfile, DonorProfile
from django.views.generic import UpdateView, DetailView, ListView, CreateView
from account.models import MemberProfile, DonorProfile
from django.db.models import Sum
from room.models import Room, Message

def index(request):
    events = Event.objects.all()
    amount = list(Donate.objects.filter(isapproved='yes').aggregate(Sum('amount')).values())[0]
    context = {
        'events': events,
        'amount': amount
    }
    return render(request, 'pages/index.html', context)

def about(request):
    members = MemberProfile.objects.all()
    
    return render(request, 'pages/about.html', {'members':members})

def event(request):
    events = Event.objects.all()
    amount = list(Donate.objects.filter(isapproved='yes').aggregate(Sum('amount')).values())[0]
    context = {
        'events': events,
        'amount': amount
    }
    return render(request, 'pages/event.html', context)

def questions(request):
    questions = QuestionPaper.objects.all()
    solutions = Solution.objects.all()

    context = {
        'questions': questions,
        'solutions': solutions,
    }

    return render(request, 'pages/qs.html' , context)

def gallery(request):
    return render(request, 'pages/gallery.html')



def contact(request):
    if request.method == 'POST':
        sender_name = request.POST['name']
        sender_email = request.POST['email']
        message = request.POST['message']

        send_mail (
            sender_name,
            sender_email,
            message,
            ['vokti77@gmail.com']
        )
        context = {
            'sender_name': sender_name,
            'sender_email': sender_email,
            'message': message

        }
        return render(request, 'pages/contact.html', context)
    return render(request, 'pages/contact.html', {})


