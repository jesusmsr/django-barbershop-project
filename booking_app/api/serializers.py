from rest_framework import serializers

from booking_app.models import Booking


class BookingSerializer(serializers.ModelSerializer):
    user = serializers.StringRelatedField(read_only=True)
    class Meta:
        model = Booking
        fields = '__all__'