from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.core.mail import send_mail
from django.db.models import Sum
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.utils.decorators import method_decorator
from django.views.generic import UpdateView, DeleteView, CreateView, DetailView, ListView

from . import models
from .forms import DonationForm, AddPeopleForm, CreateEventForm, DistributionForm, ContactForm
from event.models import Event, Donate, Person, AssetDistribution

def events(request):
    event = Event.objects.all()
    amount = list(Donate.objects.filter(isapproved='yes').aggregate(Sum('amount')).values())[0]
    context = {
        'events': event,
        'amount': amount
    }
    return render(request, 'events/events.html', context)


# def events(request):
#     qs = Event.objects.all()
#     print('------------------------------')
#     print(qs)
#     print('------------------------------')
#     amount = list(Donate.objects.filter(isapproved='yes').aggregate(Sum('amount')).values())[0]
#     context = {
#         'qs': qs,
#         'amount': amount
#     }

#     print('------------------------------')
#     print(qs)
#     print('------------------------------')
#     return render(request, 'events/events.html', context)


def donation(request, pk):
    form = DonationForm()
    if request.method == 'POST':
        form = DonationForm(request.POST)
        if form.is_valid():
            donate = form.save(commit=False)
            donate.doner = request.user
            donate.event = Event.objects.get(pk=pk)
            donate.save()
            messages.info(request, "Successfully form submitted")
            return redirect("event")
    return render(request, 'events/donate.html', {'form': form})


class AllDonations(ListView):
    context_object_name = 'donates'
    model = models.Donate
    template_name = 'events/all_donations.html'
    success_url = reverse_lazy('event')


class UpdateDonation(UpdateView):
    model = Donate
    fields = ('isapproved',)
    template_name = 'events/update.html'
    success_url = reverse_lazy('event')


def my_donations(request):
    user = request.user
    doner_id = user.pk
    donate = Donate.objects.filter(doner_id=doner_id)
    context = {
        'donates': donate,
        'doner_id': doner_id
    }
    return render(request, 'events/my_donations.html', context)


class CreateEvent(CreateView):
    model = models.Event
    fields = ['title', 'cover', 'detail', 'place', 'total', 'deadline', 'gained']
    template_name = 'events/create_event.html'
    success_url = reverse_lazy('event')


def detail_event(request, id):
    amount = Donate.objects.filter(isapproved='yes', event_id=id).aggregate(Sum('amount'))['amount__sum'] or 0
    event = Event.objects.get(id=id)
    event.gained = amount
    event.save()
    context = {
        'event': event
    }
    return render(request, 'events/detail_event.html', context)


class UpdateEvent(UpdateView):
    fields =  ['title', 'cover', 'detail', 'place', 'total', 'deadline', 'ready_to_distribute']
    model = models.Event
    template_name = 'events/update.html'
    success_url = reverse_lazy('event')


class DeleteEvent(DeleteView):
    fields = '__all__'
    model = models.Event
    template_name = 'events/delete_event.html'
    success_url = reverse_lazy('event')


class AddPeople(CreateView):
    form_class = AddPeopleForm

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super(AddPeople, self).dispatch(*args, **kwargs)

    def form_valid(self, form):
        obj = form.save(commit=False)
        obj.user_id = self.request.user.id
        obj.save()
        return redirect('all_poor_people')

    success_url = reverse_lazy('all_poor_people')
    template_name = 'events/poor_people_form.html'


class PeopleList(ListView):
    model = models.Person
    context_object_name = 'peoples'
    template_name = 'events/poor_people_list.html'
    success_url = reverse_lazy('all_poor_people')


class UpdatePeople(UpdateView):
    fields = '__all__'
    model = models.Person
    template_name = 'events/poor_people_form.html'
    success_url = reverse_lazy('all_poor_people')


class DeletePeople(DeleteView):
    fields = '__all__'
    model = models.Person
    template_name = 'events/poor_people_form.html'
    success_url = reverse_lazy('all_poor_people')


class DetailPeople(DetailView):
    context_object_name = 'people'
    model = models.Person
    template_name = 'events/poor_detail.html'
    success_url = reverse_lazy('event')


def distribute(request, id):
    form = DistributionForm()
    amount  = list(Donate.objects.filter(isapproved='yes', event_id=id).aggregate(Sum('amount')).values())[0]
    remaining=amount
    if request.method == 'POST':
        form = DistributionForm(request.POST)
        if form.is_valid():
            donate = form.save(commit=False)
            donate.user = request.user
            donate.person = Person.objects.get(id=id)
            remaining -= donate.amount
            form.save()
            messages.info(request, "Successfully form submitted")
            return redirect("distribution-list")
    context={
        'remaining':remaining,
        'form':form
    }
    return render(request, 'events/distribution-form.html', context)


class DistributionList(ListView):
    model = AssetDistribution
    context_object_name = 'persons'
    template_name = 'events/distribution-list.html'


class DistributionDetail(DetailView):
    model = AssetDistribution
    context_object_name = 'item'
    template_name = 'events/distribution-details.html'

def contact_form(request):
    if request.method == "GET":
        form = ContactForm()
        return render(request, 'pages/contact.html', {'form': form})
    else:
        form = ContactForm(request.POST)
        if form.is_valid():
            f_name = form.cleaned_data['fname']
            from_mail = form.cleaned_data['email']
            subject = form.cleaned_data['subject']
            message = form.cleaned_data['message']
            email_list = form.cleaned_data['email_list']
            send_mail(subject, message, from_mail, [email_list])
            return render(request, 'pages/contact.html', {'form': form})