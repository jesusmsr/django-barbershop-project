from rest_framework.decorators import api_view
from user_app.api.serializers import RegistrationSerializer
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework.response import Response
from django.contrib import auth
from rest_framework import status


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
            data['first_name'] = account.first_name
            data['last_name'] = account.last_name
            data['phone_number'] = account.phone_number
            
            refresh = RefreshToken.for_user(account)
            data['token'] = {
                'refreshToken': str(refresh),
                'accessToken': str(refresh.access_token)
            }
        else:
            data = serializer.errors
            
        return Response(data)
    
@api_view(['POST'])
def login_view(request):
    data = {}
    if request.method == 'POST':
        email = request.post.get('email')
        password = request.post.get('password')
        
    account = auth.authenticate(email=email, password=password)
    if account is not None:
        data['response'] = 'Login successfull'
        data['username'] = account.username
        data['email'] = account.email
        data['first_name'] = account.first_name
        data['last_number'] = account.last_name
        data['phone_number'] = account.phone_number
        refresh = RefreshToken.for_user(account)
        data['token'] = {
            'refresh': str(refresh),
            'access': str(refresh.access_token)
        }
        
        return Response(data)
    else:
        data['error'] = 'bad credentials'
        return Response(data, status=status.HTTP_INTERNAL_SERVER_ERROR)