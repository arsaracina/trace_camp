from django.shortcuts import render
from rest_framework import viewsets
from kick_api.models import KickStarter
from kick_api.serializer import KickStarterSerializer

class KickStarterViewSet(viewsets.ModelViewSet):
    queryset = KickStarter.objects.all()
    serializer_class = KickStarterSerializer




# Create your views here.
