from django.urls import path
from . import views


urlpatterns = [
    path('tribo/', views.TriboCreateListView.as_view(), name='tribo-create-list'),
    path('tribo/<int:pk>/', views.TriboRetrieveUpdateDestroyView.as_view() , name='tribo-detail-view'),
    
    path('patrono/', views.PatronoCreateListView.as_view(), name='patrono-create-list'),
    path('patrono/<int:pk>/', views.PatronoRetrieveUpdateDestroyView.as_view() , name='patrono-detail-view'),
    
    path('dom/', views.DomCreateListView.as_view(), name='dom-create-list'),
    path('dom/<int:pk>/', views.DomRetrieveUpdateDestroyView.as_view() , name='dom-detail-view'),
    
    path('lobisomem_nota/', views.NotaCreateListView.as_view(), name='lobisomem_nota-create-list'),
    path('lobisomem_nota/<int:pk>/', views.NotaRetrieveUpdateDestroyView.as_view() , name='lobisomem_nota-detail-view'),
    
    path('augurio/', views.AugurioCreateListView.as_view(), name='augurio-create-list'),
    path('augurio/<int:pk>/', views.AugurioRetrieveUpdateDestroyView.as_view() , name='augurio-detail-view'),
    
    path('ritual/', views.RitualCreateListView.as_view(), name='ritual-create-list'),
    path('ritual/<int:pk>/', views.RitualRetrieveUpdateDestroyView.as_view() , name='ritual-detail-view'),
    
    path('lobisomem/', views.LobisomemCreateListView.as_view(), name='lobisomem-create-list'),
    path('lobisomem/<int:pk>/', views.LobisomemRetrieveUpdateDestroyView.as_view() , name='lobisomem-detail-view'),
    
    path('forma/', views.FormasCreateListView.as_view(), name='forma-create-list'),
    path('forma/<int:pk>/', views.FormasRetrieveUpdateDestroyView.as_view() , name='forma-detail-view'),
    
]

