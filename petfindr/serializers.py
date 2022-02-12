from rest_framework import serializers
from .models import Pet

class PetSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')
    class Meta:
        model = Pet
        fields = ('id', 'status', 'name', 'type', 'gender', 'size', 'color', 'description', 'microchip', 'location', 'created_at', 'reported_time', 'owner', 'photo')