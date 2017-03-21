from django import forms
from apps.nacionalidad.models import Nacionalidad

class NacionalidadForm(forms.Form):
    nombre = forms.CharField(max_length=100, required=True),
    descripcion = forms.CharField(max_length=100, required=True),

    class Meta:

        model = Nacionalidad


        #campos a utilizar del modelo
        fields = [
            'nombre',
            'habilitado',
        ]


        #etiquetas en el formulario
        labels = {
            'nombre': 'Nombre',
            'habilitado': 'Habilitado',
        }


        widgets = {
            'nombre': forms.TextInput(attrs={'class':'form-control'}),
            'habilitado': forms.TextInput(attrs={'class':'form-control'}),
        }