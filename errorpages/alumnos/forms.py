from django import forms
from .models import Alumno

class AlumnoForm(forms.ModelForm):
    id = forms.CharField(widget=forms.HiddenInput(), required=False)  # Campo oculto

    class Meta:
        model = Alumno
        fields = ['id', 'nombre', 'edad', 'correo', 'matricula']

        widgets = {
            'nombre': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Nombre'}),
            'edad': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Edad'}),
            'correo': forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Correo Electrónico'}),
            'matricula': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Matrícula'}),
        }