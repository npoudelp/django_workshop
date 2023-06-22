from rest_framework import serializers
from .models import blood_doner

class blood_doner_serializers(serializers.ModelSerializer):
    class Meta:
        model = blood_doner
        fields = '__all__'