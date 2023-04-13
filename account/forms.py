from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import DonorProfile, MemberProfile


class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'email')


class SignUpForm(UserCreationForm):
    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email', 'password1', 'password2',)


class DonorProfileForm(forms.ModelForm):
    class Meta:
        model = DonorProfile
        exclude = ['user',]


class MemberProfileForm(forms.ModelForm):
    class Meta:
        model = MemberProfile
        exclude = ['user', 'status']


class MemberApprovalForm(forms.ModelForm):
    class Meta:
        model = MemberProfile
        fields = ['status']
