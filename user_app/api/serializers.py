from rest_framework import serializers
from user_app.models import Account

class RegistrationSerializer(serializers.ModelSerializer):
    password_confirm = serializers.CharField(style={'input_type': 'password'}, write_only=True)
    
    class Meta:
        model = Account
        fields = ['username','email','password', 'password_confirm','phone_number','first_name','last_name']
        extra_kwargs = {
            'password': {'write_only': True}
        }
        
    def save(self):
        password = self.validated_data['password']
        password_confirm = self.validated_data['password_confirm']
        
        if password != password_confirm:
            raise serializers.ValidationError({'error': 'password does not match'})
        
        if Account.objects.filter(email=self.validated_data['email']).exists():
            raise serializers.ValidationError({'error': 'there is already a user with that email'})
        
        #account = Account(email=self.validated_data['email'], username=self.validated_data['username'])
        account = Account.objects.create_user(
            first_name=self.validated_data['first_name'], 
            last_name=self.validated_data['last_name'],
            email= self.validated_data['email'], 
            username= self.validated_data['username'],
            password= self.validated_data['password']
        )
        
        account.phone_number = self.validated_data['phone_number']
        #account.set_password(password)
        account.save()
        return account