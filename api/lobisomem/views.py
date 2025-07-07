import json
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import get_object_or_404
from .models import *
from rest_framework import generics
from .serializer import *
from rest_framework.permissions import IsAuthenticated



class TriboCreateListView(generics.ListCreateAPIView):
    queryset = Tribo.objects.all()
    serializer_class = TriboSerializer
    permission_classes = [IsAuthenticated] 

    def perform_create(self, serializer):
        serializer.save(created_by=self.request.user)
    
    
class TriboRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Tribo.objects.all()
    serializer_class = TriboSerializer


class PatronoCreateListView(generics.ListCreateAPIView):
    queryset = Patrono.objects.all()
    serializer_class = PatronoSerializer
    permission_classes = [IsAuthenticated] 

    def perform_create(self, serializer):
        serializer.save(created_by=self.request.user)
    
class PatronoRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Patrono.objects.all()
    serializer_class = PatronoSerializer
   
 
class DomCreateListView(generics.ListCreateAPIView):
    queryset = Dom.objects.all()
    serializer_class = DomSerializer
    permission_classes = [IsAuthenticated] 

    def perform_create(self, serializer):
        serializer.save(created_by=self.request.user)
    
class DomRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Dom.objects.all()
    serializer_class = DomSerializer

   

class AugurioCreateListView(generics.ListCreateAPIView):
    queryset = Augurio.objects.all()
    serializer_class = AugurioSerializer
    permission_classes = [IsAuthenticated] 

    def perform_create(self, serializer):
        serializer.save(created_by=self.request.user)
    
class AugurioRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Augurio.objects.all()
    serializer_class = NotaSerializer
    

class RitualCreateListView(generics.ListCreateAPIView):
    queryset = Ritual.objects.all()
    serializer_class = RitualSerializer
    permission_classes = [IsAuthenticated] 

    def perform_create(self, serializer):
        serializer.save(created_by=self.request.user)
    
class RitualRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Ritual.objects.all()
    serializer_class = RitualSerializer
    
    

class LobisomemCreateListView(generics.ListCreateAPIView):
    queryset = Lobisomem.objects.all()
    serializer_class = LobisomemSerializer
    permission_classes = [IsAuthenticated] 

    def perform_create(self, serializer):
        serializer.save(created_by=self.request.user)
    
class LobisomemRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Lobisomem.objects.all()
    serializer_class = LobisomemSerializer
    

class FormasCreateListView(generics.ListCreateAPIView):
    queryset = Formas.objects.all()
    serializer_class = FormasSerializer
    permission_classes = [IsAuthenticated] 

    def perform_create(self, serializer):
        serializer.save(created_by=self.request.user)
    
class FormasRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Formas.objects.all()
    serializer_class = FormasSerializer
    
class NotaCreateListView(generics.ListCreateAPIView):
    queryset = Nota.objects.all()
    serializer_class = NotaSerializer
    permission_classes = [IsAuthenticated] 

    def perform_create(self, serializer):
        serializer.save(created_by=self.request.user)
    
class NotaRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Nota.objects.all()
    serializer_class = NotaSerializer