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

    #2° Página, Magias
    spellCastingOptions = [
        ('--', '--'),
        ('Força', 'Força'),
        ('Dextreza', 'Dextreza'),
        ('Constituição', 'Constituição'),
        ('Inteligência', 'Inteligência'),
        ('Sabedoria', 'Sabedoria'),
        ('Carisma', 'Carisma'),
    ]

    spellCasting = models.CharField(max_length=20, choices=spellCastingOptions, default='--')
    spellDC = models.IntegerField(null=True, blank=True)
    spellAttackBonus = models.IntegerField(null=True, blank=True)


    cantips = models.TextField(null=True, blank=True)

    circulo1QteMax = models.IntegerField(null=True, blank=True)
    circulo1Qte = models.IntegerField(null=True, blank=True)
    circulo1 = models.TextField(null=True, blank=True)

    circulo2QteMax = models.IntegerField(null=True, blank=True)
    circulo2Qte = models.IntegerField(null=True, blank=True)
    circulo2 = models.TextField(null=True, blank=True)

    circulo3QteMax = models.IntegerField(null=True, blank=True)
    circulo3Qte = models.IntegerField(null=True, blank=True)
    circulo3 = models.TextField(null=True, blank=True)

    circulo4QteMax = models.IntegerField(null=True, blank=True)
    circulo4Qte = models.IntegerField(null=True, blank=True)
    circulo4 = models.TextField(null=True, blank=True)

    circulo5QteMax = models.IntegerField(null=True, blank=True)
    circulo5Qte = models.IntegerField(null=True, blank=True)
    circulo5 = models.TextField(null=True, blank=True)

    circulo6QteMax = models.IntegerField(null=True, blank=True)
    circulo6Qte = models.IntegerField(null=True, blank=True)
    circulo6 = models.TextField(null=True, blank=True)

    circulo7QteMax = models.IntegerField(null=True, blank=True)
    circulo7Qte = models.IntegerField(null=True, blank=True)
    circulo7 = models.TextField(null=True, blank=True)

    circulo8QteMax = models.IntegerField(null=True, blank=True)
    circulo8Qte = models.IntegerField(null=True, blank=True)
    circulo8 = models.TextField(null=True, blank=True)

    circulo9QteMax = models.IntegerField(null=True, blank=True)
    circulo9Qte = models.IntegerField(null=True, blank=True)
    circulo9 = models.TextField(null=True, blank=True)



    



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




