# Generated by Django 5.0.1 on 2024-11-23 17:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inventario', '0025_alter_file_data_alter_file_extensao'),
    ]

    operations = [
        migrations.AlterField(
            model_name='file',
            name='data',
            field=models.CharField(default='23/11/2024', max_length=10),
        ),
    ]
