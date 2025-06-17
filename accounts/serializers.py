from rest_framework import serializers
from .models import User
from .models import JobSeekerProfile, EmployerProfile

class SignupSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = ('email', 'full_name', 'phone_number', 'role', 'password')

    def create(self, validated_data):
        return User.objects.create_user(**validated_data)

class JobSeekerProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = JobSeekerProfile
        fields = '__all__'
        

class EmployerProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = EmployerProfile
        fields = '__all__'
        