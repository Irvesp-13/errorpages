from django.urls import path, include
from .views import *
from rest_framework.routers import SimpleRouter

router = SimpleRouter()
#Registrar el path comun para la vista de Alumno
router.register(r'api', AlumnoViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('index/', index, name='index'),
]