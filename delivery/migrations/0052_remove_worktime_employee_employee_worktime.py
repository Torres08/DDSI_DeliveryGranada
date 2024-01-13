# Generated by Django 4.2.7 on 2024-01-13 12:04

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('delivery', '0051_remove_employee_worktime_remove_worktime_worktime_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='worktime',
            name='employee',
        ),
        migrations.AddField(
            model_name='employee',
            name='worktime',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, to='delivery.worktime'),
        ),
    ]