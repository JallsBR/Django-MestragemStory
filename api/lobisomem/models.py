from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from django.contrib.auth.models import User
from antecedentes.models import Vantagem
from uteis.personagem import Personagem

class Tribo(models.Model):
    nome = models.CharField(max_length=100, verbose_name='Nome', unique=True, blank=False, null=False)
    descricao = models.TextField(verbose_name='Descricao', blank=True, null=True)   
    created_at = models.DateTimeField(auto_now_add=True)
    last_updated = models.DateTimeField(auto_now=True)
    created_by = models.ForeignKey(User, on_delete=models.PROTECT, verbose_name='Criado por')
    
    class Meta:
        verbose_name = 'Tribo'
        verbose_name_plural = 'Tribos'
        ordering = ['nome']

    def __str__(self):
        
        return self.nome  
    
    
class Patrono(models.Model):
    nome = models.CharField(max_length=100, verbose_name='Nome', blank=False, null=False)
    descricao = models.TextField(verbose_name='Descricao', blank=True, null=True)    
    vantagens = models.TextField(verbose_name='vantagens', blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    last_updated = models.DateTimeField(auto_now=True)
    created_by = models.ForeignKey(User, on_delete=models.PROTECT, verbose_name='Criado por')
    
    class Meta:
        verbose_name = 'Patrono'
        verbose_name_plural = 'Patronos'
        ordering = ['nome']
    def __str__(self):
        
        return self.nome  
    
class Augurio(models.Model):
    nome = models.CharField(max_length=100, verbose_name='nome', blank=False, null=False)
    lua = models.CharField(max_length=100, verbose_name='lua', blank=False, null=False)
    descricao = models.TextField(verbose_name='nescricao', blank=True, null=True)    
    created_at = models.DateTimeField(auto_now_add=True)
    last_updated = models.DateTimeField(auto_now=True)
    created_by = models.ForeignKey(User, on_delete=models.PROTECT, verbose_name='Criado por')
    
    class Meta:
        verbose_name = 'Aúgurio'
        verbose_name_plural = 'Aúgurios'
        ordering = ['nome']
    def __str__(self):
        
        return self.nome  
    
class Dom(models.Model):
    nome = models.CharField(max_length=100, verbose_name='Nome', blank=False, null=False)
    descricao = models.TextField(verbose_name='Descricao', blank=True, null=True) 
    total_renome = models.IntegerField( blank=True, null=True, default=0, validators=[MinValueValidator(0), MaxValueValidator(10)] )
    renome = models.CharField(max_length=100, verbose_name='Renome', blank=True, null=True) 
    custo = models.CharField(max_length=300, verbose_name='Custo', blank=True, null=True)
    rolagem = models.CharField(max_length=300, verbose_name='Rolagem', blank=True, null=True)
    acao = models.CharField(max_length=300, verbose_name='Ação', blank=True, null=True)
    sistema = models.TextField(verbose_name='Sistema', blank=True, null=True)
    duracao = models.CharField(max_length=200, verbose_name='Duração', blank=True, null=True)
    nota = models.TextField(verbose_name='Nota', blank=True, null=True)   
    created_at = models.DateTimeField(auto_now_add=True)
    last_updated = models.DateTimeField(auto_now=True)
    created_by = models.ForeignKey(User, on_delete=models.PROTECT, verbose_name='Criado por')
    
    class Meta:
        verbose_name = 'Dom'
        verbose_name_plural = 'Dons'
        ordering = ['nome']

    def __str__(self):
        
        return self.nome
    
    
class Ritual(models.Model):
    nome = models.CharField(max_length=100, verbose_name='Nome', blank=False, null=False)
    descricao = models.TextField(verbose_name='Descricao', blank=True, null=True)
    rolagem = models.CharField(max_length=300, verbose_name='Rolagem', blank=True, null=True)
    sistema = models.TextField(verbose_name='Sistema', blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    last_updated = models.DateTimeField(auto_now=True)
    created_by = models.ForeignKey(User, on_delete=models.PROTECT, verbose_name='Criado por')
    
    class Meta:
        verbose_name = 'Ritual'
        verbose_name_plural = 'Rituais'
        ordering = ['nome']

    def __str__(self):
        
        return self.nome
    

class Lobisomem(Personagem):
    caern = models.CharField(max_length=200, blank=True, null=True)
   
    gloria =  models.IntegerField(verbose_name='glória', blank=True, null=True, default=0, validators=[MinValueValidator(0), MaxValueValidator(10)] )
    honra =  models.IntegerField(verbose_name='honra', blank=True, null=True, default=0, validators=[MinValueValidator(0), MaxValueValidator(10)] )
    sabedoria =  models.IntegerField(verbose_name='sabedoria', blank=True, null=True, default=0, validators=[MinValueValidator(0), MaxValueValidator(10)] )
    furia =  models.IntegerField(verbose_name='fúria', blank=True, null=True, default=0, validators=[MinValueValidator(0), MaxValueValidator(10)] )
    
      
    tribo = models.ForeignKey(Tribo, on_delete=models.PROTECT, verbose_name='tribo', related_name='lobisomem_tribo', blank=True, null=True)
    patrono = models.ForeignKey(Patrono, on_delete=models.PROTECT, verbose_name='patrono', related_name='lobisomem_patrono', blank=True, null=True)
    augurio = models.ForeignKey(Augurio, on_delete=models.PROTECT, verbose_name='augúrio', related_name='lobisomem_augurio', blank=True, null=True)
    dons = models.ManyToManyField( Dom, blank=True, verbose_name='Dons', related_name='dons_lobisomem')
    rituais = models.ManyToManyField( Ritual, blank=True, verbose_name='Rituais', related_name='rituais_lobisomem')        
    harano = models.IntegerField(verbose_name='harano', blank=True, null=True, default=0, validators=[MinValueValidator(0), MaxValueValidator(5)] )
    hauglosk = models.IntegerField(verbose_name='hauglosk', blank=True, null=True, default=0, validators=[MinValueValidator(0), MaxValueValidator(5)] )
    created_at = models.DateTimeField(auto_now_add=True)
    last_updated = models.DateTimeField(auto_now=True)
    created_by = models.ForeignKey(User, on_delete=models.PROTECT, verbose_name='Criado por')
    
    class Meta:
        verbose_name = 'Lobisomem'
        verbose_name_plural = 'Lobisomens'
        ordering = ['nome']
    
    def __str__(self):
        return self.nome
    
class Formas(Personagem):
    nome = models.CharField(verbose_name='nome', max_length=200, blank=True, null=True)
    custo = models.CharField(verbose_name='custo', max_length=200, blank=True, null=True)
    bonus_fisico = models.CharField(verbose_name='bonus_fisico', max_length=200, blank=True, null=True)
    bonus_sociais = models.CharField(verbose_name='bonus_sociais', max_length=200, blank=True, null=True)
    furtividade = models.CharField(verbose_name='furtividade', max_length=200, blank=True, null=True)
    regeneracao = models.CharField(verbose_name='regeneração', max_length=200, blank=True, null=True)
    nivel_vitalidade = models.CharField(verbose_name='nivel_vitalidade', max_length=200, blank=True, null=True)
    garras = models.CharField(verbose_name='garras', max_length=200, blank=True, null=True)
    mordida = models.CharField(verbose_name='mordida', max_length=200, blank=True, null=True)
    delirio = models.CharField(verbose_name='delirio', max_length=200, blank=True, null=True)
    prata = models.CharField(verbose_name='prata', max_length=200, blank=True, null=True)
    
    created_at = models.DateTimeField(auto_now_add=True)
    last_updated = models.DateTimeField(auto_now=True)
    created_by = models.ForeignKey(User, on_delete=models.PROTECT, verbose_name='Criado por')
   
    class Meta:
        verbose_name = 'Forma'
        verbose_name_plural = 'Formas'
        ordering = ['nome']
    
    def __str__(self):
        return self.nome


class Nota(models.Model):
    nome = models.CharField(max_length=200, verbose_name='Nome', blank=False, null=False)
    lobisomem = models.ForeignKey(Lobisomem, on_delete=models.PROTECT, verbose_name='lobisomem', related_name='lobisomem_notas')
    descricao = models.TextField(verbose_name='Descrição', blank=True, null=True) 
    pontuacao = models.IntegerField( blank=True, null=True, default=0, validators=[MinValueValidator(0), MaxValueValidator(5)] )
    created_at = models.DateTimeField(auto_now_add=True)
    last_updated = models.DateTimeField(auto_now=True)
    created_by = models.ForeignKey(User, on_delete=models.PROTECT, related_name='lobisomem_notas',verbose_name='Criado por')
    
    class Meta:
        verbose_name = 'Nota'
        verbose_name_plural = 'Notas'
        ordering = ['nome']

    def __str__(self):
        if self.pontuacao:
            return "{} - {}".format(self.nome, self.pontuacao)        
        return self.nome  

    
    