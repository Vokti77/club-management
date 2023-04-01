from django.forms import ModelForm
from django import forms
from .models import Donate, Event, Person, AssetDistribution


class DonationForm(ModelForm):
    class Meta:
        model = Donate
        exclude = ('doner', 'event', 'isapproved')


class AddPeopleForm(ModelForm):
    class Meta:
        model = Person
        fields = ['name', 'address']


class CreateEventForm(forms.ModelForm):
    class Meta:
        model = Event
        fields = ['title', 'cover', 'detail', 'place', 'total', 'deadline']


class DistributionForm(ModelForm):
    class Meta:
        model = AssetDistribution
        exclude = ('user', 'person',)

    def __init__(self, *args, **kwargs):
        super(DistributionForm, self).__init__(*args, **kwargs)
        self.fields['event'].queryset = Event.objects.filter(ready_to_distribute='yes')


class ContactForm(forms.Form):
    from_email = forms.EmailField(required=True)
    email_list = forms.CharField(required=True)
    subject = forms.CharField(required=True)
    message = forms.CharField(required=True)
