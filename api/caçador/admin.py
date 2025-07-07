from django.contrib import admin
from .models import *


@admin.register(Credo)
class CredoAdmin(admin.ModelAdmin):
    list_display = ('nome', 'descricao',)
    search_fields = ('nome',)
    ordering = ('nome',)
    exclude = ('created_by',)
    
    def save_model(self, request, obj, form, change):
        if not obj.pk:  
            obj.created_by = request.user
        obj.save()
        
@admin.register(Impeto)
class ImpetoAdmin(admin.ModelAdmin):
    list_display = ('nome', 'descricao',)
    search_fields = ('nome',)
    ordering = ('nome',)
    exclude = ('created_by',)
    
    def save_model(self, request, obj, form, change):
        if not obj.pk:  
            obj.created_by = request.user
        obj.save()
        
@admin.register(Trunfo)
class TrunfoAdmin(admin.ModelAdmin):
    list_display = ('nome', 'descricao',)
    search_fields = ('nome',)
    ordering = ('nome',)
    exclude = ('created_by',)
    
    def save_model(self, request, obj, form, change):
        if not obj.pk:  
            obj.created_by = request.user
        obj.save()
        
@admin.register(Caçador)
class CaçadorAdmin(admin.ModelAdmin):
    list_display = ('nome', 'celula', 'credo', 'impeto')
    search_fields = ('nome',)
    ordering = ('nome',)
    exclude = ('created_by',)
    
    def save_model(self, request, obj, form, change):
        if not obj.pk:  
            obj.created_by = request.user
        obj.save()