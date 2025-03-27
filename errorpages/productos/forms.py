#Vamos a crear formularios para cada modelo de la app/modulo 
from .models import Producto
from django import forms

#Crear una clase por cada formulario que necesitemos 
class ProductoForm(forms.ModelForm):
    #Definir los metadatos del form class Meta
    class Meta:
        #Perzonalizar el formulario 
        #1. Definir el modelo al que pertenece el formulario
        model = Producto
        #2. Definir los campos que se van a mostrar en el formulario
        fields = ['nombre', 'precio', 'imagen', 'proveedor']
        #3. Atributos de las etiquetas (Widgets)
        widgets = {
            'nombre': forms.TextInput(
                attrs = {
                    'class': 'form-input',
                    'placeholder': 'Ingrese el nombre del producto'
                }
            ),
            'precio': forms.NumberInput(
                attrs = {
                    'class': 'form-control',
                    'placeholder': 'Ingrese el precio del producto'
                }
            ),
            'imagen': forms.URLInput(
                attrs = {
                    'class': 'form-control',
                    'placeholder': 'Ingrese la URL de la imagen del producto'
                }
            ),
            'proveedor': forms.Select(
                attrs = {
                    'class': 'form-control',
                    'placeholder': 'Ingrese el proveedor del producto'
                }
            ),
        }

        #4. Personalizar las etiquetas (o los textos que salen a lado de los campos)
        labels = {
            'nombre': 'Nombre del producto',
            'precio': 'Precio del producto',
            'imagen': 'URL de la imagen del producto'
        }

        #5. Personalizar los mensajes de error
        error_messages = {
            'nombre': {
                'required': 'El campo nombre es obligatorio'
            },
            'precio': {
                'required': 'El campo precio es obligatorio'
            },
            'imagen': {
                'required': 'El campo imagen es obligatorio'
            }
        }
