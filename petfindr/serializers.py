from rest_framework import serializers
from .models import Pet

class PetSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')
    owner_email = serializers.ReadOnlyField(source='owner.email')
    class Meta:
        model = Pet
        fields = ('id', 'status', 'name', 'type', 'gender', 'size', 'color', 'description', 'microchip', 'location', 'created_at', 'reported_time', 'owner', 'photo', 'phone_number', 'owner_email')