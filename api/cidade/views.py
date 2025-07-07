import json
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import get_object_or_404
from .models import *
from rest_framework import generics
from .serializer import *
from rest_framework.permissions import IsAuthenticated

# Nota
class NotaCreateListView(generics.ListCreateAPIView):
    queryset = Nota.objects.all()
    serializer_class = NotaSerializer
    permission_classes = [IsAuthenticated] 

    def perform_create(self, serializer):
        serializer.save(created_by=self.request.user)
    
class NotaRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Nota.objects.all()
    serializer_class = NotaSerializer
    
# Cidade
class CidadeCreateListView(generics.ListCreateAPIView):
    queryset = Cidade.objects.all()
    serializer_class = CidadeSerializer
    permission_classes = [IsAuthenticated] 

    def perform_create(self, serializer):
        serializer.save(created_by=self.request.user)
    
class CidadeRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Cidade.objects.all()
    serializer_class = CidadeSerializer