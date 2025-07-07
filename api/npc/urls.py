from django.urls import path
from . import views


urlpatterns = [
    path('npc_nota/', views.NotaCreateListView.as_view(), name='nota-create-list'),
    path('npc_nota/<int:pk>/', views.NotaRetrieveUpdateDestroyView.as_view() , name='nota-detail-view'),
    
    path('excepcional/', views.ExcepcionalCreateListView.as_view(), name='excepcional-create-list'),
    path('excepcional/<int:pk>/', views.ExcepcionalRetrieveUpdateDestroyView.as_view() , name='excepcional-detail-view'),
    
    path('npc/', views.NpcCreateListView.as_view(), name='npc-create-list'),
    path('npc/<int:pk>/', views.NpcRetrieveUpdateDestroyView.as_view() , name='npc-detail-view'),
   
    
]

