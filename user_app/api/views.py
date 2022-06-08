from rest_framework.decorators import api_view
from user_app.api.serializers import RegistrationSerializer
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework.response import Response

@api_view(['POST'])
def register_view(request):
    if request.method == 'POST':
        serializer = RegistrationSerializer(data=request.data)
        data={}
        if serializer.is_valid():
            account = serializer.save()
            data['response'] = 'The registration was successfull'
            data['username'] = account.username
            data['email'] = account.email
            
            refresh = RefreshToken.for_user(account)
            data['token'] = {
                'refreshToken': str(refresh),
                'accessToken': str(refresh.access_token)
            }
        else:
            data = serializer.errors
            
        return Response(data)