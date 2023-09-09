from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator
from django.urls import reverse
from django.utils.text import slugify
from django.contrib.auth.models import User


class Personagem(models.Model):
    nomePerfil = models.ForeignKey(User, on_delete=models.CASCADE)
    nome = models.CharField(max_length=100)
    vida = models.IntegerField(null=True)
    
    

    class Meta:
        abstract = True
        unique_together = ('nome',)

class DnD(Personagem):
    #Dados Iniciais
    classe = models.CharField(max_length=100)
    sub_classe = models.CharField(max_length=100, blank=True, null=True)
    nivel = models.IntegerField(validators=[MinValueValidator(1)])
    raca = models.CharField(max_length=100, null=True)
    sub_raca = models.CharField(max_length=100, blank=True, null=True)
    xp = models.IntegerField(validators=[MinValueValidator(0)], blank=True, null=True)

    #Atributos
    forca = models.IntegerField(default=0)
    dex = models.IntegerField(default=0)
    const = models.IntegerField(default=0)
    int = models.IntegerField(default=0)
    sab = models.IntegerField(default=0)
    carisma = models.IntegerField(default=0)

    inspiracao = models.BooleanField(default=False)

    #Saving Throws
    forcaSalvaguarda = models.BooleanField(default=False)
    dexSalvaguarda = models.BooleanField(default=False)
    constSalvaguarda = models.BooleanField(default=False)
    intSalvaguarda = models.BooleanField(default=False)
    sabSalvaguarda = models.BooleanField(default=False)
    carismaSalvaguarda = models.BooleanField(default=False)

    #Pericias
    acrobacia = models.BooleanField(default=False)
    adestrarAnimais = models.BooleanField(default=False)
    arcana = models.BooleanField(default=False)
    atletismo = models.BooleanField(default=False)
    enganacao = models.BooleanField(default=False)
    historia = models.BooleanField(default=False)
    intuicao = models.BooleanField(default=False)
    intimidacao = models.BooleanField(default=False)
    investigacao = models.BooleanField(default=False)
    medicina = models.BooleanField(default=False)
    natureza = models.BooleanField(default=False)
    percepcao = models.BooleanField(default=False)
    atuacao = models.BooleanField(default=False)
    persuasao = models.BooleanField(default=False)
    religiao = models.BooleanField(default=False)
    prestigitacao = models.BooleanField(default=False)
    furtividade = models.BooleanField(default=False)
    sobrevivencia = models.BooleanField(default=False)


    proficienciasFerramentas = models.TextField(null=True, blank=True)
    outrasProf_Linguagens = models.TextField(null=True, blank=True)

    #Coluna do meio
    ca = models.IntegerField(default=0)
    movi = models.FloatField(blank=True, null=True)
    vidaTemp = models.IntegerField(null=True, blank=True)
    hitDice = models.IntegerField(null=True, blank=True)
    hitDiceType_Options = [
        ('d4', 'd4'),
        ('d6', 'd6'),
        ('d8', 'd8'),
        ('d10', 'd10'),
        ('d12', 'd12'),
    ]
    hitDiceType = models.CharField(max_length=4, choices=hitDiceType_Options, default='d4')

    deathSucess1 = models.BooleanField(default=False)
    deathSucess2 = models.BooleanField(default=False)
    deathSucess3 = models.BooleanField(default=False)

    deathFailure1 = models.BooleanField(default=False)
    deathFailure2 = models.BooleanField(default=False)
    deathFailure3 = models.BooleanField(default=False)


    #Ataques
    nomeAtk1 = models.CharField(max_length=100, blank=True, null=True)
    bonusAtk1 = models.IntegerField(default=0, blank=True, null=True)
    danoTipoAtk1 = models.CharField(max_length=100, blank=True, null=True)

    nomeAtk2 = models.CharField(max_length=100, blank=True, null=True)
    bonusAtk2 = models.IntegerField(default=0, blank=True, null=True)
    danoTipoAtk2 = models.CharField(max_length=100, blank=True, null=True)

    nomeAtk3 = models.CharField(max_length=100, blank=True, null=True)
    bonusAtk3 = models.IntegerField(default=0, blank=True, null=True)
    danoTipoAtk3 = models.CharField(max_length=100, blank=True, null=True)

    nomeAtk4 = models.CharField(max_length=100, blank=True, null=True)
    bonusAtk4 = models.IntegerField(default=0, blank=True, null=True)
    danoTipoAtk4 = models.CharField(max_length=100, blank=True, null=True)

    nomeAtk5 = models.CharField(max_length=100, blank=True, null=True)
    bonusAtk5 = models.IntegerField(default=0, blank=True, null=True)
    danoTipoAtk5 = models.CharField(max_length=100, blank=True, null=True)


    #Dinheiro
    pc = models.IntegerField(default=0)
    pp = models.IntegerField(default=0)
    pe = models.IntegerField(default=0)
    po = models.IntegerField(default=0)
    pl = models.IntegerField(default=0)


    #inventario
    inventario = models.TextField(null=True, blank=True)

    



    #Caracteristicas
    personalidade = models.CharField(null=True, blank=True, max_length=350)
    ideias = models.CharField(null=True, blank=True, max_length=350)
    vinculos = models.CharField(null=True, blank=True, max_length=350)
    fraquezas = models.CharField(null=True, blank=True, max_length=350)

    #Características e Talentos
    caracteristicas = models.TextField(null=True, blank=True)





