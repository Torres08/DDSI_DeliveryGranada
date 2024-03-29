# Generated by Django 4.2.7 on 2024-01-14 11:50

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('delivery', '0049_remove_pedido_empleado_asignado_alter_usuario_dni_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='employee',
            name='gasto',
        ),
        migrations.RemoveField(
            model_name='pedido',
            name='gasto_generado',
        ),
        migrations.RemoveField(
            model_name='pedido',
            name='usuario_asignado',
        ),
        migrations.AddField(
            model_name='gasto',
            name='employee',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='delivery.employee'),
        ),
        migrations.AddField(
            model_name='ingreso',
            name='pedido',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='delivery.pedido'),
        ),
        migrations.AddField(
            model_name='usuario',
            name='pedidos',
            field=models.ManyToManyField(to='delivery.pedido'),
        ),
        migrations.AlterField(
            model_name='pedido',
            name='estado',
            field=models.CharField(choices=[('preparacion', 'En preparación'), ('envio', 'En envío'), ('entregado', 'Entregado')], default='preparacion', max_length=40),
        ),
        migrations.AlterUniqueTogether(
            name='ingreso',
            unique_together={('pedido',)},
        ),
    ]
