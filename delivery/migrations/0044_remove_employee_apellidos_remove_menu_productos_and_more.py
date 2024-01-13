# Generated by Django 4.2.7 on 2024-01-12 01:19

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('delivery', '0043_menu_productos'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='employee',
            name='Apellidos',
        ),
        migrations.RemoveField(
            model_name='menu',
            name='productos',
        ),
        migrations.RemoveField(
            model_name='rating',
            name='empleado',
        ),
        migrations.RemoveField(
            model_name='schedule',
            name='empleado',
        ),
        migrations.AddField(
            model_name='employee',
            name='rating',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, to='delivery.rating'),
        ),
        migrations.AddField(
            model_name='employee',
            name='schedule',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, to='delivery.schedule'),
        ),
        migrations.AddField(
            model_name='employee',
            name='worktime',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, to='delivery.worktime'),
        ),
        migrations.AlterField(
            model_name='schedule',
            name='worktime',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, to='delivery.worktime'),
        ),
        migrations.RemoveField(
            model_name='worktime',
            name='deliveries',
        ),
        migrations.AddField(
            model_name='worktime',
            name='deliveries',
            field=models.ManyToManyField(to='delivery.pedido'),
        ),
    ]