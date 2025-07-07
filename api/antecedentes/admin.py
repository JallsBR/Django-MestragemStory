from django.contrib import admin
from .models import *

@admin.register(TipoPersonagem)
class TipoPersonagemAdmin(admin.ModelAdmin):
    list_display = ('nome',)
    search_fields = ('nome',)
    ordering = ('nome',)
    exclude = ('created_by',)
    
    def save_model(self, request, obj, form, change):
        if not obj.pk: 
            obj.created_by = request.user
        obj.save()
        
@admin.register(SubArea)
class SubAreaPersonagemAdmin(admin.ModelAdmin):
    list_display = ('nome',)
    search_fields = ('nome',)
    ordering = ('nome',)
    exclude = ('created_by',)
    
    def save_model(self, request, obj, form, change):
        if not obj.pk: 
            obj.created_by = request.user
        obj.save()
        
@admin.register(Vantagem)
class VantagemPersonagemAdmin(admin.ModelAdmin):
    list_display = ('nome', 'arvore', 'tipo_personagem', 'sub_area', 'qualidade', 'pontuacao')
    search_fields = ('nome',)
    ordering = ('nome',)
    exclude = ('created_by',)
    
    def save_model(self, request, obj, form, change):
        if not obj.pk: 
            obj.created_by = request.user
        obj.save()
        
