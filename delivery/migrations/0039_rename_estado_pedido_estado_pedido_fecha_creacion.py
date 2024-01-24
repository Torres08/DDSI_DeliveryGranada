# Generated by Django 4.2.7 on 2023-12-28 21:38

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('delivery', '0038_delete_comunica'),
    ]

    operations = [
        migrations.RenameField(
            model_name='pedido',
            old_name='Estado',
            new_name='estado',
        ),
        migrations.AddField(
            model_name='pedido',
            name='fecha_creacion',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]