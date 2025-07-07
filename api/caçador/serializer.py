from datetime import date
from rest_framework import serializers
from .models import *
from django.db.models import Avg, Count


class CredoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Credo
        fields = '__all__'
        read_only_fields = ['created_by', 'created_at', 'last_updated']
        
class ImpetoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Impeto
        fields = '__all__'
        read_only_fields = ['created_by', 'created_at', 'last_updated']

class TrunfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Trunfo
        fields = '__all__'
        read_only_fields = ['created_by', 'created_at', 'last_updated']
        
class CaçadorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Caçador
        fields = '__all__'
        read_only_fields = ['created_by', 'created_at', 'last_updated']
        
class NotaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Nota
        fields = '__all__'
        read_only_fields = ['created_by', 'created_at', 'last_updated']
   