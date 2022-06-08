

def register_view(request):
    if request.method == 'POST':
        serializer = RegistrationSerializer(data=request.data)
        data={}