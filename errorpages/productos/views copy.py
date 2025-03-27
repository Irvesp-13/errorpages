from django.shortcuts import render, redirect
from django.http import JsonResponse
from .models import Producto
from .forms import ProductoForm
import json as Json
from django.shortcuts import get_object_or_404

#Metodo que devuelve una respuesta en formato JSON
def lista_productos(request):
    #Obtener todas las instancias del objeto de la BD
    productos = Producto.objects.all()

    #Construir una variable en formato de diccionario
    #Por que el JSONResponse lo necesita
    data = [
        #Objeto de producto construido al aire
        {
        'nombre': p.nombre,
        'precio': p.precio,
        'imagen': p.imagen
        }
        for p in productos
    ]

    #Devolver una respuesta en formato JSON
    return JsonResponse(data, safe=False)

#Funcion para mandar a la vista de form 
def agregar_producto(request):
    #Averiguar si estamos teniendo una respuesta de form 
    if request.method == 'POST':
        #Crear una instancia del form 
        form = ProductoForm(request.POST)

        #Validar el form 
        if form.is_valid():
            #Guardar el form en la BD
            form.save()
            return redirect('lista')
    else:
        #Crear una instancia del form 
        form = ProductoForm()
    return render(request, 'agregar.html', {'form': form})

#Funcion que registre sin recargar la pagina (sin render)
def registrar_producto(request):
    if request.method == 'POST':
        #Checar que estamos manejando un request de tipo POST
        try:
            #Intentar obtener los datos del body del request
            data = Json.loads(request.body)
            producto = Producto.objects.create(
                #Constructor de un objeto de tipo Producto
                nombre = data['nombre'],
                precio = data['precio'],
                imagen = data['imagen']
            )#La funcion create directamente ingresa el objeto en la BD
            return JsonResponse({'mensaje': 'Producto registrado correctamente','id':producto.id}, status=201)
        except Exception as e:
            return JsonResponse({'mensaje': str(e)}, status=400)
    return JsonResponse({'mensaje': 'Metodo no permitido'}, status=405)

#El metodo del API PUT para actualizar un producto
def actualizar_producto(request, id):
    if request.method == 'PUT':
        producto = get_object_or_404(Producto, id=id)
        #Intentar Actualizar el producto
        #1. Obtener la entidad/modelo para actualizar
        #Parametros: modelo y id
        try:
            #Vamos a intentar obtener los datos del body del request
            #2.- Con la informacion que deberiamos estar recibiendo en el body del request
            data = Json.loads(request.body)
            #3.- Actualizar cada campo disponible de la entidad
            producto.nombre = data['nombre', producto.nombre]
            producto.precio = data['precio', producto.precio]
            producto.imagen = data['imagen', producto.imagen]
            producto.save()
            #4.- Retornar una respuesta en formato JSON con un mensaje de exito
            return JsonResponse({'mensaje': 'Producto actualizado correctamente'}, status=200)
        except Exception as e:
            return JsonResponse({'mensaje': str(e)}, status=400)
    return JsonResponse({'mensaje': 'Metodo no permitido'}, status=405)

#El metodo del API DELETE para eliminar un producto
def eliminar_producto(request, id_producto):
    if request.method == 'DELETE':
        #Intentar eliminar el producto
        try:
            #Obtener la entidad/modelo a eliminar
            producto = get_object_or_404(Producto, id=id_producto)
            #Eliminar la entidad/modelo
            producto.delete()
            #Retornar una respuesta en formato JSON con un mensaje de exito
            return JsonResponse({'mensaje': 'Producto eliminado correctamente'}, status=200)
        except Exception as e:
            return JsonResponse({'mensaje': str(e)}, status=400)
    return JsonResponse({'mensaje': 'Metodo no permitido'}, status=405)

#Metodo que devuelva un producto en especifico
def obtener_producto(request, id_producto):
    if request.method == 'GET':
        #Intentar obtener el producto
        try:
            #Obtener la entidad/modelo a eliminar
            producto = get_object_or_404(Producto, id=id_producto)
            #Retornar una respuesta en formato JSON con un mensaje de exito
            return JsonResponse({'id':producto.id,'nombre': producto.nombre, 'precio': producto.precio, 'imagen': producto.imagen}, status=200)
        except Exception as e:
            return JsonResponse({'mensaje': str(e)}, status=400)
    return JsonResponse({'mensaje': 'Metodo no permitido'}, status=405)
