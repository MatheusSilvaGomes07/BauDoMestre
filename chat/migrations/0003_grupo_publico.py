# Generated by Django 4.2.5 on 2023-11-05 23:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('chat', '0002_grupo_criador'),
    ]

    operations = [
        migrations.AddField(
            model_name='grupo',
            name='publico',
            field=models.BooleanField(default=False),
        ),
    ]
