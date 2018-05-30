from rest_framework import serializers
from .models import Quakes

class QuakesSerializer(serializers.ModelSerializer):

    class Meta:
        model = Quakes
        fields = ('a', 'dd', 'dl', 'dr', 'dep', 'lat', 'lon', 'q', 's', 't')
