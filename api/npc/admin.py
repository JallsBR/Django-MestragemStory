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
    
@admin.register(Excepcional)
class ExcepcionalAdmin(admin.ModelAdmin):
    list_display = ('nome', 'pontuacao')
    search_fields = ('nome',)
    ordering = ('nome',)
    exclude = ('created_by',)
    
    def save_model(self, request, obj, form, change):
        if not obj.pk: 
            obj.created_by = request.user
        obj.save()

@admin.register(Npc)
class NpcAdmin(admin.ModelAdmin):
    list_display = ('nome', 'dificuldade')
    search_fields = ('nome', 'dificuldade')
    ordering = ('nome', 'dificuldade')
    autocomplete_fields = ['excepcionais', 'notas']
    exclude = ('created_by',)
    
    def save_model(self, request, obj, form, change):
        if not obj.pk: 
            obj.created_by = request.user
        obj.save()