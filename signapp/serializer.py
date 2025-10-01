from rest_framework import serializers
from .models import SignUpRegistration

class SignUpRegistrationSerializer(serializers.ModelSerializer):
    class Meta:
        model = SignUpRegistration
        fields = '__all__'