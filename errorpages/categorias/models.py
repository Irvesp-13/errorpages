from django.db import models


class Categoria(models.Model):
    #Atributos de la clase Producto
    #Mandar a construir un campo de tipo texto con un maximo de 100 caracteres
    nombre = models.CharField(max_length=100)
    imagen = models.URLField()

    def __str__(self):
        return self.nombre