# Generated by Django 5.0.1 on 2024-11-23 17:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('meus_personagens', '0021_alter_callofcthulhu_unique_together_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='dnd',
            name='lore',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='ordemparanormal',
            name='lore',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='tormenta',
            name='lore',
            field=models.TextField(blank=True, null=True),
        ),
    ]
