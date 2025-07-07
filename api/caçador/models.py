from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from django.contrib.auth.models import User
from uteis.personagem import Personagem

class Credo(models.Model):
    nome = models.CharField(max_length=100, verbose_name='Nome', unique=True, blank=False, null=False)
    descricao = models.TextField(verbose_name='descrição', blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    last_updated = models.DateTimeField(auto_now=True)
    created_by = models.ForeignKey(User, on_delete=models.PROTECT, verbose_name='Criado por')
    
    class Meta:
        verbose_name = 'Credo'
        verbose_name_plural = 'Credos'
        ordering = ['nome']

    def __str__(self):
        
        return self.nome  
    
    
class Impeto(models.Model):
    nome = models.CharField(max_length=100, verbose_name='Nome', blank=False, null=False)
    descricao = models.TextField(verbose_name='descrição', blank=True, null=True)
    redencao = models.TextField(verbose_name='redenção', blank=True, null=True) 
    descricao_redencao = models.TextField(verbose_name='descrição da redenção', blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    last_updated = models.DateTimeField(auto_now=True)
    created_by = models.ForeignKey(User, on_delete=models.PROTECT, verbose_name='Criado por')
    
    class Meta:
        verbose_name = 'Ímpeto'
        verbose_name_plural = 'Ímpetos'
        ordering = ['nome']
    def __str__(self):
        
        return self.nome  
    
    
class Trunfo(models.Model):
    arvore = models.ForeignKey('self', on_delete=models.PROTECT, verbose_name='árvore', blank=True, null=True)
    nome = models.CharField(max_length=100, verbose_name='nome', blank=False, null=False)
    descricao = models.TextField(verbose_name='descrição', blank=True, null=True) 
    parada_trunfo = models.TextField(verbose_name='parada do trunfo', blank=True, null=True)
    sistema = models.TextField(verbose_name='sistema', blank=True, null=True)
    pontuacao = models.IntegerField( blank=True, null=True, default=0, validators=[MinValueValidator(0), MaxValueValidator(5)] )
    created_at = models.DateTimeField(auto_now_add=True)
    last_updated = models.DateTimeField(auto_now=True)
    created_by = models.ForeignKey(User, on_delete=models.PROTECT, verbose_name='Criado por')
    
    class Meta:
        verbose_name = 'Trunfo'
        verbose_name_plural = 'Trunfos'
        ordering = ['nome']

    def __str__(self):
        
        return "{} - {}".format(self.nome, self.pontuacao)        

class Caçador(Personagem):
    celula =  models.CharField(max_length=100,verbose_name= 'célula', blank=True, null=True, default=0, validators=[MinValueValidator(0), MaxValueValidator(5)] )
    desespero =  models.IntegerField( blank=True, null=True, default=0, validators=[MinValueValidator(0), MaxValueValidator(10)] )   
      
    credo = models.ForeignKey(Credo, on_delete=models.PROTECT, verbose_name='credo', related_name='caçador_credo', blank=True, null=True)
    impeto = models.ForeignKey(Impeto, on_delete=models.PROTECT, related_name='impeto', blank=True, null=True)
    trunfo = models.ManyToManyField( Trunfo, blank=True, verbose_name='trunfo', related_name='cacador_trunfo')        
    
    
    class Meta:
        verbose_name = 'Caçador'
        verbose_name_plural = 'Caçadores'
        ordering = ['nome']
    
    def __str__(self):
        return self.nome


class Nota(models.Model):
    nome = models.CharField(max_length=200, blank=False, null=False)
    cacador = models.ForeignKey(Caçador, on_delete=models.PROTECT, verbose_name='caçador', related_name='caçador_notas')
    descricao = models.TextField(verbose_name='descrição', blank=True, null=True) 
    pontuacao = models.IntegerField( blank=True, null=True, default=0, validators=[MinValueValidator(0), MaxValueValidator(5)] )
    created_at = models.DateTimeField(auto_now_add=True)
    last_updated = models.DateTimeField(auto_now=True)
    created_by = models.ForeignKey(User, on_delete=models.PROTECT, related_name='caçador_notas',verbose_name='Criado por')
    
    class Meta:
        verbose_name = 'Nota'
        verbose_name_plural = 'Notas'
        ordering = ['nome']

    def __str__(self):
        if self.pontuacao:
            return "{} - {}".format(self.nome, self.pontuacao)        
        return self.nome  

    
    