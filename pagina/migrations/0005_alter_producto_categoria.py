# Generated by Django 5.0.6 on 2024-06-29 05:03

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pagina', '0004_remove_productopedido_torta_producto_categoria_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='producto',
            name='categoria',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='pagina.categoria'),
        ),
    ]
