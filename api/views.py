from rest_framework.response import Response
from rest_framework import generics
from .models import Family,Parent
from .serializers import FamilySerializer,ParentSerializer

# Create your views here.
class FamilyView(generics.ListCreateAPIView):
    queryset = Family.objects.all()
    serializer_class = FamilySerializer

class FamilyCreateView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Family.objects.all()
    serializer_class = FamilySerializer


