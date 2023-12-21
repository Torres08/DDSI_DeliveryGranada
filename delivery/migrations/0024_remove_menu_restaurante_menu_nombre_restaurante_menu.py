# Generated by Django 4.2.7 on 2023-12-21 18:24

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('delivery', '0023_alter_restaurante_propietario'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='menu',
            name='restaurante',
        ),
        migrations.AddField(
            model_name='menu',
            name='nombre',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='restaurante',
            name='menu',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='delivery.menu'),
        ),
    ]
