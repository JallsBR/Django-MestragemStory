
from django.contrib import admin
from django.urls import path, include
from django.http import JsonResponse


urlpatterns = [
    
    path('admin/', admin.site.urls),
    path('api/v1/auth/', include('accounts.urls')),
    
    path('api/v1/', include('vampiro.urls')),
    path('api/v1/', include('npc.urls')),
    path('api/v1/', include('cidade.urls')),
    path('api/v1/', include('antecedentes.urls')),
    path('api/v1/', include('caçador.urls')),
    path('api/v1/', include('lobisomem.urls')),
    

]
