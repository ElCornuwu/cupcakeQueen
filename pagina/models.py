from django.db import models
import os

# Create your models here.
class Categoria(models.Model):
    nombre = models.CharField(max_length=100, unique=True)
    descripcion = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.nombre

# Modelo para los pedidos
class Pedido(models.Model):
    fecha_pedido = models.DateTimeField(auto_now_add=True)
    total = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f'Pedido {self.id}'
    
class Producto(models.Model):
    nombre = models.CharField(max_length=100)
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE, default=1)
    descripcion = models.TextField()
    precio = models.IntegerField()
    imagen = models.ImageField(upload_to='productos/', default='img/default-image.jpg')

    def __str__(self):
        return self.nombre

    def delete(self, *args, **kwargs):
        # Borra el archivo de imagen físicamente del sistema de archivos
        self.imagen.delete()
        super().delete(*args, **kwargs)

# Modelo para los detalles de cada pastel en un pedido
class ProductoPedido(models.Model):
    pedido = models.ForeignKey(Pedido, on_delete=models.CASCADE, related_name='order_items')
    producto = models.ForeignKey(Producto, on_delete=models.CASCADE)
    cantidad = models.PositiveIntegerField()
    precio = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f'{self.cantidad} x {self.torta.nombre}'

    def get_total_item_price(self):
        return self.cantidad * self.precio
    
