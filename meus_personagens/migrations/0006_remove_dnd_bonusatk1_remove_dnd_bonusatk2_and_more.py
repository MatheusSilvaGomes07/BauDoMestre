# Generated by Django 4.2.4 on 2023-09-06 17:32

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('meus_personagens', '0005_remove_dnd_ataques_dnd_bonusatk1_dnd_bonusatk2_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='dnd',
            name='bonusAtk1',
        ),
        migrations.RemoveField(
            model_name='dnd',
            name='bonusAtk2',
        ),
        migrations.RemoveField(
            model_name='dnd',
            name='bonusAtk3',
        ),
        migrations.RemoveField(
            model_name='dnd',
            name='danoTipoAtk1',
        ),
        migrations.RemoveField(
            model_name='dnd',
            name='danoTipoAtk2',
        ),
        migrations.RemoveField(
            model_name='dnd',
            name='danoTipoAtk3',
        ),
        migrations.RemoveField(
            model_name='dnd',
            name='nomeAtk1',
        ),
        migrations.RemoveField(
            model_name='dnd',
            name='nomeAtk2',
        ),
        migrations.RemoveField(
            model_name='dnd',
            name='nomeAtk3',
        ),
    ]
