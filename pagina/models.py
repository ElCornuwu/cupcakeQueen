from django.db import models

# Create your models here.
class Categoria(models.Model):
    nombre = models.CharField(max_length=100, unique=True)
    descripcion = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.nombre

# Modelo para los pasteles
class Torta(models.Model):
    nombre = models.CharField(max_length=200)
    descripcion = models.TextField()
    precio = models.DecimalField(max_digits=10, decimal_places=2)
    imagen = models.ImageField(upload_to='cakes/')
    Categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE, related_name='cakes')

    def __str__(self):
        return self.nombre

# Modelo para los pedidos
class Pedido(models.Model):
    fecha_pedido = models.DateTimeField(auto_now_add=True)
    total = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f'Pedido {self.id}'

# Modelo para los detalles de cada pastel en un pedido
class ProductoPedido(models.Model):
    pedido = models.ForeignKey(Pedido, on_delete=models.CASCADE, related_name='order_items')
    torta = models.ForeignKey(Torta, on_delete=models.CASCADE)
    cantidad = models.PositiveIntegerField()
    precio = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f'{self.cantidad} x {self.torta.nombre}'

    def get_total_item_price(self):
        return self.cantidad * self.precio