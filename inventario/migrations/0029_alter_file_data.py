# Generated by Django 5.0.6 on 2024-09-22 17:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inventario', '0028_alter_file_data'),
    ]

    operations = [
        migrations.AlterField(
            model_name='file',
            name='data',
            field=models.CharField(default='22/09/2024', max_length=10),
        ),
    ]
