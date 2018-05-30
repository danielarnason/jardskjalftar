from rest_framework import generics
from .serializers import QuakesSerializer
from .models import Quakes

class CreateView(generics.ListCreateAPIView):
    queryset = Quakes.objects.all()
    serializer_class = QuakesSerializer
