# Generated by Django 5.0.6 on 2024-06-29 22:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pagina', '0007_producto_categoria'),
    ]

    operations = [
        migrations.AlterField(
            model_name='producto',
            name='precio',
            field=models.IntegerField(),
        ),
    ]
