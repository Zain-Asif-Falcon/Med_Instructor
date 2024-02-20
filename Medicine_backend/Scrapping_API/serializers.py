
from rest_framework import serializers

from Scrapping_API.models import Medicine


class MedicineSerializer(serializers.ModelSerializer):
    class Meta:
        model = Medicine
        fields = ['name', 'description']


class SignUpSerializer(serializers.Serializer):
    first_name = serializers.CharField(max_length=20)
    last_name = serializers.CharField(max_length=20)
    email = serializers.EmailField()
    password = serializers.CharField(max_length=20)
    age = serializers.CharField(max_length=20)
    role = serializers.CharField(max_length=20)
    
    
    