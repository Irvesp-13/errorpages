from .models import alumno
from rest_framework import serializers

class AlumnoSerializer(serializers.ModelSerializer):
    class Meta:
        model = alumno
        fields = '__all__' #Serializar todos los campos del modelo Producto