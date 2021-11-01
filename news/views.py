from django.shortcuts import render
from django.contrib.auth import authenticate
from django.contrib.auth.models import User
from rest_framework import status
from rest_framework.authtoken.models import Token
from rest_framework.decorators import api_view, permission_classes
from rest_framework.generics import ListAPIView, ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.pagination import PageNumberPagination
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from .serializers import *
from .models import *


class NewsListAPIView(APIView):
    def get(self, request):
        news = News.objects.all()
        data = NewsListSerializer(news, many=True, context={
            'request': request
        }).data
        return Response(data=data)


class NewsFullListAPIView(APIView):
    def get(self, request, pk):
        news = News.objects.get(id=pk)
        data = NewFullListSerializer(news, many=False, context={
            'request': request
        }).data
        return Response(data=data)


class LawListAPIView(APIView):
    def get(self, request):
        law = Law.objects.all()
        data = LawListSerializer(law, many=True, context={
            'request': request
        }).data
        return Response(data=data)


class LawFullListAPIView(APIView):
    def get(self, request, pk):
        law = Law.objects.get(id=pk)
        data = LawFullListSerializer(law, many=False, context={
            'request': request
        }).data
        return Response(data=data)


class PublicationListAPIView(APIView):
    def get(self, request):
        publication = Publication.objects.all()
        data = PublicationListSerializer(publication, many=True, context={
            'request': request
        }).data
        return Response(data=data)


# class PublicationFullListAPIView(APIView):
#     def get(self, request, pk):
#         publication = Publication.objects.get(id=pk)
#         data = PublicationListSerializer(publication, many=True, context={
#             'request': request
#         }).data
#         return Response(data=data)





