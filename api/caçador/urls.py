from django.urls import path
from . import views


urlpatterns = [
    path('credo/', views.CredoCreateListView.as_view(), name='credo-create-list'),
    path('credo/<int:pk>/', views.CredoRetrieveUpdateDestroyView.as_view() , name='credo-detail-view'),
    
    path('impeto/', views.ImpetoCreateListView.as_view(), name='impeto-create-list'),
    path('impeto/<int:pk>/', views.ImpetoRetrieveUpdateDestroyView.as_view() , name='impeto-detail-view'),
    
    path('trunfo/', views.TrunfoCreateListView.as_view(), name='trunfo-create-list'),
    path('trunfo/<int:pk>/', views.TrunfoRetrieveUpdateDestroyView.as_view() , name='trunfo-detail-view'),
    
    path('caçador_nota/', views.NotaCreateListView.as_view(), name='caçador_nota-create-list'),
    path('caçador_nota/<int:pk>/', views.NotaRetrieveUpdateDestroyView.as_view() , name='caçador_nota-detail-view'),
    
    path('caçador/', views.CaçadorCreateListView.as_view(), name='caçador-create-list'),
    path('caçador/<int:pk>/', views.CaçadorRetrieveUpdateDestroyView.as_view() , name='caçador-detail-view'),
    
]

