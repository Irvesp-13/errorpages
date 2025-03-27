from django.db import models

class alumno (models.Model):
    #Atributos de la clase Producto
    #Mandar a construir un campo de tipo texto con un maximo de 100 caracteres
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    edad = models.IntegerField()
    correo = models.EmailField(unique=True)
    matricula = models.CharField(max_length=10, unique=True)

    def __str__(self):
        return self.nombre
