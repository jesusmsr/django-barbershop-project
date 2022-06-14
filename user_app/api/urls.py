from rest_framework.authtoken.views import obtain_auth_token
from django.urls import path, include
from user_app.api.views import login_view, logout_view, register_view, session_view
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

urlpatterns = [
    path('login/', obtain_auth_token, name='login'),
    path('login-app/', login_view, name='login-app'),
    path('register/', register_view, name='register'),
    path('logout/', logout_view, name='logout'),
    path('session/', session_view, name='session'),
    
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh')
]