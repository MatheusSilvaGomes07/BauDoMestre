# Generated by Django 4.2.1 on 2023-11-25 19:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inventario', '0019_alter_file_data'),
    ]

    operations = [
        migrations.AlterField(
            model_name='file',
            name='data',
            field=models.CharField(default='25/11/2023', max_length=10),
        ),
    ]
