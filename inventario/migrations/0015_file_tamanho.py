# Generated by Django 4.2.5 on 2023-11-18 01:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inventario', '0014_remove_file_tamanho'),
    ]

    operations = [
        migrations.AddField(
            model_name='file',
            name='tamanho',
            field=models.IntegerField(default=0),
        ),
    ]