from django.shortcuts import render

from django.contrib.auth.models import User, Group
from .models import ValorCambio
from rest_framework import viewsets
from rest_framework import permissions
from quickstart.serializers import ValorCambioSerializer


class ValorCambioViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = ValorCambio.objects.all().order_by('-fecha')
    serializer_class = ValorCambioSerializer
    #permission_classes = [permissions.IsAuthenticated]

