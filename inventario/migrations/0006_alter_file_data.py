# Generated by Django 4.2.5 on 2023-10-18 21:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inventario', '0005_alter_file_data'),
    ]

    operations = [
        migrations.AlterField(
            model_name='file',
            name='data',
            field=models.CharField(default='18/10/2023', max_length=10),
        ),
    ]
