# Generated by Django 4.2.7 on 2023-12-14 18:23

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('delivery', '0016_remove_worktime_empleado_schedule'),
    ]

    operations = [
        migrations.AddField(
            model_name='schedule',
            name='worktime',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='delivery.worktime', unique=True),
        ),
    ]
