from django.urls import path

from . import views
from .views import UpdateEvent, DeleteEvent, CreateEvent, AllDonations, UpdateDonation, PeopleList, \
    AddPeople, UpdatePeople, DeletePeople, DetailPeople, DistributionList, distribute, DistributionDetail, detail_event

urlpatterns = [
    path('', views.events, name="events"),
    path('donate/<pk>', views.donation, name="donate"),
    path('my-donations/', views.my_donations, name="my-donations"),
    path('all-donations/', AllDonations.as_view(), name="all-donations"),
    path('update-donation/<pk>', UpdateDonation.as_view(), name="update-donation"),
    path('detail-event/<id>', detail_event, name="detail-event"),
    # path('detail-event/<pk>', DetailEvent.as_view(), name="detail-event"),
    path('create-event/', CreateEvent.as_view(), name="create-event"),
    path('update-event/<pk>', UpdateEvent.as_view(), name="update-event"),
    path('delete-event/<pk>', DeleteEvent.as_view(), name="delete-event"),
    path('all-poor-people', PeopleList.as_view(), name="all_poor_people"),
    path('create-people-list', AddPeople.as_view(), name="add_poor_people"),
    path('donate-people/<pk>', UpdatePeople.as_view(), name="donate-people"),
    path('delete-poor-people/<pk>', DeletePeople.as_view(), name="delete_poor_people"),
    path('detail-people/<pk>', DetailPeople.as_view(), name="detail-people"),
    path('make-distribution/<id>', views.distribute, name="make-distribution"),
    path('update-people/<pk>', UpdatePeople.as_view(), name="update-people"),
    path('distribution-list/', DistributionList.as_view(), name="distribution-list"),
    path('distribution-details/<pk>', DistributionDetail.as_view(), name="distribution-detail"),
    path('invite-doner/', views.contact_form, name="invite-doner"),
]
