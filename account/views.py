from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.shortcuts import redirect, render
from django.urls import reverse_lazy
from django.utils.decorators import method_decorator
from django.views.generic import UpdateView, DetailView, ListView, CreateView
from .forms import SignUpForm, DonorProfileForm, MemberProfileForm
from .models import MemberProfile, DonorProfile
from django.contrib.auth import login

def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)

        if form.is_valid():
            user = form.save()
            user.save()
            return redirect('login')
    else:
        form = SignUpForm()
    
    return render(request, 'accounts/signup.html', {'form': form})

@login_required(login_url='login')
def dashboard(request):
    if request.user.is_superuser:
        user_request = User.objects.all()
        context = {
            'users': user_request
        }
        return render(request, 'dashboard/admin.html', context)
    return render(request, 'dashboard/dashboard.html')


class MemberProfileView(CreateView):
    form_class = MemberProfileForm

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super(MemberProfileView, self).dispatch(*args, **kwargs)

    def form_valid(self, form):
        obj = form.save(commit=False)
        obj.user_id = self.request.user.id
        obj.save()
        return redirect('dashboard')

    success_url = reverse_lazy('dashboard')
    template_name = 'dashboard/profile.html'


class DonorProfileView(CreateView):
    form_class = DonorProfileForm

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super(DonorProfileView, self).dispatch(*args, **kwargs)

    def form_valid(self, form):
        obj = form.save(commit=False)
        obj.user_id = self.request.user.id
        obj.save()
        return redirect('dashboard')

    success_url = reverse_lazy('dashboard')
    template_name = 'dashboard/profile.html'


class ActiveUsersList(ListView):
    context_object_name = 'users'
    model = User
    template_name = 'profiles/active_users.html'


class DonorList(ListView):
    context_object_name = 'donors'
    model = DonorProfile
    template_name = 'profiles/notification.html'


class UserProfile(DetailView):
    context_object_name = 'user'
    model = User
    template_name = 'profiles/user_profile.html'
    success_url = reverse_lazy('dashboard')


class UpdateMember(UpdateView):
    fields = ('status',)
    model = MemberProfile
    template_name = 'events/update.html'
    success_url = reverse_lazy('dashboard')


class UpdateMemberProfile(UpdateView):
    fields = ('name', 'email', 'contact', 'address', 'department', 'image', 'batch','cv',)
    model = MemberProfile
    template_name = 'events/update.html'
    success_url = reverse_lazy('dashboard')


class UpdateDonorProfile(UpdateView):
    fields = ('name', 'email', 'contact', 'address', 'image', 'blood')
    model = DonorProfile
    template_name = 'events/update.html'
    success_url = reverse_lazy('dashboard')
