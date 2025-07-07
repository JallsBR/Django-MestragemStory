from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from django.contrib.auth.models import User
from antecedentes.models import Vantagem

class Personagem(models.Model):
    jogador = models.CharField(max_length=200, verbose_name='Jogador', blank=True, null=True)
    nome = models.CharField(max_length=200, unique=True, blank=False, null=False)
    conceito = models.CharField(max_length=200,  blank=True, null=True)    
    ambicao = models.CharField(max_length=200, verbose_name='ambição', blank=True, null=True)   
    desejo = models.CharField(max_length=200, blank=True, null=True)
    pilares = models.TextField(verbose_name='pilares', blank=True, null=True)
    
    idade_aparente = models.IntegerField( verbose_name='idade aparente', blank=True, null=True )
    idade_verdadeira = models.IntegerField( verbose_name='idade verdadeira', blank=True, null=True )
    data_nascimento = models.DateField( verbose_name='data de nascimento', blank=True, null=True )
    aparencia = models.TextField(verbose_name='aparência', blank=True, null=True)
    historia = models.TextField(verbose_name='história', blank=True, null=True)  
    equipamento = models.TextField(verbose_name='equipamento', blank=True, null=True)  
      
    forca = models.IntegerField( verbose_name='força', blank=True, null=True, default=0, validators=[MinValueValidator(0), MaxValueValidator(10)] )
    destreza =  models.IntegerField(blank=True, null=True, default=0, validators=[MinValueValidator(0), MaxValueValidator(10)] )
    vigor =  models.IntegerField( blank=True, null=True,  validators=[MinValueValidator(1), MaxValueValidator(5)] )
    
    carisma = models.IntegerField( blank=True, null=True, default=0, validators=[MinValueValidator(0), MaxValueValidator(5)] )
    manipulacao =  models.IntegerField( verbose_name='manipulação', blank=True, null=True, default=0, validators=[MinValueValidator(0), MaxValueValidator(10)] )
    autocontrole =  models.IntegerField( blank=True, null=True, default=0, validators=[MinValueValidator(0), MaxValueValidator(5)] )
    
    inteligencia =  models.IntegerField( verbose_name='inteligência', blank=True, null=True, default=0, validators=[MinValueValidator(0), MaxValueValidator(10)] )
    raciocinio =  models.IntegerField( verbose_name='raciocínio', blank=True, null=True, default=0, validators=[MinValueValidator(0), MaxValueValidator(5)] )
    determinacao =  models.IntegerField( verbose_name='determinação', blank=True, null=True, default=0, validators=[MinValueValidator(0), MaxValueValidator(10)] )
    
    
    arma_branca =  models.IntegerField( verbose_name='armas brancas', blank=True, null=True, default=0, validators=[MinValueValidator(0), MaxValueValidator(10)] )
    armas_de_fogo =  models.IntegerField( verbose_name='armas de fogo', blank=True, null=True, default=0, validators=[MinValueValidator(0), MaxValueValidator(10)] )
    atletismo =  models.IntegerField( blank=True, null=True, default=0, validators=[MinValueValidator(0), MaxValueValidator(10)] )
    briga =  models.IntegerField( blank=True, null=True, default=0, validators=[MinValueValidator(0), MaxValueValidator(10)] )
    conducao =  models.IntegerField( verbose_name='condução', blank=True, null=True, default=0, validators=[MinValueValidator(0), MaxValueValidator(10)] )
    furtividade =  models.IntegerField( blank=True, null=True, default=0, validators=[MinValueValidator(0), MaxValueValidator(10)] )
    ladroagem =  models.IntegerField( blank=True, null=True, default=0, validators=[MinValueValidator(0), MaxValueValidator(10)] )
    oficios =  models.IntegerField( verbose_name='ofícios', blank=True, null=True, default=0, validators=[MinValueValidator(0), MaxValueValidator(10)] )
    sobrevivencia =  models.IntegerField( blank=True, null=True, default=0, validators=[MinValueValidator(0), MaxValueValidator(5)] )
    
    empatia_com_animais =  models.IntegerField( verbose_name='empatia com animais', blank=True, null=True, default=0, validators=[MinValueValidator(0), MaxValueValidator(10)] )
    etiqueta =  models.IntegerField( blank=True, null=True, default=0, validators=[MinValueValidator(0), MaxValueValidator(5)] )
    intimidacao =  models.IntegerField( verbose_name='intimidação' ,blank=True, null=True, default=0, validators=[MinValueValidator(0), MaxValueValidator(10)] )
    lideranca =  models.IntegerField( blank=True, null=True, default=0, validators=[MinValueValidator(0), MaxValueValidator(10)] )
    manha =  models.IntegerField( blank=True, null=True, default=0, validators=[MinValueValidator(0), MaxValueValidator(10)] )
    performance =  models.IntegerField( blank=True, null=True, default=0, validators=[MinValueValidator(0), MaxValueValidator(5)] )
    persuasao =  models.IntegerField( verbose_name='persuasão', blank=True, null=True, default=0, validators=[MinValueValidator(0), MaxValueValidator(10)] )
    sagacidade =  models.IntegerField( blank=True, null=True, default=0, validators=[MinValueValidator(0), MaxValueValidator(5)] )
    subterfugio =  models.IntegerField( verbose_name= 'subterfúgio', blank=True, null=True, default=0, validators=[MinValueValidator(0), MaxValueValidator(10)] )
    
    ciencia =  models.IntegerField( verbose_name='ciência', blank=True, null=True, default=0, validators=[MinValueValidator(0), MaxValueValidator(10)] )
    erudicao =  models.IntegerField( verbose_name= 'erudição', blank=True, null=True, default=0, validators=[MinValueValidator(0), MaxValueValidator(10)] )
    financas =  models.IntegerField( blank=True, null=True, default=0, validators=[MinValueValidator(0), MaxValueValidator(5)] )
    investigacao =  models.IntegerField(verbose_name= 'investigação', blank=True, null=True, default=0, validators=[MinValueValidator(0), MaxValueValidator(10)] )
    medicina =  models.IntegerField( blank=True, null=True, default=0, validators=[MinValueValidator(0), MaxValueValidator(10)] )
    ocultismo =  models.IntegerField( blank=True, null=True, default=0, validators=[MinValueValidator(0), MaxValueValidator(5)] )
    percepcao =  models.IntegerField(verbose_name= 'percepção', blank=True, null=True, default=0, validators=[MinValueValidator(0), MaxValueValidator(10)] )
    politica =  models.IntegerField( verbose_name='política', blank=True, null=True, default=0, validators=[MinValueValidator(0), MaxValueValidator(10)] )
    tecnologia =  models.IntegerField( blank=True, null=True, default=0, validators=[MinValueValidator(0), MaxValueValidator(10)] )   
 
    vitalidade_maxima =  models.IntegerField( verbose_name= 'vitalidade máxima', blank=True, null=True, default=0, validators=[MinValueValidator(0), MaxValueValidator(20)] )
    vitalidade_atual =  models.IntegerField( verbose_name= 'vitalidade atual', blank=True, null=True, default=0, validators=[MinValueValidator(0), MaxValueValidator(20)] )
    vitalidade_agravada =  models.IntegerField( verbose_name= 'vitalidade agravada', blank=True, null=True, default=0, validators=[MinValueValidator(0), MaxValueValidator(20)] )
    
    vontade_maxima =  models.IntegerField( verbose_name= 'vontade máxima', blank=True, null=True, default=0, validators=[MinValueValidator(0), MaxValueValidator(20)] )
    vontade_atual =  models.IntegerField( verbose_name= 'vontade atual', blank=True, null=True, default=0, validators=[MinValueValidator(0), MaxValueValidator(20)] )
    vontade_agravada =  models.IntegerField( verbose_name= 'vontade agravada', blank=True, null=True, default=0, validators=[MinValueValidator(0), MaxValueValidator(20)] )
    
    vantagens = models.ManyToManyField(Vantagem, blank=True, related_name='+', verbose_name='Vantagens')

   
    experiencia =  models.IntegerField( verbose_name= 'experiência', blank=True, null=True, default=0 )
    experiencia_gasta =  models.IntegerField( verbose_name= 'experiência gasta', blank=True, null=True, default=0 )        

    created_at = models.DateTimeField(auto_now_add=True)
    last_updated = models.DateTimeField(auto_now=True)
    created_by = models.ForeignKey(User, on_delete=models.PROTECT, verbose_name='Criado por')
    
    
    
    class Meta:
        abstract = True       
    
    def __str__(self):
        return self.nome