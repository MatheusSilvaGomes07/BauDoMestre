# Generated by Django 5.0.6 on 2024-11-10 22:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tabletop', '0002_alter_token_position_x_alter_token_position_y'),
    ]

    operations = [
        migrations.AlterField(
            model_name='token',
            name='position_x',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='token',
            name='position_y',
            field=models.IntegerField(default=0),
        ),
    ]