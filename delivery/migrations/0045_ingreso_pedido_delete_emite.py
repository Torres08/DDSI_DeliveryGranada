# Generated by Django 4.2.7 on 2024-01-12 00:19

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('delivery', '0044_remove_pedido_precio_total'),
    ]

    operations = [
        migrations.AddField(
            model_name='ingreso',
            name='pedido',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='delivery.pedido', unique=True),
        ),
        migrations.DeleteModel(
            name='Emite',
        ),
    ]
