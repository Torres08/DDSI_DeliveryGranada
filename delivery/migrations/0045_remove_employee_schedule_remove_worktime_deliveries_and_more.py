# Generated by Django 4.2.7 on 2024-01-12 01:25

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('delivery', '0044_remove_employee_apellidos_remove_menu_productos_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='employee',
            name='schedule',
        ),
        migrations.RemoveField(
            model_name='worktime',
            name='deliveries',
        ),
        migrations.AddField(
            model_name='employee',
            name='gasto',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, to='delivery.gasto'),
        ),
        migrations.AddField(
            model_name='rating',
            name='comentario',
            field=models.TextField(null=True),
        ),
    ]
