from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from django.contrib.auth.models import User
from django.utils import timezone


class Nota(models.Model):
    nome = models.CharField(max_length=200, verbose_name='Nome', blank=False, null=False)
    descricao = models.TextField(verbose_name='descrição', blank=True, null=True) 
    pontuacao = models.IntegerField( verbose_name='pontuação',blank=True, null=True, default=0, validators=[MinValueValidator(0), MaxValueValidator(20)] )
    created_at = models.DateTimeField(auto_now_add=True)
    last_updated = models.DateTimeField(auto_now=True)
    created_by = models.ForeignKey(User, on_delete=models.PROTECT, related_name='npcs_notas', verbose_name='Criado por')
    
    class Meta:
        verbose_name = 'Nota'
        verbose_name_plural = 'Notas'
        ordering = ['nome']

    def __str__(self):
        if self.pontuacao:
            return "{} - {}".format(self.nome, self.pontuacao)
        return self.nome  
    
    
class Excepcional(models.Model):
    nome = models.CharField(max_length=200, verbose_name='Nome', blank=False, null=False)
    pontuacao = models.IntegerField( blank=True, null=True, default=0, validators=[MinValueValidator(0), MaxValueValidator(20)] )
    created_at = models.DateTimeField(auto_now_add=True)
    last_updated = models.DateTimeField(auto_now=True)
    created_by = models.ForeignKey(User, on_delete=models.PROTECT, verbose_name='Criado por')
    
    class Meta:
        verbose_name = 'Atributo excepcional'
        verbose_name_plural = 'Atributos excepcionais'
        ordering = ['nome']

    def __str__(self):
        
        return "{} - {}".format(self.nome, self.pontuacao)
    
    
class Npc(models.Model):
    nome = models.CharField(max_length=100, verbose_name='Nome', unique=True, blank=False, null=False)
    dificuldade = models.IntegerField( verbose_name='Dificuldade', blank=True, null=True, default=0, validators=[MinValueValidator(0), MaxValueValidator(10)] )
    descricao = models.TextField(verbose_name='Descrição', blank=True, null=True)
    fisico = models.IntegerField( verbose_name='Físico', blank=True, null=True, default=0, validators=[MinValueValidator(0), MaxValueValidator(15)] )   
    mental = models.IntegerField( verbose_name='Mental', blank=True, null=True, default=0, validators=[MinValueValidator(0), MaxValueValidator(15)] )
    social = models.IntegerField( verbose_name='Social', blank=True, null=True, default=0, validators=[MinValueValidator(0), MaxValueValidator(15)] )
    vitalidade = models.IntegerField( verbose_name='Vitalidade', blank=True, null=True, default=0, validators=[MinValueValidator(0), MaxValueValidator(40)] )
    vontade = models.IntegerField( verbose_name='Força de Vontade', blank=True, null=True, default=0, validators=[MinValueValidator(0), MaxValueValidator(40)] )
    excepcionais = models.ManyToManyField(Excepcional, verbose_name='Atributos excepcionais', related_name='npcs_excepcionais', blank=True)
    especial = models.TextField(verbose_name='Especial', blank=True, null=True)
    notas = models.ManyToManyField(Nota, verbose_name='Notas', related_name='npcs_notas', blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    last_updated = models.DateTimeField(auto_now=True)
    created_by = models.ForeignKey(User, on_delete=models.PROTECT, verbose_name='Criado por')
    
    class Meta:
        verbose_name = 'Npc'
        verbose_name_plural = 'Npcs'
        ordering = ['nome', 'dificuldade']

    def __str__(self):
        if self.dificuldade:
            return "{} - dificuldade {}".format(self.nome, self.dificuldade)        
        return self.nome  