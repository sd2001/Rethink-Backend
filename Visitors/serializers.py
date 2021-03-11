from rest_framework import serializers
from .models import Register, RegisterVerify, Booking, PaymentVerify

class R_Serializer(serializers.ModelSerializer):
    class Meta:
        model = Register
        fields = '__all__'
        
class RV_Serializer(serializers.ModelSerializer):
    class Meta:
        model = RegisterVerify
        fields = '__all__'

class B_Serializer(serializers.ModelSerializer):
    class Meta:
        model = Booking
        fields = '__all__'

class BV_Serializer(serializers.ModelSerializer):
    class Meta:
        model = PaymentVerify
        fields = '__all__'