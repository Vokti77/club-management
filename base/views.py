from django.shortcuts import render
from question.models import QuestionPaper, Solution
from event.models import Event, Donate
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


def contact(request):
    if request.method == 'POST':
        sender_name = request.POST['sender_name']
        sender_email = request.POST['sender_email']
        message = request.POST['message']
    return render(request, 'pages/contact.html')

def questions(request):
    questions = QuestionPaper.objects.all()
    solutions = Solution.objects.all()

    context = {
        'questions': questions,
        'solutions': solutions,
    }

    return render(request, 'pages/qs.html' , context)
