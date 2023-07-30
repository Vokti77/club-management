from django.shortcuts import render, redirect
from question.models import QuestionPaper, Solution
from django.core.mail import send_mail
from django.contrib.auth.models import User
from event.models import Event, Donate
from account.models import MemberProfile, DonorProfile
from django.views.generic import UpdateView, DetailView, ListView, CreateView
from account.models import MemberProfile, DonorProfile
from django.db.models import Sum
from room.models import Room, Message
from django.conf import settings

def index(request):
    events = Event.objects.all()
    # print("************************")
    # print(events)
    # print("************************")
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
   
    return render(request, 'events/events.html')

def initiative(request):
    events = Event.objects.all()
   
    amount = list(Donate.objects.filter(isapproved='yes').aggregate(Sum('amount')).values())[0]
    context = {
        'events': events,
        'amount': amount
    }
    return render(request, 'pages/initiative.html', context)


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
        subject = request.POST['subject']
        message = request.POST['message']

                # Send an email to the host email account
        host_email = 'vokti77@gmail.com'  # Replace with your host email account
        send_mail(f"{sender_name} - {subject}", f"From: {sender_name} <{sender_email}>\n\n{message}", sender_email, [host_email])


        user_subject = "Thank you for your interest in EEE Club!"
        user_message = f"Hello {sender_name},\n\nThank you for your interest in EEE Club! We have received your email. We will review your email and get back to you soon.\n\nWe hope you have a good day! \n\n\n\n\nBest regards, \n\nEEEclub Team"
        send_mail(user_subject, user_message, host_email, [sender_email])
    
        context = {
            'sender_name': sender_name,
            'sender_email': sender_email,
            'message': message

        }
        return render(request, 'pages/contact.html', context)
    return render(request, 'pages/contact.html', {})


# from .forms import ContactForm
# from .models import ContactMessage

# def contact(request):
#     if request.method == 'POST':
#         form = ContactForm(request.POST)
#         if form.is_valid():
#             name = form.cleaned_data['name']
#             email = form.cleaned_data['email']
#             subject = form.cleaned_data['subject']
#             message = form.cleaned_data['message']

#             # Save the message to the database
#             contact_message = ContactMessage(name=name, email=email, subject=subject, message=message)
#             contact_message.save()

#             # Send an email to the host email account
#             host_email = 'vokti77@gmail.com'  # Replace with your host email account
#             send_mail(f"{name} - {subject}", f"From: {name} <{email}>\n\n{message}", email, [host_email])


#             user_subject = "Thank you {name} for contacting us"
#             user_message = "Thank you for your message. We will get back to you soon."
#             send_mail(user_subject, user_message, host_email, [email])

#             return redirect('contact_success')  # Redirect to a success page after successful submission
#     else:
#         form = ContactForm()

#     return render(request, 'pages/contact.html', {'form': form})

def contact_success(request):
    return render(request, 'pages/contact_success.html')
