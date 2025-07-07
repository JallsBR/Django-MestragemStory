from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from django.contrib.auth.models import User

class TipoPersonagem(models.Model):       
    nome = models.CharField(max_length=200, verbose_name='Nome', blank=False, null=False) 
    created_at = models.DateTimeField(auto_now_add=True)
    last_updated = models.DateTimeField(auto_now=True)
    created_by = models.ForeignKey(User, on_delete=models.PROTECT, verbose_name='Criado por', related_name='antecedentes_tipos_personagem')
    
    class Meta:
        verbose_name = 'Tipo de personagem'
        verbose_name_plural = 'Tipos de personagem'
        ordering = ['nome']
    
    def __str__(self):
        return self.nome


class SubArea(models.Model):
    nome = models.CharField(max_length=200, verbose_name='Nome', blank=False, null=False)
    created_at = models.DateTimeField(auto_now_add=True)
    last_updated = models.DateTimeField(auto_now=True)
    created_by = models.ForeignKey(User, on_delete=models.PROTECT, verbose_name='Criado por', related_name='antecedentes_subareas')
    
    class Meta:
        verbose_name = 'Subárea'
        verbose_name_plural = 'Subáreas'
        ordering = ['nome']
    def __str__(self):
        return self.nome

class Vantagem(models.Model):
    arvore = models.ForeignKey('self', on_delete=models.PROTECT, verbose_name='árvore', blank=True, null=True)
    tipo_personagem = models.ForeignKey(TipoPersonagem, on_delete=models.PROTECT, verbose_name='tipo de personagem', blank=True, null=True)
    sub_area = models.ForeignKey(SubArea, on_delete=models.PROTECT, verbose_name='subárea', blank=True, null=True) 
    
    qualidade = models.IntegerField( default= 1, validators=[MinValueValidator(0), MaxValueValidator(1)], verbose_name='qualidade', blank=True, null=True)
    nome = models.CharField(max_length=200, verbose_name='Nome', blank=False, null=False)
    descricao = models.TextField(verbose_name='descrição', blank=True, null=True) 
    pontuacao = models.IntegerField( blank=True, null=True, default=0, validators=[MinValueValidator(0), MaxValueValidator(5)] )
    
    created_at = models.DateTimeField(auto_now_add=True)
    last_updated = models.DateTimeField(auto_now=True)
    created_by = models.ForeignKey(User, on_delete=models.PROTECT, verbose_name='Criado por', related_name='antecedentes_vantagens')
    
    class Meta:
        verbose_name = 'Vantagem'
        verbose_name_plural = 'Vantagens'
        ordering = ['nome']
        
    def __str__(self):
        qualidade_str = "Defeito" if self.qualidade == 0 else "Qualidade"
        return "{} - {} - {}".format(qualidade_str, self.nome, self.pontuacao)