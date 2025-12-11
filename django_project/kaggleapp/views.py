from rest_framework import generics
from .models import HouseRent, PatientData, Results
from .serializers import HostRentSerializer, PatientDataSerializer, ResultsSerializer

class ListHostRent(generics.ListAPIView):
    queryset=HouseRent.objects.all()
    serializer_class=HostRentSerializer
    
