from rest_framework.views import APIView
from booking_app.models import Booking
from rest_framework.response import Response
from booking_app.api.serializers import BookingSerializer
from rest_framework.permissions import IsAuthenticated



class BookingAV(APIView):
    permission_classes = [IsAuthenticated]
    
    def get(self, request):
        bookings = Booking.objects.all()
        serializer = BookingSerializer(bookings, many=True, context={'request': request})
        return Response(serializer.data)