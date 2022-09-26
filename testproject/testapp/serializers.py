# from dataclasses import fields
from .models import Mkoa, Wilaya, Mazao
from rest_framework import serializers


class MkoaSerializer(serializers.ModelSerializer):
    mkoa_id = serializers.IntegerField(read_only=True, source='id')
    class Meta:
        model = Mkoa
        fields = '__all__'
        
class WilayaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Wilaya
        fields = '__all__'     
        
class MazaoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Mazao
        fields = '__all__'                