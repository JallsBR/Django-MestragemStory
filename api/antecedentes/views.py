import json
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import get_object_or_404
from .models import *
from rest_framework import generics
from .serializer import *
from rest_framework.permissions import IsAuthenticated

# Nota
class TipoPersonagemCreateListView(generics.ListCreateAPIView):
    queryset = TipoPersonagem.objects.all()
    serializer_class = TipoPersonagemSerializer
    permission_classes = [IsAuthenticated] 

    def perform_create(self, serializer):
        serializer.save(created_by=self.request.user)
        
class TipoPersonagemRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = TipoPersonagem.objects.all()
    serializer_class = TipoPersonagemSerializer
        
        
class SubAreaCreateListView(generics.ListCreateAPIView):
    queryset = SubArea.objects.all()
    serializer_class = SubAreaSerializer
    permission_classes = [IsAuthenticated] 

    def perform_create(self, serializer):
        serializer.save(created_by=self.request.user)
        
        
class SubAreaRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = SubArea.objects.all()
    serializer_class = SubAreaSerializer
    

class VantagemCreateListView(generics.ListCreateAPIView):
    queryset = Vantagem.objects.all()
    serializer_class = VantagemSerializer
    permission_classes = [IsAuthenticated] 

    def perform_create(self, serializer):
        serializer.save(created_by=self.request.user)
    
class VantagemRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Vantagem.objects.all()
    serializer_class = VantagemSerializer