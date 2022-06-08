from rest_framework.views import APIView
from booking_app.models import Booking
from rest_framework.response import Response
from booking_app.api.serializers import BookingSerializer
from rest_framework.permissions import IsAuthenticated
from rest_framework import status


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
        
        if serializer.is_valid():
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
        