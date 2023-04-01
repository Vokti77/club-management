from django.urls import path, include

from . import views
from .views import UserProfile, DonorList, DonorProfileView, EmployeeProfileView, \
    ActiveUsersList, UpdateEmployee, UpdateEmployeeProfile, UpdateDonorProfile

urlpatterns = [
    path('signup/', views.signup, name="signup"),
    path('accounts/', include('django.contrib.auth.urls')),
    path('dashboard/', views.dashboard, name="dashboard"),
    path('donor-profile/', DonorProfileView.as_view(), name="donor_profile"),
    path('employee-profile/', EmployeeProfileView.as_view(), name="employee_profile"),
    path('active-users/', ActiveUsersList.as_view(), name="active-users"),
    path('doner_list/', DonorList.as_view(), name="doner_list"),
    path('user_profile/<pk>', UserProfile.as_view(), name="user_profile"),
    path('update-employee/<pk>', UpdateEmployee.as_view(), name="update_employee"),
    path('update-employee-profile/<pk>', UpdateEmployeeProfile.as_view(), name='update_employee_profile'),
    path('update-donor-profile/<pk>', UpdateDonorProfile.as_view(), name='update_donor_profile'),
]
