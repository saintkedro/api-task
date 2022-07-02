from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework import generics
from django.contrib.auth import get_user_model
from rest_framework.response import Response
from .serializers import LinkSerializer
from .models import Link



# Create your views here.

class PostListApi(generics.ListAPIView):
    queryset = Link.objects.filter(active=True)
    serialIzer_class = LinkSerializer

class PostCreateApi(generics.CreateAPIView):
    queryset = Link.objects.filter(active=True)
    serialIzer_class = LinkSerializer

class PostDetailApi(generics.RetrieveAPIView):
    queryset = Link.objects.filter(active=True)
    serialIzer_class = LinkSerializer

class PostUpdateApi(generics.UpdateAPIView):
    queryset = Link.objects.filter(active=True)
    serialIzer_class = LinkSerializer

class PostDeleteApi(generics.DestroyAPIView):
    queryset = Link.objects.filter(active=True)
    serialIzer_class = LinkSerializer