# Generated by Django 4.2.7 on 2023-11-28 19:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('SistAmizade', '0010_alter_amigo_slug'),
    ]

    operations = [
        migrations.AddField(
            model_name='amigo',
            name='fotoConta',
            field=models.CharField(default='Indefinido', max_length=200),
        ),
    ]