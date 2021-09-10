from django.contrib.auth.models import User, Group
from rest_framework import serializers
from .models import ValorCambio


class ValorCambioSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = ValorCambio
        fields = ['url', 'valor', 'fecha']
