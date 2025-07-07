from django.contrib import admin
from .models import *


@admin.register(Cla)
class ClaAdmin(admin.ModelAdmin):
    list_display = ('nome', 'descricao', 'disciplinas', 'desvantagem')
    search_fields = ('nome',)
    ordering = ('nome',)
    exclude = ('created_by',)
    
    def save_model(self, request, obj, form, change):
        if not obj.pk:  
            obj.created_by = request.user
        obj.save()


@admin.register(Predador)
class PredadorAdmin(admin.ModelAdmin):
    list_display = ('nome', 'descricao', 'vantagens')
    search_fields = ('nome',)
    ordering = ('nome',)
    exclude = ('created_by',)
    def save_model(self, request, obj, form, change):
        if not obj.pk: 
            obj.created_by = request.user
        obj.save()


@admin.register(Disciplina)
class DisciplinaAdmin(admin.ModelAdmin):
    list_display = ('nome', 'descricao')
    search_fields = ('nome',)
    ordering = ('nome',)
    exclude = ('created_by',)
    
    def save_model(self, request, obj, form, change):
        if not obj.pk: 
            obj.created_by = request.user
        obj.save()


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


@admin.register(Vampiro)
class VampiroAdmin(admin.ModelAdmin):
    list_display = ('nome', 'jogador','cla', 'predador', 'geracao', )
    search_fields = ('nome', 'cla__nome', 'predador__nome')
    list_filter = ('cla', 'predador', 'geracao', 'jogador')
    ordering = ('nome',)
    autocomplete_fields = ['cla', 'predador', 'disciplinas', 'vantagens']
    exclude = ('created_by',)
    
    def save_model(self, request, obj, form, change):
        if not obj.pk: 
            obj.created_by = request.user
        obj.save()