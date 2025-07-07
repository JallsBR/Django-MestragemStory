from datetime import date
from rest_framework import serializers
from .models import *
from django.db.models import Avg, Count


      
class NotaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Nota
        fields = '__all__'
        read_only_fields = ['created_by', 'created_at', 'last_updated']
        
class CidadeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cidade
        fields = '__all__'
        read_only_fields = ['created_by', 'created_at', 'last_updated']
        