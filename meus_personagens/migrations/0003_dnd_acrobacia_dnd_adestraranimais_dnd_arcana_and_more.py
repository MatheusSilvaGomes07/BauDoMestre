# Generated by Django 4.2.5 on 2023-09-05 19:26

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('meus_personagens', '0002_remove_dnd_acrobacia_remove_dnd_adestraranimais_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='dnd',
            name='acrobacia',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='dnd',
            name='adestrarAnimais',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='dnd',
            name='arcana',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='dnd',
            name='atletismo',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='dnd',
            name='atuacao',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='dnd',
            name='ca',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='dnd',
            name='caracteristicas',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='dnd',
            name='carisma',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='dnd',
            name='carismaSalvaguarda',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='dnd',
            name='classe',
            field=models.CharField(default=1, max_length=100),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='dnd',
            name='const',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='dnd',
            name='constSalvaguarda',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='dnd',
            name='deathFailure1',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='dnd',
            name='deathFailure2',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='dnd',
            name='deathFailure3',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='dnd',
            name='deathSucess1',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='dnd',
            name='deathSucess2',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='dnd',
            name='deathSucess3',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='dnd',
            name='dex',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='dnd',
            name='dexSalvaguarda',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='dnd',
            name='enganacao',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='dnd',
            name='forca',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='dnd',
            name='forcaSalvaguarda',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='dnd',
            name='fraquezas',
            field=models.CharField(blank=True, max_length=350, null=True),
        ),
        migrations.AddField(
            model_name='dnd',
            name='furtividade',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='dnd',
            name='historia',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='dnd',
            name='hitDice',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='dnd',
            name='hitDiceType',
            field=models.CharField(choices=[('d4', 'd4'), ('d6', 'd6'), ('d8', 'd8'), ('d10', 'd10'), ('d12', 'd12')], default='d4', max_length=4),
        ),
        migrations.AddField(
            model_name='dnd',
            name='ideias',
            field=models.CharField(blank=True, max_length=350, null=True),
        ),
        migrations.AddField(
            model_name='dnd',
            name='inspiracao',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='dnd',
            name='int',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='dnd',
            name='intSalvaguarda',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='dnd',
            name='intimidacao',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='dnd',
            name='intuicao',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='dnd',
            name='inventario',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='dnd',
            name='investigacao',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='dnd',
            name='medicina',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='dnd',
            name='movi',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='dnd',
            name='natureza',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='dnd',
            name='nivel',
            field=models.IntegerField(default=1, validators=[django.core.validators.MinValueValidator(1)]),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='dnd',
            name='outrasProf_Linguagens',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='dnd',
            name='pc',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='dnd',
            name='pe',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='dnd',
            name='percepcao',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='dnd',
            name='personalidade',
            field=models.CharField(blank=True, max_length=350, null=True),
        ),
        migrations.AddField(
            model_name='dnd',
            name='persuasao',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='dnd',
            name='pl',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='dnd',
            name='po',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='dnd',
            name='pp',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='dnd',
            name='prestigitacao',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='dnd',
            name='proficienciasFerramentas',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='dnd',
            name='raca',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='dnd',
            name='religiao',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='dnd',
            name='sab',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='dnd',
            name='sabSalvaguarda',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='dnd',
            name='sobrevivencia',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='dnd',
            name='sub_classe',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='dnd',
            name='sub_raca',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='dnd',
            name='vidaTemp',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='dnd',
            name='vinculos',
            field=models.CharField(blank=True, max_length=350, null=True),
        ),
        migrations.AddField(
            model_name='dnd',
            name='xp',
            field=models.IntegerField(blank=True, null=True, validators=[django.core.validators.MinValueValidator(0)]),
        ),
    ]
