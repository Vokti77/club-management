from django.urls import path, include

from . import views
from .views import UserProfile, DonorList, DonorProfileView, MemberProfileView, \
    ActiveUsersList, UpdateMember, UpdateMemberProfile, UpdateDonorProfile

urlpatterns = [
    path('signup/', views.signup, name='signup'),
    path('accounts/', include('django.contrib.auth.urls')),
    path('dashboard/', views.dashboard, name="dashboard"),
    path('donor-profile/', DonorProfileView.as_view(), name="donor_profile"),
    path('Member-profile/', MemberProfileView.as_view(), name="Member_profile"),
    path('active-users/', ActiveUsersList.as_view(), name="active-users"),
    path('doner_list/', DonorList.as_view(), name="doner_list"),
    path('user_profile/<pk>', UserProfile.as_view(), name="user_profile"),

    path('update_member/<pk>', UpdateMember.as_view(), name="update-member"),

    path('update_member_profile/<pk>', UpdateMemberProfile.as_view(), name='update-member-profile'),

    path('update-donor-profile/<pk>', UpdateDonorProfile.as_view(), name='update_donor_profile'),
]
