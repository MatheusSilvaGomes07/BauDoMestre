# Generated by Django 4.2.3 on 2023-07-23 19:26

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='campanha',
            name='slug',
        ),
        migrations.AlterField(
            model_name='campanha',
            name='nomeMestre',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='home.perfil'),
        ),
    ]
