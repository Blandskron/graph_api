from django.db import models

class Venta(models.Model):
    producto = models.CharField(max_length=255)
    cantidad = models.IntegerField()
    fecha = models.DateField()
    precio = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return self.producto
