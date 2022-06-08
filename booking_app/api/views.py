from rest_framework.views import APIView
from booking_app.models import Booking
from rest_framework.response import Response
from booking_app.api.serializers import BookingSerializer
from rest_framework.permissions import IsAuthenticated
from rest_framework import status


class BookingListAV(APIView):
    permission_classes = [IsAuthenticated]
    
    def get(self, request):
        bookings = Booking.objects.all()
        serializer = BookingSerializer(bookings, many=True, context={'request': request})
        return Response(serializer.data)
    
class BookingCreateAV(APIView):
    permission_classes = [IsAuthenticated]
    
    def post(self, request):
        serializer = BookingSerializer(data=request.data)
        user = self.request.user
        
        if serializer.is_valid():
            serializer.save(user=user)
            return Response(serializer.data)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)