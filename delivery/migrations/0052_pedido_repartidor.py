# Generated by Django 4.2.7 on 2024-01-14 15:05

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('delivery', '0051_employee_disponible_alter_usuario_pedidos'),
    ]

    operations = [
        migrations.AddField(
            model_name='pedido',
            name='repartidor',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='delivery.employee'),
        ),
    ]