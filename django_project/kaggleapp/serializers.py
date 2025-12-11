from rest_framework import serializers
from .models import HouseRent, PatientData, Results

class HostRentSerializer(serializers.ModelSerializer):

    class Meta:
        model=HouseRent
        fields='__all__'

class PatientDataSerializer(serializers.ModelSerializer):
    class Meta:
        model=PatientData
        fields='__all__'

class ResultsSerializer(serializers.ModelField):
    class Meta:
        model=Results
        fields='__all__'