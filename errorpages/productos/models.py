from django.db import models

class Detalles_Producto(models.Model):
    descripcion = models.TextField(max_length=500)
    fecha_caducidad = models.DateField()

class Proveedor(models.Model):
    nombre = models.CharField(max_length=100)
    contacto = models.CharField(max_length=100)

    def __str__(self):
        return self.nombre

from categorias.models import Categoria

#Campos para relaciones
#OneToOneField ==> Uno a uno
#ForeignKey ==> Uno a muchos
#ManyToManyField ==> Muchos a muchos <--- Django genera una tabla de insersecion
class Producto(models.Model):
    #Atributos de la clase Producto
    #Mandar a construir un campo de tipo texto con un maximo de 100 caracteres
    nombre = models.CharField(max_length=100)
    precio = models.DecimalField(max_digits=10, decimal_places=2)
    imagen = models.URLField()
    #Relacion uno a uno
    Detalles_Producto = models.OneToOneField(
        Detalles_Producto, 
        null=True,
        on_delete=models.CASCADE
        )
    #Relacion uno a muchos
    categoria = models.ForeignKey(
        Categoria,
        null=True,
        blank=True,
        on_delete=models.CASCADE,
        db_column='categoria_id'
        )
    #Relacion muchos a muchos
    proveedor = models.ManyToManyField(
        #through=Modelo_personalizado para incluir campos nuevos 
        Proveedor,
        blank=True,
        null=True
        )

    def __str__(self):
        return self.nombre