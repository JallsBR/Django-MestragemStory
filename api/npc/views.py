import json
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import get_object_or_404
from .models import *
from rest_framework import generics
from .serializer import *
from rest_framework.permissions import IsAuthenticated


class NotaCreateListView(generics.ListCreateAPIView):
    queryset = Nota.objects.all()
    serializer_class = NotaSerializer
    permission_classes = [IsAuthenticated] 

    def perform_create(self, serializer):
        serializer.save(created_by=self.request.user)
        
class NotaRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Nota.objects.all()
    serializer_class = NotaSerializer
    
class ExcepcionalCreateListView(generics.ListCreateAPIView):
    queryset = Excepcional.objects.all()
    serializer_class = ExcepcionalSerializer
    permission_classes = [IsAuthenticated] 

    def perform_create(self, serializer):
        serializer.save(created_by=self.request.user)
        
class ExcepcionalRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Excepcional.objects.all()
    serializer_class = ExcepcionalSerializer

class  NpcCreateListView(generics.ListCreateAPIView):
    queryset =  Npc.objects.all()
    serializer_class =  NpcSerializer
    permission_classes = [IsAuthenticated] 

    def perform_create(self, serializer):
        serializer.save(created_by=self.request.user)

class NpcRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset =  Npc.objects.all()
    serializer_class =  NpcSerializer