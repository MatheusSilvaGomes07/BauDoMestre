# Generated by Django 4.2.7 on 2023-11-28 17:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inventario', '0020_alter_file_data'),
    ]

    operations = [
        migrations.AlterField(
            model_name='file',
            name='data',
            field=models.CharField(default='28/11/2023', max_length=10),
        ),
    ]
