# Generated by Django 4.2.5 on 2023-11-03 19:40

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('SistAmizade', '0006_remove_amigo_data_criacao'),
    ]

    operations = [
        migrations.AddField(
            model_name='amigo',
            name='data_criacao',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]
