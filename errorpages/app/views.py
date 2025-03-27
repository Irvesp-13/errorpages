from django.http import HttpResponse
from .utils import google_search
from django.shortcuts import render
from django.http import JsonResponse
from .models import ErrorLog

# Create your views here.

def index(request):
    return HttpResponse("<h1>Hola mundo</h1>")



def error_404_view(request, exception):
    render(request, '404.html', status=404)


def error_500_view(request, exception):
    render(request, '500.html', status=500)


def error(request, exception):
    return 7/0

def onepage(request):
    return render(request, 'onepage.html',status=200)

def prueba(request):
    #Como obtener información de un html?
    nombre = request.GET.get('nombre', '')
    edad = request.GET.get('edad', '')

    persona = {
        'nombre': nombre,
        'edad': edad,
        'descripcion': nombre + " - " + edad
    }

    persona2 = {
        'nombre': 'Javier',
        'edad': 25,
        'descripcion': nombre + " - " + edad
    }

    persona3 = {
        'nombre': 'Antonio',
        'edad': 30,
        'descripcion': nombre + " - " + edad
    }

    if (persona['nombre'] == 'Antonio'):
        persona['descripcion'] = 'Antonio es el mejor'

    print(persona['nombre'])
    conjunto=[persona, persona2, persona3]
    
    return render(
        request, 
        'prueba.html',
        {'objeto': persona, 'saludo': 'Hola mundo', 'personas': conjunto}
    )

def search_view(request):
    query = request.GET.get("q", "")
    results = []
    if query:
        data = google_search(query)
        results = data.get("items", [])

    return render(request, "search.html", {"results": results, "query": query})

def error_logs(request):
    return render(request, 'error_logs.html')

def get_error_logs(request):
    errors = ErrorLog.objects.values('id', 'codigo', 'mensaje', 'fecha')
    return JsonResponse({'data': list(errors)})
