# Generated by Django 4.2.2 on 2023-09-23 22:52

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('chat', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='grupo',
            name='criador',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='grupos_criados', to=settings.AUTH_USER_MODEL),
        ),
    ]
