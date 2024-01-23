# Generated by Django 4.2.7 on 2023-12-24 12:46

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('delivery', '0031_pedido_productos_pedido_restaurante'),
    ]

    operations = [
        migrations.AlterField(
            model_name='detallepedido',
            name='cantidad',
            field=models.PositiveIntegerField(default=1, validators=[django.core.validators.MinValueValidator(1), django.core.validators.MaxValueValidator(20)]),
        ),
    ]
