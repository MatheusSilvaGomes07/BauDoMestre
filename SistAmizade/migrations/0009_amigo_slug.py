# Generated by Django 4.2.7 on 2023-11-28 18:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('SistAmizade', '0008_alter_solicitacaoamizade_unique_together'),
    ]

    operations = [
        migrations.AddField(
            model_name='amigo',
            name='slug',
            field=models.SlugField(default=None, max_length=255, unique=True),
        ),
    ]