class CallOfCthulhu(Personagem):
    ocupacao = models.CharField(max_length=100)
    localNascimento = models.CharField(max_length=100, null=True, blank=True)
    pronome = models.CharField(max_length=10, null=True, blank=True)
    residencia = models.CharField(max_length=100)
    idade = models.IntegerField()

    #Atributos
    forca = models.IntegerField(default=0)
    con = models.IntegerField(default=0)
    des = models.IntegerField(default=0)
    int = models.IntegerField(default=0)
    tam = models.IntegerField(default=0)
    pod = models.IntegerField(default=0)
    apa = models.IntegerField(default=0)
    edu = models.IntegerField(default=0)

    pvMax = models.IntegerField(default=0, null=True, blank=True)
    pvAtual = models.IntegerField(default=0, null=True, blank=True)

    magiaMax = models.IntegerField(default=0, null=True, blank=True)
    magiaAtual = models.IntegerField(default=0, null=True, blank=True)

    sorte = models.IntegerField(default=0)

    sanidadeMax = models.IntegerField(default=0, null=True, blank=True)
    sanidadeAtual = models.IntegerField(default=0, null=True, blank=True)

    #Pericias
    contabilidade = models.BooleanField(default=False)
    contabilidadeMod = models.IntegerField(null=True, blank=True)

    antropologia = models.BooleanField(default=False)
    antropologiaMod = models.IntegerField(null=True, blank=True)
    
    arqueologia = models.BooleanField(default=False)
    arqueologiaMod = models.IntegerField(null=True, blank=True)
    
    livre1 = models.BooleanField(default=False)
    livre1Nome = models.CharField(max_length=50, null=True, blank=True)
    livre1Mod = models.IntegerField(null=True, blank=True)
    
    livre2 = models.BooleanField(default=False)
    livre2Nome = models.CharField(max_length=50, null=True, blank=True)
    livre2Mod = models.IntegerField(null=True, blank=True)

    seducao = models.BooleanField(default=False)
    seducaoMod = models.IntegerField(null=True, blank=True)
    
    escalada = models.BooleanField(default=False)
    escaladaMod = models.IntegerField(null=True, blank=True)
    

    creditoMod = models.IntegerField(null=True, blank=True)


    cthulhuMitosMod = models.IntegerField(null=True, blank=True)

    disfarce = models.BooleanField(default=False)
    disfarceMod = models.IntegerField(null=True, blank=True)

    esquiva = models.BooleanField(default=False)
    esquivaMod = models.IntegerField(null=True, blank=True)

    dirigirAuto = models.BooleanField(default=False)
    dirigirAutoMod = models.IntegerField(null=True, blank=True)

    reparoEletrico = models.BooleanField(default=False)
    reparoEletricoMod = models.IntegerField(null=True, blank=True)

    conversaRapida = models.BooleanField(default=False)
    conversaRapidaMod = models.IntegerField(null=True, blank=True)

    luta = models.BooleanField(default=False)
    luraMod = models.IntegerField(null=True, blank=True)

    livre3 = models.BooleanField(default=False)
    livre3Nome = models.CharField(max_length=50, null=True, blank=True)
    livre3Mod = models.IntegerField(null=True, blank=True)

    livre4 = models.BooleanField(default=False)
    livre4Nome = models.CharField(max_length=50, null=True, blank=True)
    livre4Mod = models.IntegerField(null=True, blank=True)

    #Pistola
    armaDeFogo = models.BooleanField(default=False)
    armaDeFogoMod = models.IntegerField(null=True, blank=True)

    #Rifles e escopetas
    armaDeFogoPesada = models.BooleanField(default=False)
    armaDeFogoPesadaMod = models.IntegerField(null=True, blank=True)

    livre4 = models.BooleanField(default=False)
    livre4Nome = models.CharField(max_length=50, null=True, blank=True)
    livre4Mod = models.IntegerField(null=True, blank=True)
    
    primeirosSocorros = models.BooleanField(default=False)
    primeirosSocorrosMod = models.IntegerField(null=True, blank=True)

    historia = models.BooleanField(default=False)
    historiaMod = models.IntegerField(null=True, blank=True)

    intimidacao = models.BooleanField(default=False)
    intimidacaoMod = models.IntegerField(null=True, blank=True)    
     
    pulo = models.BooleanField(default=False)
    puloMod = models.IntegerField(null=True, blank=True)  

    livre5 = models.BooleanField(default=False)
    livre5Nome = models.CharField(max_length=50, null=True, blank=True)
    livre5Mod = models.IntegerField(null=True, blank=True)

    livre6 = models.BooleanField(default=False)
    livre6Nome = models.CharField(max_length=50, null=True, blank=True)
    livre6Mod = models.IntegerField(null=True, blank=True)

    livre7 = models.BooleanField(default=False)
    livre7Nome = models.CharField(max_length=50, null=True, blank=True)
    livre7Mod = models.IntegerField(null=True, blank=True)

    livre8 = models.BooleanField(default=False)
    livre8Nome = models.CharField(max_length=50, null=True, blank=True)
    livre8Mod = models.IntegerField(null=True, blank=True)

    direito = models.BooleanField(default=False)
    direitoMod = models.IntegerField(null=True, blank=True)

    pesquisarBiblioteca = models.BooleanField(default=False)
    pesquisarBibliotecaMod = models.IntegerField(null=True, blank=True)

    escutar = models.BooleanField(default=False)
    escutarMod = models.IntegerField(null=True, blank=True)

    chaveiro = models.BooleanField(default=False)
    chaveiroMod = models.IntegerField(null=True, blank=True)

    reparoMecanico = models.BooleanField(default=False)
    reparoMecanicoMod = models.IntegerField(null=True, blank=True)

    medicina = models.BooleanField(default=False)
    medicinaMod = models.IntegerField(null=True, blank=True)

    linguaNativa = models.BooleanField(default=False)
    linguaNativaMod = models.IntegerField(null=True, blank=True)

    navegacao = models.BooleanField(default=False)
    navegacaoMod = models.IntegerField(null=True, blank=True)

    persuasao = models.BooleanField(default=False)
    persuasaoMod = models.IntegerField(null=True, blank=True)

    livre9 = models.BooleanField(default=False)
    livre9Nome = models.CharField(max_length=50, null=True, blank=True)
    livre9Mod = models.IntegerField(null=True, blank=True)

    psicanalise = models.BooleanField(default=False)
    psicanaliseMod = models.IntegerField(null=True, blank=True)

    psicologia = models.BooleanField(default=False)
    psicologiaMod = models.IntegerField(null=True, blank=True)

    cavalgar = models.BooleanField(default=False)
    cavalgarMod = models.IntegerField(null=True, blank=True)

    livre10 = models.BooleanField(default=False)
    livre10Nome = models.CharField(max_length=50, null=True, blank=True)
    livre10Mod = models.IntegerField(null=True, blank=True)

    livre11 = models.BooleanField(default=False)
    livre11Nome = models.CharField(max_length=50, null=True, blank=True)
    livre11Mod = models.IntegerField(null=True, blank=True)

    livre12 = models.BooleanField(default=False)
    livre12Nome = models.CharField(max_length=50, null=True, blank=True)
    livre12Mod = models.IntegerField(null=True, blank=True)

    maosHabeis = models.BooleanField(default=False)
    maosHabeisMod = models.IntegerField(null=True, blank=True)

    esconder = models.BooleanField(default=False)
    esconderMod = models.IntegerField(null=True, blank=True)

    furtividade = models.BooleanField(default=False)
    furtividadeMod = models.IntegerField(null=True, blank=True)

    livre13 = models.BooleanField(default=False)
    livre13Nome = models.CharField(max_length=50, null=True, blank=True)
    livre13Mod = models.IntegerField(null=True, blank=True)

    nadar = models.BooleanField(default=False)
    nadarMod = models.IntegerField(null=True, blank=True)

    arremessar = models.BooleanField(default=False)
    arremessarMod = models.IntegerField(null=True, blank=True)

    rastrear = models.BooleanField(default=False)
    rastrearMod = models.IntegerField(null=True, blank=True)

    livre14 = models.BooleanField(default=False)
    livre14Nome = models.CharField(max_length=50, null=True, blank=True)
    livre14Mod = models.IntegerField(null=True, blank=True)

    livre15 = models.BooleanField(default=False)
    livre15Nome = models.CharField(max_length=50, null=True, blank=True)
    livre15Mod = models.IntegerField(null=True, blank=True)

    livre16 = models.BooleanField(default=False)
    livre16Nome = models.CharField(max_length=50, null=True, blank=True)
    livre16Mod = models.IntegerField(null=True, blank=True)

    livre17 = models.BooleanField(default=False)
    livre17Nome = models.CharField(max_length=50, null=True, blank=True)
    livre17Mod = models.IntegerField(null=True, blank=True)

    #Ataques
    ataque1 = models.CharField(max_length=100, null=True, blank=True)
    ataque1Mod = models.IntegerField(null=True, blank=True)
    ataque1Dano = models.CharField(max_length=100, null=True, blank=True)
    ataque1Num = models.IntegerField(null=True, blank=True)
    ataque1Alcance = models.FloatField(null=True, blank=True)
    ataque1Municao = models.IntegerField(null=True, blank=True)
    ataque1Defeito = models.IntegerField(null=True, blank=True)

    ataque2 = models.CharField(max_length=100, null=True, blank=True)
    ataque2Mod = models.IntegerField(null=True, blank=True)
    ataque2Dano = models.CharField(max_length=100, null=True, blank=True)
    ataque2Num = models.IntegerField(null=True, blank=True)
    ataque2Alcance = models.FloatField(null=True, blank=True)
    ataque2Municao = models.IntegerField(null=True, blank=True)
    ataque2Defeito = models.IntegerField(null=True, blank=True) 
    
    ataque3 = models.CharField(max_length=100, null=True, blank=True)
    ataque3Mod = models.IntegerField(null=True, blank=True)
    ataque3Dano = models.CharField(max_length=100, null=True, blank=True)
    ataque3Num = models.IntegerField(null=True, blank=True)
    ataque3Alcance = models.FloatField(null=True, blank=True)
    ataque3Municao = models.IntegerField(null=True, blank=True)
    ataque3Defeito = models.IntegerField(null=True, blank=True)

    ataque4 = models.CharField(max_length=100, null=True, blank=True)
    ataque4Mod = models.IntegerField(null=True, blank=True)
    ataque4Dano = models.CharField(max_length=100, null=True, blank=True)
    ataque4Num = models.IntegerField(null=True, blank=True)
    ataque4Alcance = models.FloatField(null=True, blank=True)
    ataque4Municao = models.IntegerField(null=True, blank=True)
    ataque4Defeito = models.IntegerField(null=True, blank=True)

    movimentacao = models.IntegerField(null=True, blank=True)
    build = models.IntegerField(null=True, blank=True)
    esquiva2 = models.IntegerField(null=True, blank=True)
    danoBonus = models.IntegerField(null=True, blank=True)


    #Lores
    descricaoPessoal = models.TextField(null=True, blank=True)
    ideologia = models.TextField(null=True, blank=True)
    pessoasSignificantes = models.TextField(null=True, blank=True)
    lugaresSignificativos = models.TextField(null=True, blank=True)
    bensPreciosos = models.TextField(null=True, blank=True)
    tracos = models.TextField(null=True, blank=True)
    feridas = models.TextField(null=True, blank=True)
    fobiasManias = models.TextField(null=True, blank=True)
    magias = models.TextField(null=True, blank=True)
    encontroEntidades = models.TextField(null=True, blank=True)

    equipamentos = models.TextField(null=True, blank=True)
    posses = models.TextField(null=True, blank=True)


    #Riquezas
    nivelGastos = models.CharField(max_length=100, null=True, blank=True)
    dinheiro = models.IntegerField(null=True, blank=True)
    bens = models.CharField(max_length=100, null=True, blank=True)
    lore = models.TextField(null=True, blank=True)

