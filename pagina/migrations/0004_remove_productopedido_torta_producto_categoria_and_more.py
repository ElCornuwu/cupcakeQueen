# Generated by Django 5.0.6 on 2024-06-29 05:00

import django.db.models.deletion
import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pagina', '0003_alter_producto_imagen'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='productopedido',
            name='torta',
        ),
        migrations.AddField(
            model_name='producto',
            name='categoria',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='pagina.categoria'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='productopedido',
            name='producto',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='pagina.producto'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='producto',
            name='imagen',
            field=models.ImageField(default='img/default-image.jpg', upload_to='productos/'),
        ),
        migrations.DeleteModel(
            name='Torta',
        ),
    ]
