from datetime import date
from rest_framework import serializers
from .models import *
from django.db.models import Avg, Count


class ClaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cla
        fields = '__all__'
        read_only_fields = ['created_by', 'created_at', 'last_updated']
        
class PredadorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Predador
        fields = '__all__'
        read_only_fields = ['created_by', 'created_at', 'last_updated']

class DisciplinaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Disciplina
        fields = '__all__'
        read_only_fields = ['created_by', 'created_at', 'last_updated']
        
class VantagemSerializer(serializers.ModelSerializer):
    class Meta:
        model = Vantagem
        fields = '__all__'
        read_only_fields = ['created_by', 'created_at', 'last_updated']
        
class NotaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Nota
        fields = '__all__'
        read_only_fields = ['created_by', 'created_at', 'last_updated']
        
class VampiroSerializer(serializers.ModelSerializer):
    class Meta:
        model = Vampiro
        fields = '__all__'
        read_only_fields = ['created_by', 'created_at', 'last_updated']
        