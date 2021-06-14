from typing import Pattern
from django import forms
from django.forms import ValidationError
from django.forms.widgets import NumberInput
from .models import Cliente


class ClienteForm(forms.ModelForm):

    fecha_nacimiento = forms.DateField(required=True,
    widget=NumberInput(attrs=({'type' : 'date'})))

    celular = forms.IntegerField(required=True)

    def clean_celular(self):
        celular = self.cleaned_data["celular"]
        existe = Cliente.objects.filter(celular=celular).exists()

        if existe:
            raise ValidationError("Este número de celular ya existe")
        return celular

    numero_dni = forms.IntegerField(required=True,
        widget=forms.NumberInput(attrs=({'placeholder':'Ingrese el número sin puntos, ni espacios'})))

    def clean_numero_dni(self):
        numero_dni = self.cleaned_data['numero_dni']
        if numero_dni < 0:
            raise ValidationError("Este número no puede tener valores negativos")
        return numero_dni      

    class Meta:
        model=Cliente
        fields=['nombres','apellidos', 'tipo_documento' ,'numero_dni', 'fecha_nacimiento', 'sexo','tipo',
            'celular', 'email','estado']
        exclude = ['um','fm','uc','fc']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in iter(self.fields):
            self.fields[field].widget.attrs.update({
                'class': 'form-control'
            })