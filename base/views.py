from django.shortcuts import render
from question.models import QuestionPaper, Solution
from event.models import Event, Donate
from django.db.models import Sum

def index(request):
    events = Event.objects.all()
    amount = list(Donate.objects.filter(isapproved='yes').aggregate(Sum('amount')).values())[0]
    context = {
        'events': events,
        'amount': amount
    }
    return render(request, 'pages/index.html', context)

def about(request):
    return render(request, 'pages/about.html')

def event(request):
    return render(request, 'pages/event.html')


def contact(request):
    return render(request, 'pages/contact.html')

def questions(request):
    questions = QuestionPaper.objects.all()
    solutions = Solution.objects.all()

    context = {
        'questions': questions,
        'solutions': solutions,
    }

    return render(request, 'pages/qs.html' , context)