from .models import Categoria
from django import forms

class CategoriaForm(forms.ModelForm):
    class Meta: 
        model = Categoria
        fields = ['nombre', 'imagen']
        widgets = {
            'nombre': forms.TextInput(
                attrs = {
                    'class': 'form-input',
                    'placeholder': 'Ingrese el nombre de la categoria',
                    'style': 'width: 100%;'
                }
            ),
            'imagen': forms.URLInput(
                attrs = {
                    'class': 'form-control',
                    'placeholder': 'Ingrese la URL de la imagen de la categoria',
                    'style': 'width: 100%;'
                }
            )
        }
        labels = {
            'nombre': 'Nombre de la categoria',
            'imagen': 'URL de la imagen de la categoria'
        }
        error_messages = {
            'nombre': {
                'required': 'El campo nombre es obligatorio'
            },
            'imagen': {
                'required': 'El campo imagen es obligatorio'
            }
        }