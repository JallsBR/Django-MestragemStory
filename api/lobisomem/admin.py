from django.contrib import admin
from .models import *


@admin.register(Tribo)
class TriboAdmin(admin.ModelAdmin):
    list_display = ('nome', 'descricao',)
    search_fields = ('nome',)
    ordering = ('nome',)
    exclude = ('created_by',)
    
    def save_model(self, request, obj, form, change):
        if not obj.pk:  
            obj.created_by = request.user
        obj.save()

@admin.register(Patrono)
class PatronoAdmin(admin.ModelAdmin):
    list_display = ('nome', 'descricao',)
    search_fields = ('nome',)
    ordering = ('nome',)
    exclude = ('created_by',)
    
    def save_model(self, request, obj, form, change):
        if not obj.pk:  
            obj.created_by = request.user
        obj.save()
        
@admin.register(Augurio)
class AugurioAdmin(admin.ModelAdmin):
    list_display = ('nome', 'lua','descricao',)
    search_fields = ('nome',)
    ordering = ('nome',)
    exclude = ('created_by',)
    
    def save_model(self, request, obj, form, change):
        if not obj.pk:  
            obj.created_by = request.user
        obj.save()
        
@admin.register(Dom)
class DomAdmin(admin.ModelAdmin):
    list_display = ('nome', 'total_renome',)
    search_fields = ('nome',)
    ordering = ('nome', 'total_renome',)
    exclude = ('created_by',)
    
    def save_model(self, request, obj, form, change):
        if not obj.pk:  
            obj.created_by = request.user
        obj.save()

@admin.register(Ritual)
class RitualAdmin(admin.ModelAdmin):
    list_display = ('nome',)
    search_fields = ('nome',)
    ordering = ('nome',)
    exclude = ('created_by',)
    
    def save_model(self, request, obj, form, change):
        if not obj.pk:  
            obj.created_by = request.user
        obj.save()
        
@admin.register(Lobisomem)
class LobisomemAdmin(admin.ModelAdmin):
    list_display = ('nome', 'tribo', 'caern', 'patrono', 'augurio', )
    search_fields = ('nome',)
    ordering = ('nome',)
    exclude = ('created_by',)
    
    def save_model(self, request, obj, form, change):
        if not obj.pk:  
            obj.created_by = request.user
        obj.save()
        
@admin.register(Formas)
class FormasAdmin(admin.ModelAdmin):
    list_display = ('nome', )
    search_fields = ('nome',)
    ordering = ('nome', )
    exclude = ('created_by',)
    
    def save_model(self, request, obj, form, change):
        if not obj.pk:  
            obj.created_by = request.user
        obj.save()
        
@admin.register(Nota)
class NotaAdmin(admin.ModelAdmin):
    list_display = ('nome', 'pontuacao', 'lobisomem' )
    search_fields = ('nome',)
    ordering = ('nome', )
    exclude = ('created_by',)
    
    def save_model(self, request, obj, form, change):
        if not obj.pk:  
            obj.created_by = request.user
        obj.save()