# Generated by Django 4.2.5 on 2023-11-17 00:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inventario', '0010_alter_file_data'),
    ]

    operations = [
        migrations.AlterField(
            model_name='file',
            name='data',
            field=models.CharField(default='16/11/2023', max_length=10),
        ),
    ]