# Generated by Django 4.2.5 on 2023-09-26 02:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('meus_personagens', '0018_dnd_foto'),
    ]

    operations = [
        migrations.AlterField(
            model_name='dnd',
            name='foto',
            field=models.ImageField(upload_to='images'),
        ),
    ]
