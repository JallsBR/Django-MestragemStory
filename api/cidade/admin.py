from django.contrib import admin
from .models import *

@admin.register(Nota)
class NotaAdmin(admin.ModelAdmin):
    list_display = ('nome', 'pontuacao', 'descricao')
    search_fields = ('nome',)
    ordering = ('nome',)
    exclude = ('created_by',)
    
    def save_model(self, request, obj, form, change):
        if not obj.pk: 
            obj.created_by = request.user
        obj.save()

@admin.register(Cidade)
class CidadeAdmin(admin.ModelAdmin):
    list_display = ('nome', 'idade', 'estado', 'pais', 'populacao')
    search_fields = ('nome', 'estado', 'pais')
    ordering = ('nome', 'estado', 'pais')
    autocomplete_fields = ['vampiros', 'npcs']
    exclude = ('created_by',)
    
    def save_model(self, request, obj, form, change):
        if not obj.pk: 
            obj.created_by = request.user
        obj.save()