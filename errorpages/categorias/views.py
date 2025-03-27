from django.shortcuts import render, redirect
from django.http import JsonResponse
from .models import Categoria
from .forms import CategoriaForm
import json as Json
from django.views.decorators.csrf import csrf_exempt

def lista_categorias(request):
    categorias = Categoria.objects.all()
    data = [
        {
            'nombre': c.nombre,
            'imagen': c.imagen
        }
        for c in categorias
    ]
    return JsonResponse(data, safe=False)

def agregar_categoria(request):
    if request.method == 'POST':
        form = CategoriaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('lista')
    else:
        form = CategoriaForm()
    return render(request, 'agregarC.html', {'form': form})


@csrf_exempt  # Solo para pruebas, usa CSRF Token en producción
def registrar_categoria(request):
    if request.method == "POST":
        nombre = request.POST.get('nombre')
        imagen = request.POST.get('imagen')

        if not nombre or not imagen:  # Validación de datos
            return JsonResponse({"error": "Faltan campos obligatorios"}, status=400)

        categoria = Categoria.objects.create(nombre=nombre, imagen=imagen)
        return JsonResponse({"mensaje": "Categoría agregada correctamente"}, status=201)

    return JsonResponse({"error": "Método no permitido"}, status=405)

def json_categoria(request):
    if request.method == 'GET':
        categorias = Categoria.objects.all()
        data = [
            {
                'nombre': c.nombre,
                'imagen': c.imagen
            }
            for c in categorias
        ]
        return JsonResponse(data, safe=False)
    elif request.method == 'POST':
        form = CategoriaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('json_categoria')
    else:
        form = CategoriaForm()
    return render(request, 'listas.html', {'form': form})
