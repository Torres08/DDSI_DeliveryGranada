# Generated by Django 4.2.7 on 2024-01-13 14:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('delivery', '0059_alter_menu_restaurante_alter_producto_menu'),
    ]

    operations = [
        migrations.AddField(
            model_name='gasto',
            name='comentario',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='ingreso',
            name='comentario',
            field=models.TextField(blank=True, null=True),
        ),
    ]
