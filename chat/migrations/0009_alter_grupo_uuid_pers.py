# Generated by Django 4.2.7 on 2023-12-01 19:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('chat', '0008_grupo_uuid_pers'),
    ]

    operations = [
        migrations.AlterField(
            model_name='grupo',
            name='uuid_pers',
            field=models.CharField(default=None, max_length=10),
        ),
    ]
