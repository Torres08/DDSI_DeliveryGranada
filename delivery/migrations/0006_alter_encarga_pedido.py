# Generated by Django 4.2.7 on 2023-11-30 14:42

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('delivery', '0005_encarga'),
    ]

    operations = [
        migrations.AlterField(
            model_name='encarga',
            name='pedido',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='delivery.pedido', unique=True),
        ),
    ]
