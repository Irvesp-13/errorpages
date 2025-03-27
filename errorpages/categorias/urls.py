from django.urls import path
from .views import *

urlpatterns = [
    path('api/get/', json_categoria, name='lista'),
    path('agregar/', agregar_categoria, name='agregarC'),
    path('json/', json_categoria, name='json_categoria'),
    path('api/post/', registrar_categoria, name='post'),
]