class OrdemParanormal(Personagem):

    #Atributos
    agi = models.IntegerField(default=0)
    inte = models.IntegerField(default=0)
    vig = models.IntegerField(default=0)
    pre = models.IntegerField(default=0)
    forc = models.IntegerField(default=0)
    
    #Outros dados
    origem = models.CharField(max_length=100)

    classesOptions = [
            ('Combatente', 'Combatente'),
            ('Especialista', 'Especialista'),
            ('Ocultista', 'Ocultista'),
    ]
    classe = models.CharField(max_length=20, choices=classesOptions, default='Combatente')

    nex = models.IntegerField(validators=[MaxValueValidator(99), MinValueValidator(0)])
    peRodada = models.IntegerField(default=0)
    deslocamento = models.FloatField(default=0)

    pe = models.IntegerField(default=0)


    equipBonus = models.IntegerField(default=0)
    defOutrosBonus = models.IntegerField(default=0)

    sanidade = models.IntegerField(default=0)

    protecao = models.CharField(max_length=250, blank=True, null=True)
    resistencias = models.CharField(max_length=250, blank=True, null=True)


    #Pericias
    periciasNivel = [
            ('Leigo', 'Leigo'),
            ('Treinado', 'Treinado'),
            ('Veterano', 'Veterano'),
            ('Especialista', 'Especialista'),
    ]

    acrobacia = models.CharField(max_length=20, choices=periciasNivel, default='Leigo')
    acrobaciaOutros = models.IntegerField(default=0)

    adestramento = models.CharField(max_length=20, choices=periciasNivel, default='Leigo')
    adestramentoOutros = models.IntegerField(default=0)

    artes = models.CharField(max_length=20, choices=periciasNivel, default='Leigo')
    artesOutros = models.IntegerField(default=0)

    atletismo = models.CharField(max_length=20, choices=periciasNivel, default='Leigo')
    atletismoOutros = models.IntegerField(default=0)

    atualidades = models.CharField(max_length=20, choices=periciasNivel, default='Leigo')
    atualidadesOutros = models.IntegerField(default=0)

    ciencias = models.CharField(max_length=20, choices=periciasNivel, default='Leigo')
    cienciasOutros = models.IntegerField(default=0)

    crime = models.CharField(max_length=20, choices=periciasNivel, default='Leigo')
    crimeOutros = models.IntegerField(default=0)

    diplomacia = models.CharField(max_length=20, choices=periciasNivel, default='Leigo')
    diplomaciaOutros = models.IntegerField(default=0)

    enganacao = models.CharField(max_length=20, choices=periciasNivel, default='Leigo')
    enganacaoOutros = models.IntegerField(default=0)

    fortitude = models.CharField(max_length=20, choices=periciasNivel, default='Leigo')
    fortitudeOutros = models.IntegerField(default=0)

    furtividade = models.CharField(max_length=20, choices=periciasNivel, default='Leigo')
    furtividadeOutros = models.IntegerField(default=0)

    iniciativa = models.CharField(max_length=20, choices=periciasNivel, default='Leigo')
    iniciativaOutros = models.IntegerField(default=0)

    intimidacao = models.CharField(max_length=20, choices=periciasNivel, default='Leigo')
    intimidacaoOutros = models.IntegerField(default=0)

    intuicao = models.CharField(max_length=20, choices=periciasNivel, default='Leigo')
    intuicaoOutros = models.IntegerField(default=0)

    investigacao = models.CharField(max_length=20, choices=periciasNivel, default='Leigo')
    investigacaoOutros = models.IntegerField(default=0)

    luta = models.CharField(max_length=20, choices=periciasNivel, default='Leigo')
    lutaOutros = models.IntegerField(default=0)

    medicina = models.CharField(max_length=20, choices=periciasNivel, default='Leigo')
    medicinaOutros = models.IntegerField(default=0)

    ocultismo = models.CharField(max_length=20, choices=periciasNivel, default='Leigo')
    ocultismoOutros = models.IntegerField(default=0)

    percepcao = models.CharField(max_length=20, choices=periciasNivel, default='Leigo')
    percepcaoOutros = models.IntegerField(default=0)

    pilotagem = models.CharField(max_length=20, choices=periciasNivel, default='Leigo')
    pilotagemOutros = models.IntegerField(default=0)

    pontaria = models.CharField(max_length=20, choices=periciasNivel, default='Leigo')
    pontariaOutros = models.IntegerField(default=0)

    profissao = models.CharField(max_length=20, choices=periciasNivel, default='Leigo')
    profissaoOutros = models.IntegerField(default=0)

    reflexos = models.CharField(max_length=20, choices=periciasNivel, default='Leigo')
    reflexosOutros = models.IntegerField(default=0)

    religiao = models.CharField(max_length=20, choices=periciasNivel, default='Leigo')
    religiaoOutros = models.IntegerField(default=0)

    sobrevivencia = models.CharField(max_length=20, choices=periciasNivel, default='Leigo')
    sobrevivenciaOutros = models.IntegerField(default=0)

    tatica = models.CharField(max_length=20, choices=periciasNivel, default='Leigo')
    taticaOutros = models.IntegerField(default=0)

    tecnologia = models.CharField(max_length=20, choices=periciasNivel, default='Leigo')
    tecnologiaOutros = models.IntegerField(default=0)

    vontade = models.CharField(max_length=20, choices=periciasNivel, default='Leigo')
    vontadeOutros = models.IntegerField(default=0)

   #Ataques
    ataqueNome1 = models.CharField(max_length=150, blank=True, null=True)
    tipo1 = models.CharField(max_length=50, blank=True, null=True)
    teste1 = models.CharField(max_length=50, blank=True, null=True)
    dano1 = models.CharField(max_length=50, blank=True, null=True)
    critico1 = models.CharField(max_length=50, blank=True, null=True)
    alcance1 = models.CharField(max_length=100, blank=True, null=True)
    especial1 = models.CharField(max_length=50, blank=True, null=True)

    ataqueNome2 = models.CharField(max_length=150, blank=True, null=True)
    tipo2 = models.CharField(max_length=50, blank=True, null=True)
    teste2 = models.CharField(max_length=50, blank=True, null=True)
    dano2 = models.CharField(max_length=50, blank=True, null=True)
    critico2 = models.CharField(max_length=50, blank=True, null=True)
    alcance2 = models.CharField(max_length=100, blank=True, null=True)
    especial2 = models.CharField(max_length=50, blank=True, null=True)

    ataqueNome3 = models.CharField(max_length=150, blank=True, null=True)
    tipo3 = models.CharField(max_length=50, blank=True, null=True)
    teste3 = models.CharField(max_length=50, blank=True, null=True)
    dano3 = models.CharField(max_length=50, blank=True, null=True)
    critico3 = models.CharField(max_length=50, blank=True, null=True)
    alcance3 = models.CharField(max_length=100, blank=True, null=True)
    especial3 = models.CharField(max_length=50, blank=True, null=True)

    ataqueNome4 = models.CharField(max_length=150, blank=True, null=True)
    tipo4 = models.CharField(max_length=50, blank=True, null=True)
    teste4 = models.CharField(max_length=50, blank=True, null=True)
    dano4 = models.CharField(max_length=50, blank=True, null=True)
    critico4 = models.CharField(max_length=50, blank=True, null=True)
    alcance4 = models.CharField(max_length=100, blank=True, null=True)
    especial4 = models.CharField(max_length=50, blank=True, null=True)

    ataqueNome5 = models.CharField(max_length=150, blank=True, null=True)
    tipo5 = models.CharField(max_length=50, blank=True, null=True)
    teste5 = models.CharField(max_length=50, blank=True, null=True)
    dano5 = models.CharField(max_length=50, blank=True, null=True)
    critico5 = models.CharField(max_length=50, blank=True, null=True)
    alcance5 = models.CharField(max_length=100, blank=True, null=True)
    especial5 = models.CharField(max_length=50, blank=True, null=True)

    ataqueNome6 = models.CharField(max_length=150, blank=True, null=True)
    tipo6 = models.CharField(max_length=50, blank=True, null=True)
    teste6 = models.CharField(max_length=50, blank=True, null=True)
    dano6 = models.CharField(max_length=50, blank=True, null=True)
    critico6 = models.CharField(max_length=50, blank=True, null=True)
    alcance6 = models.CharField(max_length=100, blank=True, null=True)
    especial6 = models.CharField(max_length=50, blank=True, null=True)


    #Habilidades e rituais
    dt = models.IntegerField(default=0)
    habilidades = models.TextField(null=True, blank=True)


    #Inventário
    pp = models.IntegerField(default=0)
    patente = models.CharField(max_length=100, null=True, blank=True)
    #Limite de itens
    carga1 = models.BooleanField(default=False)
    carga2 = models.BooleanField(default=False)
    carga3 = models.BooleanField(default=False)
    carga4 = models.BooleanField(default=False)

    limiteCredito = models.CharField(max_length=50, null=True, blank=True)

    cargaAtual = models.IntegerField(default=0)
    cargaMax = models.IntegerField(default=0)


    itens = models.TextField(null=True, blank=True)


    #Descrição
    aparencia = models.CharField(max_length=500, null=True, blank=True)
    personalidade = models.CharField(max_length=500, null=True, blank=True)
    historico = models.CharField(max_length=500, null=True, blank=True)
    objetivo = models.CharField(max_length=500, null=True, blank=True)
