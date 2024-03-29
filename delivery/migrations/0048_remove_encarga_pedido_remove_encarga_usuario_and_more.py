# Generated by Django 4.2.7 on 2024-01-13 19:34

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('delivery', '0047_usuario_apellidos'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='encarga',
            name='pedido',
        ),
        migrations.RemoveField(
            model_name='encarga',
            name='usuario',
        ),
        migrations.RemoveField(
            model_name='produce',
            name='empleado',
        ),
        migrations.RemoveField(
            model_name='produce',
            name='gasto',
        ),
        migrations.RemoveField(
            model_name='schedule',
            name='empleado',
        ),
        migrations.RemoveField(
            model_name='schedule',
            name='worktime',
        ),
        migrations.RemoveField(
            model_name='employee',
            name='Hire_date',
        ),
        migrations.RemoveField(
            model_name='employee',
            name='Salario',
        ),
        migrations.RemoveField(
            model_name='ingreso',
            name='pedido',
        ),
        migrations.RemoveField(
            model_name='menu',
            name='productos',
        ),
        migrations.RemoveField(
            model_name='worktime',
            name='deliveries',
        ),
        migrations.RemoveField(
            model_name='worktime',
            name='worktime',
        ),
        migrations.AddField(
            model_name='employee',
            name='gasto',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, to='delivery.gasto'),
        ),
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
        migrations.AddField(
            model_name='pedido',
            name='empleado_asignado',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='pedidos_asignados', to='delivery.employee'),
        ),
        migrations.AddField(
            model_name='pedido',
            name='gasto_generado',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='pedidos_asignados', to='delivery.gasto'),
        ),
        migrations.AddField(
            model_name='pedido',
            name='precio_total',
            field=models.DecimalField(decimal_places=2, default=0.0, max_digits=10),
        ),
        migrations.AddField(
            model_name='pedido',
            name='usuario_asignado',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='pedidos_asignados', to='delivery.usuario'),
        ),
        migrations.AddField(
            model_name='rating',
            name='comentario',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='worktime',
            name='employee',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='worktimes', to='delivery.employee'),
        ),
        migrations.AlterField(
            model_name='employee',
            name='IBAN',
            field=models.CharField(max_length=25, unique=True),
        ),
        migrations.AlterField(
            model_name='employee',
            name='Nombre',
            field=models.CharField(max_length=30),
        ),
        migrations.AlterField(
            model_name='gasto',
            name='Importe',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='ingreso',
            name='Importe',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='rating',
            name='empleado',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='ratings', to='delivery.employee'),
        ),
        migrations.DeleteModel(
            name='Asigna',
        ),
        migrations.DeleteModel(
            name='Encarga',
        ),
        migrations.DeleteModel(
            name='Produce',
        ),
        migrations.DeleteModel(
            name='Schedule',
        ),
    ]
