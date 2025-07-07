from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from django.contrib.auth.models import User
from npc.models import Npc
from vampiro.models import Vampiro



class Cidade(models.Model):
    nome = models.CharField(max_length=200, unique=True, blank=False, null=False)
    idade = models.IntegerField( verbose_name='idade', blank=True, null=True )
    pais = models.CharField( verbose_name='país', max_length=200, blank=False, null=False)
    estado = models.CharField(verbose_name='estado', max_length=200, blank=False, null=False)
    origem_nome = models.TextField(verbose_name='origem do nome', blank=False, null=False)
    historia = models.TextField(verbose_name='história', blank=True, null=True)
    historia_sobrenatural = models.TextField(verbose_name='história sobrenatural', blank=True, null=True)
    populacao = models.IntegerField( verbose_name='população', blank=True, null=True )
    populacao_sobrenatural = models.IntegerField( verbose_name='população sobrenatural', blank=True, null=True )    
    eventos = models.TextField(verbose_name='eventos', blank=True, null=True)
    eventos_sobrenaturais = models.TextField(verbose_name='eventos sobrenaturais', blank=True, null=True)
    clima = models.TextField(verbose_name='clima', max_length=400, blank=False, null=False)
    atmosfera = models.TextField(verbose_name='atmosfera', max_length=400, blank=False, null=False)
    arquitetura= models.TextField(verbose_name='arquitetura', max_length=400, blank=False, null=False)
    economia = models.TextField(verbose_name='economia', blank=False, null=False)
    religiao = models.TextField(verbose_name='religiao', blank=False, null=False)
    religiao_sobrenatural = models.TextField(verbose_name='religiao sobrenatural',  blank=False, null=False)
    mobilidade = models.TextField(verbose_name='mobilidade',blank=False, null=False)
    ruas_principais = models.TextField(verbose_name='ruas principais',blank=False, null=False)
    
    cidades_relacionadas = models.ManyToManyField( 'self', verbose_name='cidades relacionadas', blank=True)
    
    locais_proibidos = models.TextField(verbose_name='locais proibidos',blank=False, null=False)
    bairros_elegantes = models.TextField(verbose_name='bairros elegantes',blank=False, null=False)
    bairros_decadentes = models.TextField(verbose_name='bairros decadentes',blank=False, null=False)
    centros_comerciais = models.TextField(verbose_name='centros comerciais',blank=False, null=False)
    centros_culturais = models.TextField(verbose_name='centros culturais',blank=False, null=False)
    zonas_perifericas = models.TextField(verbose_name='zonas periféricas',blank=False, null=False)
    zonas_rurais = models.TextField(verbose_name='zonas rurais',blank=False, null=False)
    prefeito = models.CharField(max_length=200, verbose_name='prefeito', blank=True, null=True)
    controle_prefeito = models.TextField( verbose_name='controle prefeito', blank=True, null=True)
    detalhes_prefeitura = models.TextField(verbose_name='detalhes prefeitura',blank=False, null=False)
    orgaos_publicos = models.TextField(verbose_name='orgaos publicos',blank=False, null=False)
    delegacias = models.TextField(verbose_name='delegacias',blank=False, null=False)
    policiais = models.TextField(verbose_name='policiais',blank=False, null=False)
    detalhes_policiais = models.TextField(verbose_name='detalhes policiais',blank=False, null=False)
    esgotos = models.TextField(verbose_name='esgotos',blank=False, null=False)
    detalhes_esgotos = models.TextField(verbose_name='detalhes esgotos',blank=False, null=False)
    hospitais = models.TextField(verbose_name='hospitais',blank=False, null=False)
    detalhes_hospitais = models.TextField(verbose_name='detalhes hospitais',blank=False, null=False)
    bibliotecas = models.TextField(verbose_name='bibliotecas',blank=False, null=False)
    detalhes_bibliotecas = models.TextField(verbose_name='detalhes bibliotecas',blank=False, null=False)
    parques = models.TextField(verbose_name='parques',blank=False, null=False)
    detalhes_parques = models.TextField(verbose_name='detalhes parques',blank=False, null=False)
    museus = models.TextField(verbose_name='museus',blank=False, null=False)
    detalhes_museus = models.TextField(verbose_name='detalhes museus',blank=False, null=False)
    midias = models.TextField(verbose_name='midias',blank=False, null=False)
    detalhes_midias = models.TextField(verbose_name='detalhes midias',blank=False, null=False)
    aeroporto = models.TextField(verbose_name='aeroporto',blank=False, null=False)
    empresas = models.TextField(verbose_name='empresas',blank=False, null=False)
    detalhes_empresas = models.TextField(verbose_name='detalhes empresas',blank=False, null=False)
    locais_importantes = models.TextField(verbose_name='locais importantes',blank=False, null=False)
    abrigos = models.TextField(verbose_name='abrigos',blank=False, null=False)
    universidades = models.TextField(verbose_name='universidades',blank=False, null=False)
    gangues = models.TextField(verbose_name='gangues',blank=False, null=False)
    vida_noturna = models.TextField(verbose_name='vida noturna',blank=False, null=False)
    descricao_cortes = models.TextField(verbose_name='descricao cortes',blank=False, null=False)
    senescal = models.TextField(verbose_name='senescal',blank=False, null=False)
    primigenie = models.TextField(verbose_name='primigênie',blank=False, null=False)
    secretarios_clas = models.TextField(verbose_name='secretários clãs',blank=False, null=False)
    xerifes = models.TextField(verbose_name='xerifes',blank=False, null=False)
    arauto = models.TextField(verbose_name='arauto',blank=False, null=False)
    elisios = models.TextField(verbose_name='elisíos',blank=False, null=False)
   
    npcs = models.ManyToManyField(Npc, verbose_name='Npcs', related_name='cidade_npcs', blank=True)
    vampiros = models.ManyToManyField(Vampiro, verbose_name='Vampiros', related_name='cidade_vampiros', blank=True) 
    created_at = models.DateTimeField(auto_now_add=True)
    last_updated = models.DateTimeField(auto_now=True)
    created_by = models.ForeignKey(User, on_delete=models.PROTECT, verbose_name='Criado por')
    
    class Meta:
        verbose_name = 'Cidade'
        verbose_name_plural = 'Cidades'
        ordering = ['nome']
    
    def __str__(self):
        return self.nome


class Nota(models.Model):
    nome = models.CharField(max_length=200, verbose_name='Nome', blank=False, null=False)
    cidade = models.ForeignKey(Cidade, on_delete=models.PROTECT, verbose_name='Cidade', related_name='cidade_notas')
    descricao = models.TextField(verbose_name='Descricao', blank=True, null=True) 
    pontuacao = models.IntegerField( blank=True, null=True, default=0, validators=[MinValueValidator(0), MaxValueValidator(5)] )
    created_at = models.DateTimeField(auto_now_add=True)
    last_updated = models.DateTimeField(auto_now=True)
    created_by = models.ForeignKey(User, on_delete=models.PROTECT, related_name='cidades_nota',verbose_name='Criado por')
    
    class Meta:
        verbose_name = 'Nota'
        verbose_name_plural = 'Notas'
        ordering = ['nome']

    def __str__(self):        
        return self.nome  

    
    