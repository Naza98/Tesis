from django import forms

from .models import Categoria, SubCategoria, Marca, Producto


class CategoriaForm(forms.ModelForm):
    class Meta:
        model=Categoria
        fields = ['descripcion','estado'] #campos que se van a cambiar
        labels = {'descripcion':"Descripción de la Categoría", #descripcion de la etiqueta
               "estado":"Estado"}
        widget={'descripcion': forms.TextInput} #tipo de elemento html

    def __init__(self, *args, **kwargs): 
        super().__init__(*args,**kwargs) 
        for field in iter(self.fields):  #recorrer todos los campos que se van a mostrar y que los itere
            self.fields[field].widget.attrs.update({
                'class':'form-control'
            })

class SubCategoriaForm(forms.ModelForm):
    categoria = forms.ModelChoiceField(
        queryset=Categoria.objects.filter(estado=True)
        .order_by('descripcion')
    )
    class Meta:
        model=SubCategoria
        fields = ['categoria','descripcion','estado']
        labels = {'descripcion':"Sub Categoría",
               "estado":"Estado"}
        widget={'descripcion': forms.TextInput}

    def __init__(self, *args, **kwargs):
        super().__init__(*args,**kwargs)
        for field in iter(self.fields):
            self.fields[field].widget.attrs.update({
                'class':'form-control'
            })
        self.fields['categoria'].empty_label =  "Seleccione Categoría"


class MarcaForm(forms.ModelForm):
    class Meta:
        model=Marca
        fields = ['descripcion','estado']
        labels= {'descripcion': "Descripción de la Marca",
                "estado":"Estado"}
        widget={'descripcion': forms.TextInput()}

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in iter(self.fields):
            self.fields[field].widget.attrs.update({
                'class': 'form-control'
            })

'''
class UMForm(forms.ModelForm):
    class Meta:
        model=UnidadMedida
        fields = ['descripcion','estado']
        labels= {'descripcion': "Descripción de la Marca",
                "estado":"Estado"}
        widget={'descripcion': forms.TextInput()}

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in iter(self.fields):
            self.fields[field].widget.attrs.update({
                'class': 'form-control'
            })
'''

class ProductoForm(forms.ModelForm):
    class Meta:
        model=Producto
        fields=[ 'nombre_producto', 'codigo','codigo_barra','descripcion','estado', \
                'precio','existencia','ultima_compra',
                'marca','subcategoria','foto']
        exclude = ['fm','uc','fc']
        widget={'nombre_producto': forms.TextInput()}

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in iter(self.fields):
            self.fields[field].widget.attrs.update({
                'class': 'form-control'
            })
        self.fields['ultima_compra'].widget.attrs['readonly'] = True
        self.fields['existencia'].widget.attrs['readonly'] = True