from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from django.contrib.auth.models import User
from antecedentes.models import Vantagem
from uteis.personagem import Personagem

class Cla(models.Model):
    nome = models.CharField(max_length=100, verbose_name='Nome', unique=True, blank=False, null=False)
    descricao = models.TextField(verbose_name='Descricao', blank=True, null=True)
    disciplinas = models.TextField(verbose_name='Disciplinas', blank=True, null=True)
    desvantagem = models.TextField(verbose_name='Desvantagem', blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    last_updated = models.DateTimeField(auto_now=True)
    created_by = models.ForeignKey(User, on_delete=models.PROTECT, verbose_name='Criado por')
    
    class Meta:
        verbose_name = 'Clã'
        verbose_name_plural = 'Clãs'
        ordering = ['nome']

    def __str__(self):
        
        return self.nome  
    
    
class Predador(models.Model):
    nome = models.CharField(max_length=100, verbose_name='Nome', blank=False, null=False)
    descricao = models.TextField(verbose_name='Descricao', blank=True, null=True)    
    vantagens = models.TextField(verbose_name='vantagens', blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    last_updated = models.DateTimeField(auto_now=True)
    created_by = models.ForeignKey(User, on_delete=models.PROTECT, verbose_name='Criado por')
    
    class Meta:
        verbose_name = 'Predador'
        verbose_name_plural = 'Predadores'
        ordering = ['nome']
    def __str__(self):
        
        return self.nome  
    
class Disciplina(models.Model):
    nome = models.CharField(max_length=100, verbose_name='Nome', blank=False, null=False)
    nome_efeito = models.CharField(max_length=100, verbose_name='Nome efeito', blank=True, null=True) 
    pontuacao = models.IntegerField( blank=True, null=True, default=0, validators=[MinValueValidator(1), MaxValueValidator(10)] )
    descricao = models.TextField(verbose_name='Descricao', blank=True, null=True) 
    created_at = models.DateTimeField(auto_now_add=True)
    last_updated = models.DateTimeField(auto_now=True)
    created_by = models.ForeignKey(User, on_delete=models.PROTECT, verbose_name='Criado por')
    
    class Meta:
        verbose_name = 'Disciplina'
        verbose_name_plural = 'Disciplinas'
        ordering = ['nome']

    def __str__(self):
        
        return "{} {} - {}".format(self.nome, self.pontuacao, self.nome_efeito )
    

class Vampiro(Personagem):
    senhor = models.CharField(max_length=200, blank=True, null=True)
    geracao = models.CharField(max_length=200, verbose_name='geração', blank=True, null=True)     
    data_morte = models.DateField( verbose_name='data de morte', blank=True, null=True )
    ressonancia =  models.CharField(max_length=100,verbose_name= 'ressonância', blank=True, null=True, default=0, validators=[MinValueValidator(0), MaxValueValidator(5)] )
    fome =  models.IntegerField( blank=True, null=True, default=0, validators=[MinValueValidator(0), MaxValueValidator(10)] )
    potencia_sangue =  models.IntegerField( verbose_name='potência de sangue', blank=True, null=True, default=0, validators=[MinValueValidator(0), MaxValueValidator(10)] )
    humanidade =  models.IntegerField( blank=True, null=True, default=0, validators=[MinValueValidator(0), MaxValueValidator(10)] )  
    macula =  models.IntegerField( blank=True, null=True, default=0, validators=[MinValueValidator(0), MaxValueValidator(10)] )   
      
    cla = models.ForeignKey(Cla, on_delete=models.PROTECT, verbose_name='clã', related_name='vampire_cla', blank=True, null=True)
    predador = models.ForeignKey(Predador, on_delete=models.PROTECT, related_name='vampire_predador', blank=True, null=True)
    disciplinas = models.ManyToManyField( Disciplina, blank=True, verbose_name='Disciplina', related_name='disciplina')        
    
    
    class Meta:
        verbose_name = 'Vampiro'
        verbose_name_plural = 'Vampiros'
        ordering = ['nome']
    
    def __str__(self):
        return self.nome


class Nota(models.Model):
    nome = models.CharField(max_length=200, verbose_name='Nome', blank=False, null=False)
    vampiro = models.ForeignKey(Vampiro, on_delete=models.PROTECT, verbose_name='Vampiro', related_name='vampire_notas')
    descricao = models.TextField(verbose_name='Descrição', blank=True, null=True) 
    pontuacao = models.IntegerField( blank=True, null=True, default=0, validators=[MinValueValidator(0), MaxValueValidator(5)] )
    created_at = models.DateTimeField(auto_now_add=True)
    last_updated = models.DateTimeField(auto_now=True)
    created_by = models.ForeignKey(User, on_delete=models.PROTECT, related_name='vampiros_notas',verbose_name='Criado por')
    
    class Meta:
        verbose_name = 'Nota'
        verbose_name_plural = 'Notas'
        ordering = ['nome']

    def __str__(self):
        if self.pontuacao:
            return "{} - {}".format(self.nome, self.pontuacao)        
        return self.nome  

    
    