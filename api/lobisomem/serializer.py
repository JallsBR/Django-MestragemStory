from datetime import date
from rest_framework import serializers
from .models import *
from django.db.models import Avg, Count


class TriboSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tribo
        fields = '__all__'
        read_only_fields = ['created_by', 'created_at', 'last_updated']
        
class PatronoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Patrono
        fields = '__all__'
        read_only_fields = ['created_by', 'created_at', 'last_updated']

class AugurioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Augurio
        fields = '__all__'
        read_only_fields = ['created_by', 'created_at', 'last_updated']
        
class DomSerializer(serializers.ModelSerializer):
    class Meta:
        model = Dom
        fields = '__all__'
        read_only_fields = ['created_by', 'created_at', 'last_updated']
        
class RitualSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ritual
        fields = '__all__'
        read_only_fields = ['created_by', 'created_at', 'last_updated']
        
class LobisomemSerializer(serializers.ModelSerializer):
    class Meta:
        model = Lobisomem
        fields = '__all__'
        read_only_fields = ['created_by', 'created_at', 'last_updated']
        
class FormasSerializer(serializers.ModelSerializer):
    class Meta:
        model = Formas
        fields = '__all__'
        read_only_fields = ['created_by', 'created_at', 'last_updated']
        
class NotaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Nota
        fields = '__all__'
        read_only_fields = ['created_by', 'created_at', 'last_updated']
        
        