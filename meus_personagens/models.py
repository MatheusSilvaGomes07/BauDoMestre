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





class Tormenta(Personagem):
    raca = models.CharField(max_length=100)
    origem = models.CharField(max_length=100, null=True, blank=True)
    classe = models.CharField(max_length=100)
    nivel = models.IntegerField(default=1)
    divindade = models.CharField(max_length=50)

    #Atributos
    forca = models.IntegerField(default=0)
    des = models.IntegerField(default=0)
    const = models.IntegerField(default=0)
    inteli = models.IntegerField(default=0)
    sab = models.IntegerField(default=0)
    car = models.IntegerField(default=0)

    pvMax = models.IntegerField(default=0)
    pvAtual = models.IntegerField(default=0)

    manaMax = models.IntegerField(default=0)
    manaAtual = models.IntegerField(default=0)

    #Ataques
    atkNome1 = models.CharField(max_length=100, null=True, blank=True)
    atkBonus1 = models.CharField(max_length=100, null=True, blank=True)
    atkDano1 = models.CharField(max_length=100, null=True, blank=True)
    atkDanoExtra1 = models.CharField(max_length=100, null=True, blank=True)
    dadoCrit1 = models.IntegerField(default=20)
    multiplicadorCrit1 = models.IntegerField(default=2)
    alcance1 = models.CharField(max_length=20, null=True, blank=True)

    atkNome2 = models.CharField(max_length=100, null=True, blank=True)
    atkBonus2 = models.CharField(max_length=100, null=True, blank=True)
    atkDano2 = models.CharField(max_length=100, null=True, blank=True)
    atkDanoExtra2 = models.CharField(max_length=100, null=True, blank=True)
    dadoCrit2 = models.IntegerField(default=20)
    multiplicadorCrit2 = models.IntegerField(default=2)
    alcance2 = models.CharField(max_length=20, null=True, blank=True)

    atkNome3 = models.CharField(max_length=100, null=True, blank=True)
    atkBonus3 = models.CharField(max_length=100, null=True, blank=True)
    atkDano3 = models.CharField(max_length=100, null=True, blank=True)
    atkDanoExtra3 = models.CharField(max_length=100, null=True, blank=True)
    dadoCrit3 = models.IntegerField(default=20)
    multiplicadorCrit3 = models.IntegerField(default=2)
    alcance3 = models.CharField(max_length=20, null=True, blank=True)

    atkNome4 = models.CharField(max_length=100, null=True, blank=True)
    atkBonus4 = models.CharField(max_length=100, null=True, blank=True)
    atkDano4 = models.CharField(max_length=100, null=True, blank=True)
    atkDanoExtra4 = models.CharField(max_length=100, null=True, blank=True)
    dadoCrit4 = models.IntegerField(default=20)
    multiplicadorCrit4 = models.IntegerField(default=2)
    alcance4 = models.CharField(max_length=20, null=True, blank=True)

    atkNome5 = models.CharField(max_length=100, null=True, blank=True)
    atkBonus5 = models.CharField(max_length=100, null=True, blank=True)
    atkDano5 = models.CharField(max_length=100, null=True, blank=True)
    atkDanoExtra5 = models.CharField(max_length=100, null=True, blank=True)
    dadoCrit5 = models.IntegerField(default=20)
    multiplicadorCrit5 = models.IntegerField(default=2)
    alcance5 = models.CharField(max_length=20, null=True, blank=True)


    #Defesa CA (Soma tudo)
    desBonus = models.BooleanField(default=True)
    armaduraBonus = models.IntegerField(default=0)
    escudoBonus = models.IntegerField(default=0)
    outrosBonus = models.IntegerField(default=0)
    
    #Itens de armadura e escudo
    nomeArmadura = models.CharField(max_length=100, null=True, blank=True)
    bonusArmaduraItem = models.IntegerField(default=0)
    penalidadeArmadura = models.IntegerField(default=0)

    nomeEscudo = models.CharField(max_length=100, null=True, blank=True)
    bonusEscudoItem = models.IntegerField(default=0)
    penalidadeEscudo = models.IntegerField(default=0)

    #Proficiencias & Outras Características
    proficiencias = models.TextField(null=True, blank=True)


    #Magias
    magiasCirculo1 = models.TextField(null=True, blank=True)
    magiasCirculo2 = models.TextField(null=True, blank=True)
    magiasCirculo3 = models.TextField(null=True, blank=True)
    magiasCirculo4 = models.TextField(null=True, blank=True)
    magiasCirculo5 = models.TextField(null=True, blank=True)

    #Pericias
    periciasMod = [
            ('For', 'For'),
            ('Des', 'Des'),
            ('Con', 'Con'),
            ('Int', 'Int'),
            ('Sab', 'Sab'),
            ('Car', 'Car'),
    ]

    acrobacia = models.BooleanField(default=False)
    acrobaciaMod = models.CharField(max_length=3, choices=periciasMod, default='Des')
    acrobaciaOutros = models.IntegerField(default=0)

    adestramento = models.BooleanField(default=False)
    adestramentoMod = models.CharField(max_length=3, choices=periciasMod, default='Car')
    adestramentoOutros = models.IntegerField(default=0)

    atletismo = models.BooleanField(default=False)
    atletismoMod = models.CharField(max_length=3, choices=periciasMod, default='For')
    atletismoOutros = models.IntegerField(default=0)

    atuacao = models.BooleanField(default=False)
    atuacaoMod = models.CharField(max_length=3, choices=periciasMod, default='Car')
    atuacaoOutros = models.IntegerField(default=0)

    cavalgar = models.BooleanField(default=False)
    cavalgarMod = models.CharField(max_length=3, choices=periciasMod, default='Des')
    cavalgarOutros = models.IntegerField(default=0)

    conhecimento = models.BooleanField(default=False)
    conhecimentoMod = models.CharField(max_length=3, choices=periciasMod, default='Int')
    conhecimentoOutros = models.IntegerField(default=0)

    cura = models.BooleanField(default=False)
    curaMod = models.CharField(max_length=3, choices=periciasMod, default='Sab')
    curaOutros = models.IntegerField(default=0)

    diplomacia = models.BooleanField(default=False)
    diplomaciaMod = models.CharField(max_length=3, choices=periciasMod, default='Car')
    diplomaciaOutros = models.IntegerField(default=0)

    enganacao = models.BooleanField(default=False)
    enganacaoMod = models.CharField(max_length=3, choices=periciasMod, default='Car')
    enganacaoOutros = models.IntegerField(default=0)

    fortitude = models.BooleanField(default=False)
    fortitudeMod = models.CharField(max_length=3, choices=periciasMod, default='Con')
    fortitudeOutros = models.IntegerField(default=0)

    furtividade = models.BooleanField(default=False)
    furtividadeMod = models.CharField(max_length=3, choices=periciasMod, default='Des')
    furtividadeOutros = models.IntegerField(default=0)

    guerra = models.BooleanField(default=False)
    guerraMod = models.CharField(max_length=3, choices=periciasMod, default='Int')
    guerraOutros = models.IntegerField(default=0)

    iniciativa = models.BooleanField(default=False)
    iniciativaMod = models.CharField(max_length=3, choices=periciasMod, default='Des')
    iniciativaOutros = models.IntegerField(default=0)
    
    intimidacao = models.BooleanField(default=False)
    intimidacaoMod = models.CharField(max_length=3, choices=periciasMod, default='Car')
    intimidacaoOutros = models.IntegerField(default=0)
    
    intuicao = models.BooleanField(default=False)
    intuicaoMod = models.CharField(max_length=3, choices=periciasMod, default='Sab')
    intuicaoOutros = models.IntegerField(default=0)
    
    investigacao = models.BooleanField(default=False)
    investigacaoMod = models.CharField(max_length=3, choices=periciasMod, default='Int')
    investigacaoOutros = models.IntegerField(default=0)
    
    jogatina = models.BooleanField(default=False)
    jogatinaMod = models.CharField(max_length=3, choices=periciasMod, default='Car')
    jogatinaOutros = models.IntegerField(default=0)
    
    ladinagem = models.BooleanField(default=False)
    ladinagemMod = models.CharField(max_length=3, choices=periciasMod, default='Des')
    ladinagemOutros = models.IntegerField(default=0)

    luta = models.BooleanField(default=False)
    lutaMod = models.CharField(max_length=3, choices=periciasMod, default='For')
    lutaOutros = models.IntegerField(default=0)
    
    misticismo = models.BooleanField(default=False)
    misticismoMod = models.CharField(max_length=3, choices=periciasMod, default='Int')
    misticismoOutros = models.IntegerField(default=0)
    
    nobreza = models.BooleanField(default=False)
    nobrezaMod = models.CharField(max_length=3, choices=periciasMod, default='Int')
    nobrezaOutros = models.IntegerField(default=0)
    
    oficio1 = models.BooleanField(default=False)
    oficio1Nome = models.CharField(max_length=50, null=True, blank=True)
    oficio1Mod = models.CharField(max_length=3, choices=periciasMod, default='Int')
    oficio1Outros = models.IntegerField(default=0)

    oficio2 = models.BooleanField(default=False)
    oficio2Nome = models.CharField(max_length=50, null=True, blank=True)
    oficio2Mod = models.CharField(max_length=3, choices=periciasMod, default='Int')
    oficio2Outros = models.IntegerField(default=0)
    
    percepcao = models.BooleanField(default=False)
    percepcaoMod = models.CharField(max_length=3, choices=periciasMod, default='Sab')
    percepcaoOutros = models.IntegerField(default=0)
    
    pilotagem = models.BooleanField(default=False)
    pilotagemMod = models.CharField(max_length=3, choices=periciasMod, default='Des')
    pilotagemOutros = models.IntegerField(default=0)
    
    pontaria = models.BooleanField(default=False)
    pontariaMod = models.CharField(max_length=3, choices=periciasMod, default='Des')
    pontariaOutros = models.IntegerField(default=0)
    
    reflexos = models.BooleanField(default=False)
    reflexosMod = models.CharField(max_length=3, choices=periciasMod, default='Des')
    reflexosOutros = models.IntegerField(default=0)
    
    religiao = models.BooleanField(default=False)
    religiaoMod = models.CharField(max_length=3, choices=periciasMod, default='Sab')
    religiaoOutros = models.IntegerField(default=0)

    sobrevivencia = models.BooleanField(default=False)
    sobrevivenciaMod = models.CharField(max_length=3, choices=periciasMod, default='Sab')
    sobrevivenciaOutros = models.IntegerField(default=0)
    
    vontade = models.BooleanField(default=False)
    vontadeMod = models.CharField(max_length=3, choices=periciasMod, default='Sab')
    vontadeOutros = models.IntegerField(default=0)
    

    #Equipamentos
    equipamentos = models.TextField(blank=True, null=True)
    TS = models.IntegerField(default=0)
    TO = models.IntegerField(default=0)
    carga = models.IntegerField(default=0)