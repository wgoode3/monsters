from django.shortcuts import render
from .models import Monster
from rest_framework import viewsets
from .serializers import MonsterSerializer
from rest_framework.views import APIView
from rest_framework.response import Response

# Create your views here.

class MonsterViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = Monster.objects.all().order_by('name')
    serializer_class = MonsterSerializer
