# Generated by Django 4.2.5 on 2023-11-21 20:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('chat', '0006_solicitacaoentrada'),
    ]

    operations = [
        migrations.AddField(
            model_name='solicitacaoentrada',
            name='aceita',
            field=models.BooleanField(default=False),
        ),
    ]
