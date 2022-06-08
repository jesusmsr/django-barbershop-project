from django.urls import path, include
from booking_app.api.views import BookingListAV, BookingCreateAV

urlpatterns = {
    path('list/', BookingListAV.as_view(), name='booking-list'),
    path('booking-create/', BookingCreateAV.as_view(), name='booking-create'),
}