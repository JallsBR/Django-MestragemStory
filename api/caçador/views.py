from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import get_object_or_404
from .models import *
from rest_framework import generics
from .serializer import *
from rest_framework.permissions import IsAuthenticated

class CredoCreateListView(generics.ListCreateAPIView):
    queryset = Credo.objects.all()
    serializer_class = CredoSerializer
    permission_classes = [IsAuthenticated] 

    def perform_create(self, serializer):
        serializer.save(created_by=self.request.user)
    
    
class CredoRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Credo.objects.all()
    serializer_class = CredoSerializer
    
    
    
class ImpetoCreateListView(generics.ListCreateAPIView):
    queryset = Impeto.objects.all()
    serializer_class = ImpetoSerializer
    permission_classes = [IsAuthenticated] 

    def perform_create(self, serializer):
        serializer.save(created_by=self.request.user)
    
    
class ImpetoRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Impeto.objects.all()
    serializer_class = ImpetoSerializer
    
    
class TrunfoCreateListView(generics.ListCreateAPIView):
    queryset = Trunfo.objects.all()
    serializer_class = TrunfoSerializer
    permission_classes = [IsAuthenticated] 

    def perform_create(self, serializer):
        serializer.save(created_by=self.request.user)
    
    
class TrunfoRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Trunfo.objects.all()
    serializer_class = TrunfoSerializer
    

class CaçadorCreateListView(generics.ListCreateAPIView):
    queryset = Caçador.objects.all()
    serializer_class = CaçadorSerializer
    permission_classes = [IsAuthenticated] 

    def perform_create(self, serializer):
        serializer.save(created_by=self.request.user)
    
    
class CaçadorRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Caçador.objects.all()
    serializer_class = CaçadorSerializer
    
class NotaCreateListView(generics.ListCreateAPIView):
    queryset = Nota.objects.all()
    serializer_class = NotaSerializer
    permission_classes = [IsAuthenticated] 

    def perform_create(self, serializer):
        serializer.save(created_by=self.request.user)
    
class NotaRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Nota.objects.all()
    serializer_class = NotaSerializer