from datetime import date
from rest_framework import serializers
from .models import *



class TipoPersonagemSerializer(serializers.ModelSerializer):
    class Meta:
        model = TipoPersonagem
        fields = '__all__'
        read_only_fields = ['created_by', 'created_at', 'last_updated']
        
class SubAreaSerializer(serializers.ModelSerializer):
    class Meta:
        model = SubArea
        fields = '__all__'
        read_only_fields = ['created_by', 'created_at', 'last_updated']

class VantagemSerializer(serializers.ModelSerializer):
    class Meta:
        model = Vantagem
        fields = '__all__'
        read_only_fields = ['created_by', 'created_at', 'last_updated']
        
