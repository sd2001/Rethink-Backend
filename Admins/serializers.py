from rest_framework import serializers
from .models import CreatePractioner

class CreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = CreatePractioner
        fields = '__all__'
