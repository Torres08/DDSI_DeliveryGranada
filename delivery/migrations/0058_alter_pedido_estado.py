# Generated by Django 4.2.7 on 2024-01-15 13:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('delivery', '0057_alter_pedido_estado'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pedido',
            name='estado',
            field=models.CharField(choices=[('En Preparación', 'En preparación'), ('envio', 'En envío'), ('entregado', 'Entregado')], default='En Preparación', max_length=40),
        ),
    ]
