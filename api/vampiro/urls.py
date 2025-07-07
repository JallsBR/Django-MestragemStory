from django.urls import path
from . import views


urlpatterns = [
    path('cla/', views.ClaCreateListView.as_view(), name='cla-create-list'),
    path('cla/<int:pk>/', views.ClaRetrieveUpdateDestroyView.as_view() , name='cla-detail-view'),
    
    path('predador/', views.PredadorCreateListView.as_view(), name='predador-create-list'),
    path('predador/<int:pk>/', views.PredadorRetrieveUpdateDestroyView.as_view() , name='predador-detail-view'),
    
    path('disciplina/', views.DisciplinaCreateListView.as_view(), name='disciplina-create-list'),
    path('disciplina/<int:pk>/', views.DisciplinaRetrieveUpdateDestroyView.as_view() , name='disciplina-detail-view'),
    
    path('vampiro_nota/', views.NotaCreateListView.as_view(), name='vampiro_nota-create-list'),
    path('vampiro_nota/<int:pk>/', views.NotaRetrieveUpdateDestroyView.as_view() , name='vampiro_nota-detail-view'),
    
    path('vampiro/', views.VampiroCreateListView.as_view(), name='vampiro-create-list'),
    path('vampiro/<int:pk>/', views.VampiroRetrieveUpdateDestroyView.as_view() , name='vampiro-detail-view'),
    
]

