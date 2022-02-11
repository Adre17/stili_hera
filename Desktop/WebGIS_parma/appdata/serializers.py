from rest_framework import serializers
from .models import prove_geognostiche

class ProveSerializer(serializers.ModelSerializer):
    class Meta:
        model = prove_geognostiche
        fields = ('id', 'geom')
        #fields = '__all__' #per portare tutti i campi del modello