from rest_framework.views import APIView
from booking_app.models import Booking
from rest_framework.response import Response
from booking_app.api.serializers import BookingSerializer
from rest_framework.permissions import IsAuthenticated
from rest_framework import status
from datetime import datetime, timedelta
import pytz

class BookingAV(APIView):
    permission_classes = [IsAuthenticated]
    
    def get(self, request):
        if self.request.user.is_staff:
            bookings = Booking.objects.all()
        else:
            bookings = Booking.objects.filter(user=self.request.user)
        serializer = BookingSerializer(bookings, many=True, context={'request': request})
        return Response(serializer.data)
    
    def post(self, request):
        serializer = BookingSerializer(data=request.data)
        user = self.request.user
        bookings = Booking.objects.all()
        
        if serializer.is_valid():
            utc = pytz.UTC
            parsed_time = datetime.strptime(request.data['booking_date'], '%Y-%m-%dT%H:%M:%S.%fZ')
            final_time = parsed_time + timedelta(minutes=request.data['duration'])
            if len(bookings) > 1:
                for booking in bookings:
                    if utc.localize(parsed_time) > booking.booking_date and final_time:
                        return Response({'error':'booking date intersect with another booking'})
                    else:
                        serializer.save(user=user)
                        return Response(serializer.data)
            else:
                serializer.save(user=user)
                return Response(serializer.data)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
    def put(self, request, pk):
        try:
            booking = Booking.objects.get(pk=pk)
        except Booking.DoesNotExist:
            return Response({'error': 'Booking does not exist'},status=status.HTTP_404_NOT_FOUND)
        
        if booking.user == request.user:
            serializer = BookingSerializer(booking, data=request.data, context={'request': request})
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data)
            else:
                return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        else:
            return Response({'error':'You cant edit other users booking'})
        