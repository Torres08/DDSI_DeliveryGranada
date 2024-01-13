# Generated by Django 4.2.7 on 2024-01-13 13:08

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('delivery', '0054_remove_employee_rating_rating_empleado'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='employee',
            name='worktime',
        ),
        migrations.AddField(
            model_name='employee',
            name='worktimes',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='employees', to='delivery.worktime'),
        ),
    ]
