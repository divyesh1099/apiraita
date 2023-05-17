from rest_framework import serializers
from .models import APOD

class APODSerializer(serializers.ModelSerializer):
    class Meta:
        model = APOD
        fields = ("__all__")