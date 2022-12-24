from rest_framework import generics
from .serializers import RegistrationSerializers , CustomAuthTokenSerializer , UserProfileSerilizers , ResendVerificationSerializers
from rest_framework import status
from rest_framework.response import Response
from rest_framework.authtoken.views import ObtainAuthToken 
from rest_framework.authtoken.models import Token
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from django.shortcuts import get_object_or_404
from accounts.models import Profile
from django.core.mail import send_mail
from rest_framework_simplejwt.tokens import RefreshToken
from accounts.models import User
import jwt
from jwt.exceptions import ExpiredSignatureError ,InvalidSignatureError
from core.settings import SECRET_KEY

# Create your views here.

class RegistrationUser(generics.GenericAPIView):
    serializer_class = RegistrationSerializers

    def post(self,request,*args,**kwargs):
        serializers = RegistrationSerializers(data= request.data)
        if serializers.is_valid():
            serializers.save()
            email = serializers.validated_data['email']
            data = {
                'email' : email,
                'next step' : 'pleas verify your email addres'
            }
            user=get_object_or_404(User,email=email)
            token= self.get_tokens_for_user(user)
            send_mail(
                'Subject here',
                f'http://localhost:8000/accounts/api/v1/email/activation/{token}',
                'from@example.com',
                ['to@example.com'],
                fail_silently=False,
            )
            return Response(data,status=status.HTTP_201_CREATED)
        return Response(serializers.errors,status=status.HTTP_400_BAD_REQUEST)

    def get_tokens_for_user(self,user):
        refresh = RefreshToken.for_user(user)
        return str(refresh.access_token)

class ActivivationAcccount(APIView):
    def get(self,request,token,*args,**kwargs):
        try:
            token = jwt.decode(token,SECRET_KEY,algorithms=["HS256"])
        except ExpiredSignatureError:
            return Response({'details':'Your token was exired'},status=status.HTTP_400_BAD_REQUEST)
        except InvalidSignatureError:
            return Response({'details':'Your token is invalid'},status=status.HTTP_400_BAD_REQUEST)
        user_id = token.get('user_id')
        user = User.objects.get(id=user_id)
        if  user.is_verified:
            return Response({'details':'you oheriopwqhytiohywipt verified'},status=status.HTTP_200_OK)
        user.is_verified = True
        user.save()
        return Response({'details':'you are verified'},status=status.HTTP_200_OK)

class ResendVerification(generics.GenericAPIView):
    serializer_class = ResendVerificationSerializers
    def post(self,request,*args,**kwargs):
        data = self.serializer_class(data= request.data)
        data.is_valid(raise_exception=True)
        user = data.validated_data['user']
        email = data.validated_data['email']
        user=get_object_or_404(User,email=email)
        token= self.get_tokens_for_user(user)
        send_mail(
            'Subject here',
            f'http://localhost:8000/accounts/api/v1/email/activation/{token}',
            'from@example.com',
            ['to@example.com'],
            fail_silently=False,
        )

        return Response({'detail':'email sent'})
    
    def get_tokens_for_user(self,user):
        refresh = RefreshToken.for_user(user)
        return str(refresh.access_token)
    


class CustomObtainAuthToken(ObtainAuthToken):
    serializer_class = CustomAuthTokenSerializer
    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data,
                                           context={'request': request})
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']
        token, created = Token.objects.get_or_create(user=user)
        return Response({
            'token': token.key,
            'user_id': user.pk,
            'email': user.email
        })

class CustomDiscardAuthToken(APIView):
    permission_classes = [IsAuthenticated]
    def post(self,request):
        request.user.auth_token.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

class UserProfile(generics.RetrieveUpdateAPIView):
    serializer_class = UserProfileSerilizers
    permission_classes = [IsAuthenticated]
    queryset = Profile.objects.all()
    
    def get_object(self):
        queryset = self.get_queryset()
        obj = get_object_or_404(queryset, user=self.request.user)
        return obj

class SendEmailBackend(generics.GenericAPIView):
    def get(self,request,*args,**kwargs):
        user=get_object_or_404(User,email='admin@admin.com')
        token= self.get_tokens_for_user(user)
        send_mail(
            'Subject here',
            token,
            'from@example.com',
            ['to@example.com'],
            fail_silently=False,
        )
        return Response({'detail':'email sent'})


    def get_tokens_for_user(self,user):
        refresh = RefreshToken.for_user(user)
        return str(refresh.access_token)
