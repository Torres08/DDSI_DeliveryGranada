# Generated by Django 4.2.7 on 2024-01-15 11:05

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('delivery', '0053_remove_usuario_pedidos_encarga'),
    ]

    operations = [
        migrations.AddField(
            model_name='pedido',
            name='usuario',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='delivery.usuario'),
        ),
    ]