# Generated by Django 4.2.7 on 2023-12-24 11:38

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('delivery', '0028_alter_pedido_restaurante'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='pedido',
            name='restaurante',
        ),
    ]
