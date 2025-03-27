# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class Usuarios(models.Model):
    nombre = models.CharField(max_length=30, blank=True, null=True)
    apellidos = models.CharField(max_length=50, blank=True, null=True)
    matricula = models.CharField(max_length=20, blank=True, null=True)
    edad = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'usuarios'

class ErrorLog(models.Model):
    codigo = models.CharField(max_length=10)
    mensaje = models.TextField()
    fecha = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = 'app_errorlog'
