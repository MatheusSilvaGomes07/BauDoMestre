# Generated by Django 4.2.5 on 2023-11-08 21:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inventario', '0008_alter_file_data'),
    ]

    operations = [
        migrations.AlterField(
            model_name='file',
            name='data',
            field=models.CharField(default='08/11/2023', max_length=10),
        ),
    ]
