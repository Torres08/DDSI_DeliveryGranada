# Generated by Django 4.2.7 on 2023-12-18 17:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('delivery', '0022_remove_pedido_cantidad_remove_pedido_nombre_producto_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='restaurante',
            name='Propietario',
            field=models.CharField(max_length=40),
        ),
    ]
