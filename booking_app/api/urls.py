from django.urls import path, include
from booking_app.api.views import BookingAV

urlpatterns = [
    path('list/', BookingAV.as_view(), name='booking-list'),
    path('booking/', BookingAV.as_view(), name='booking-create'),
    path('booking/<int:pk>', BookingAV.as_view(), name='booking-create'),
]