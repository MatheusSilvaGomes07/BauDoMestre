# Generated by Django 4.2.5 on 2023-10-13 17:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inventario', '0003_alter_file_pasta'),
    ]

    operations = [
        migrations.AddField(
            model_name='file',
            name='data',
            field=models.CharField(default='13/10/2023', max_length=10),
        ),
    ]