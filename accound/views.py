import datetime
import random

from django.contrib.auth import authenticate
from django.contrib.auth.models import User
from django.shortcuts import render

# Create your views here.
from rest_framework import status
from rest_framework.authtoken.models import Token
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import ConfirmCode


class RegisterAPIView(APIView):
    def post(self, request):
        username = request.data['username']
        password = request.data['password']
        user = User.objects.create_user(
            username=username,
            email="a@n.ru",
            password=password,
            is_active=False
        )
        code = str(random.randint(1000, 9999))
        valid_time = datetime.datetime.now() + datetime.timedelta(minutes=20)
        ConfirmCode.objects.create(user=user, code=code, valid_until=valid_time)
        # send_code_to_phone(code, username)
        return Response(data={'massage': 'User created'})


class ConfirmAPIView(APIView):
    def post(self, request):
        code = request.data['code']
        code_list = ConfirmCode.objects.filter(code=code, valid_until__gte=datetime.datetime.now())

        if code_list:
            user = code_list[0]
            user.is_active = True
            user.save()
            code_list.delete()
            return Response(data={'massage': 'user activated'})
        else:
            return Response(status=status.HTTP_404_NOT_FOUND)