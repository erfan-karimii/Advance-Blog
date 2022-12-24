from django.urls import path , include
from . import views 
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
    TokenVerifyView,
)
app_name = 'api-v1'

urlpatterns = [
    path('register/',views.RegistrationUser.as_view(),name='registration'),
    path('token/login/',views.CustomObtainAuthToken.as_view(),name='token-login'),
    path('token/logout/',views.CustomDiscardAuthToken.as_view(),name='token-logout'),
    path('jwt/create/', TokenObtainPairView.as_view(), name='jwt-create'),
    path('jwt/refresh/', TokenRefreshView.as_view(), name='jwt-refresh'),
    path('jwt/verify/', TokenVerifyView.as_view(), name='jwt-verify'),
    path('profile/',views.UserProfile.as_view(),name='profile'),
    path('send/mail/',views.SendEmailBackend.as_view(),name='send-mail'),
    path('email/activation/<str:token>',views.ActivivationAcccount.as_view(),name='activation-email'),
    path('resend/activation/',views.ResendVerification.as_view(),name='activation-resend'),


]