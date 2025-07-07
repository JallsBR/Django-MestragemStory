import json
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import get_object_or_404
from .models import *
from rest_framework import generics
from .serializer import *
from rest_framework.permissions import IsAuthenticated


# Clã
class ClaCreateListView(generics.ListCreateAPIView):
    queryset = Cla.objects.all()
    serializer_class = ClaSerializer
    permission_classes = [IsAuthenticated] 

    def perform_create(self, serializer):
        serializer.save(created_by=self.request.user)
    
    
class ClaRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Cla.objects.all()
    serializer_class = ClaSerializer

# Predador
class PredadorCreateListView(generics.ListCreateAPIView):
    queryset = Predador.objects.all()
    serializer_class = PredadorSerializer
    permission_classes = [IsAuthenticated] 

    def perform_create(self, serializer):
        serializer.save(created_by=self.request.user)
    
class PredadorRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Predador.objects.all()
    serializer_class = PredadorSerializer
   
# Disciplina 
class DisciplinaCreateListView(generics.ListCreateAPIView):
    queryset = Disciplina.objects.all()
    serializer_class = DisciplinaSerializer
    permission_classes = [IsAuthenticated] 

    def perform_create(self, serializer):
        serializer.save(created_by=self.request.user)
    
class DisciplinaRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Disciplina.objects.all()
    serializer_class = DisciplinaSerializer

   
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
    
# Vampiro
class VampiroCreateListView(generics.ListCreateAPIView):
    queryset = Vampiro.objects.all()
    serializer_class = VampiroSerializer
    permission_classes = [IsAuthenticated] 

    def perform_create(self, serializer):
        serializer.save(created_by=self.request.user)
    
class VampiroRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Vampiro.objects.all()
    serializer_class = VampiroSerializer