from django.urls import path
from . import views


urlpatterns = [
    path('cidade/', views.CidadeCreateListView.as_view(), name='cidade-create-list'),
    path('cidade/<int:pk>/', views.CidadeRetrieveUpdateDestroyView.as_view() , name='cidade-detail-view'),
    
    path('cidade_nota/', views.NotaCreateListView.as_view(), name='nota-create-list'),
    path('cidade_nota/<int:pk>/', views.NotaRetrieveUpdateDestroyView.as_view() , name='nota-detail-view'),   
    
]

