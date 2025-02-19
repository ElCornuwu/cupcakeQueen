# Generated by Django 5.0.6 on 2024-06-30 03:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pagina', '0008_alter_producto_precio'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='productopedido',
            name='pedido',
        ),
        migrations.RemoveField(
            model_name='productopedido',
            name='producto',
        ),
        migrations.AlterField(
            model_name='producto',
            name='imagen',
            field=models.ImageField(default='static\\img\\default-image.jpg', upload_to='productos/'),
        ),
        migrations.DeleteModel(
            name='Pedido',
        ),
        migrations.DeleteModel(
            name='ProductoPedido',
        ),
    ]
