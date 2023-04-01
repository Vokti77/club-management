from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import DonorProfile, EmployeeProfile


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


class EmployeeProfileForm(forms.ModelForm):
    class Meta:
        model = EmployeeProfile
        exclude = ['user', 'status']


class EmployeeApprovalForm(forms.ModelForm):
    class Meta:
        model = EmployeeProfile
        fields = ['status']
