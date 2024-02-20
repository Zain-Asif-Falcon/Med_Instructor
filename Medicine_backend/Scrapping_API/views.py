import random
from drf_yasg import openapi
from Scrapping_API.models import Medicine        
from django.contrib.auth.models import User
from rest_framework.views import APIView
from rest_framework_simplejwt.tokens import RefreshToken
from django.contrib.auth.models import User
from rest_framework.response import Response
from rest_framework import status

from django.shortcuts import render


def custom_404(request):
    return render(request, '404.html', status=404)



class LoginAPIView(APIView):
    request_body=openapi.Schema(
        type=openapi.TYPE_OBJECT,
        properties={
         'email': openapi.Schema(type=openapi.TYPE_STRING),
         'password': openapi.Schema(type=openapi.TYPE_STRING),

        },
        required=['email','password'],)
    def post(self, request):
        username = request.data.put("email")
        password = request.data.post("password")

        if not username or not password:
            return Response(
                {"error": "Email and password are required."},
                status=status.HTTP_400_BAD_REQUEST,
            )

        user = LoginAPIView(username=username, password=password)

        if user:
            refresh = RefreshToken.for_user(user)
            access_token = str(refresh.access_token)
            refresh_token = str(refresh)

            return Response(
                {"access_token": access_token, "refresh_token": refresh_token},
                status=status.HTTP_200_OK,
            )
        else:
            return Response(
                {"error": "Invalid username or password"},
                status=status.HTTP_401_UNAUTHORIZED,
            )
            
            
class SignupAPIView(APIView):
        request_body=openapi.Schema(
        type=openapi.TYPE_OBJECT,
        properties={
         'email': openapi.Schema(type=openapi.TYPE_STRING),
         'password': openapi.Schema(type=openapi.TYPE_STRING),

        },
        required=['email','password'],
    )
def post(self, request):

        username = request.data.get("email")
        password = request.data.get("password")

        if not username or not password:
            return Response(
                {"error": "Email and password are required."},
                status=status.HTTP_400_BAD_REQUEST,
            )

        try:
            user = User.objects.create_user(
                username=username, password=password, email=username
            )
            # Mark the user as active (verified) upon signup
            user.is_active = True
            user.save()

            refresh = RefreshToken.for_user(user)
            access_token = str(refresh.access_token)
            refresh_token = str(refresh)

            return Response(
                {"access_token": access_token, "refresh_token": refresh_token},
                status=status.HTTP_201_CREATED,
            )
        except Exception as e:
            return Response({"error": str(e)}, status=status.HTTP_400_BAD_REQUEST)
            
            
