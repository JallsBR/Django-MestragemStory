from django.urls import path
from . import views


urlpatterns = [
    path('tipo_personagem/', views.TipoPersonagemCreateListView.as_view(), name='tipo-personagem-create-list'),
    path('tipo_personagem/<int:pk>/', views.TipoPersonagemRetrieveUpdateDestroyView.as_view() , name='tipo-personagem-detail-view'),
    
    path('subarea/', views.SubAreaCreateListView.as_view(), name='subarea-create-list'),
    path('subarea/<int:pk>/', views.SubAreaRetrieveUpdateDestroyView.as_view() , name='subarea-detail-view'),
    
    path('vantagem/', views.VantagemCreateListView.as_view(), name='vantagem-create-list'),
    path('vantagem/<int:pk>/', views.VantagemRetrieveUpdateDestroyView.as_view() , name='vantagem-detail-view'),

]

