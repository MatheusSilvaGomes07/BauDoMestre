# Generated by Django 4.2.5 on 2023-11-05 23:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inventario', '0007_alter_file_data'),
    ]

    operations = [
        migrations.AlterField(
            model_name='file',
            name='data',
            field=models.CharField(default='05/11/2023', max_length=10),
        ),
    ]
