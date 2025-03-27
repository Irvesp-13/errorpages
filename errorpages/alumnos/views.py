from .models import alumno
from .serializers import AlumnoSerializer
from rest_framework import viewsets #Vamos a crear una vista de varial al mismo tiempo
from django.shortcuts import render
from rest_framework.renderers import JSONRenderer

class AlumnoViewSet(viewsets.ModelViewSet):
    #1 Saber a que objeto hago referencia
    queryset = alumno.objects.all()
    #2 Serularizar el objeto
    serializer_class = AlumnoSerializer
    #3 Renderizar la vista
    renderer_classes = [JSONRenderer] #Vamos a renderizar la vista en formato JSON


#Views de la aplicacion:
def index(request):
    return render(request, 'Diaz_Jose.html')
