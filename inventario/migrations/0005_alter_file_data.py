# Generated by Django 4.2.5 on 2023-10-14 21:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inventario', '0004_file_data'),
    ]

    operations = [
        migrations.AlterField(
            model_name='file',
            name='data',
            field=models.CharField(default='14/10/2023', max_length=10),
        ),
    ]
