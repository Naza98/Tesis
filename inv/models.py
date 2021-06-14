from decouple import AutoConfig
from django.db import models

from bases.models import ClaseModelo


'''

Aplicacion de inventario

'''

class Categoria(ClaseModelo):
    descripcion = models.CharField(
        max_length=100,
        help_text='Descripción de la Categoría',
        unique=True
    )

    def __str__(self):
        return '{}'.format(self.descripcion)

    def save(self):
        self.descripcion = self.descripcion.upper() #Colocar todas las letras en mayuscula
        super(Categoria, self).save() #Guardar

    class Meta:
        verbose_name_plural= "Categorias"


class SubCategoria(ClaseModelo):
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE)
    descripcion = models.CharField(
        max_length=100,
        help_text='Descripción de la Categoría'
    )

    def __str__(self):
        return '{}:{}'.format(self.categoria.descripcion,self.descripcion)
    
    def save(self):
        self.descripcion = self.descripcion.upper()
        super(SubCategoria, self).save()

    class Meta:
        verbose_name_plural= "Sub Categorias"
        unique_together = ('categoria','descripcion')


class Marca(ClaseModelo):
    descripcion = models.CharField(
        max_length=100,
        help_text='Descripción de la Marca',
        unique=True
    )

    def __str__(self):
        return '{}'.format(self.descripcion)

    def save(self):
        self.descripcion = self.descripcion.upper()
        super(Marca, self).save()

    class Meta:
        verbose_name_plural = "Marca"

'''
class UnidadMedida(ClaseModelo):
    descripcion = models.CharField(
        max_length=100,
        help_text='Descripción de la Unidad Medida',
        unique=True
    )

    def __str__(self):
        return '{}'.format(self.descripcion)

    def save(self):
        self.descripcion = self.descripcion.upper()
        super(UnidadMedida, self).save()

    class Meta:
        verbose_name_plural = "Unidades de Medida"
'''

class Producto(ClaseModelo):
    codigo = models.CharField(
        max_length=20,
        unique=True, auto_created=True
    )
    nombre_producto = models.CharField(max_length=300)
    codigo_barra = models.CharField(max_length=50, auto_created=True)
    descripcion = models.CharField(max_length=300)
    precio = models.FloatField(default=0)
    existencia = models.IntegerField(default=0)
    ultima_compra = models.DateField(null=True, blank=True)

    marca = models.ForeignKey(Marca, on_delete=models.CASCADE)
    #unidad_medida = models.ForeignKey(UnidadMedida, on_delete=models.CASCADE)
    subcategoria = models.ForeignKey(SubCategoria, on_delete=models.CASCADE)
    foto = models.ImageField(upload_to="images/",null=True,blank=True)

    def __str__(self):
        return '{}'.format(self.nombre_producto)
    
    def save(self):
        self.nombre_producto = self.nombre_producto.upper()
        super(Producto,self).save()
    
    class Meta:
        verbose_name_plural = "Productos"
        unique_together = ('codigo','codigo_barra')



class TipoMovimiento(models.Model):
    '''
    alta, baja, compra, venta, ajuste_incremento, ajuste_disminucion
    '''
    descripcion = models.CharField(max_length=300, null=False, blank=False)

    class Meta:
        verbose_name = 'Tipo de movimiento'
        verbose_name_plural = 'Tipo de movimientos'
        db_table = 'Tipo de movimientos'


class Movimiento(models.Model):

    producto = models.ForeignKey(Producto, null=False, blank=False, on_delete=models.CASCADE)
    tipo_movimiento = models.ForeignKey(TipoMovimiento, null=False, blank=False, on_delete=models.CASCADE)
    fecha = models.DateField(null=True, blank=True)
    cantidad = models.IntegerField(null=True, blank=True)

    class Meta:
        verbose_name = 'Historial de precios de productos'
        verbose_name_plural = 'Historial de precios de productos'
        db_table = 'Historial de precios de productos'


class Motivo(models.Model):
 
    descripcion = models.CharField(max_length=100, help_text='Descripción del motivo', unique=True )

    def __str__(self):
        return '{}'.format(self.descripcion)
    
    def save(self):
        self.descripcion = self.descripcion.upper()
        super(Producto,self).save()
    
    class Meta:
        verbose_name_plural = "Motivos"



class Devolucion(models.Model):

    producto = models.ForeignKey(Producto, null=False, blank=False, on_delete=models.CASCADE)
    moviento = models.ForeignKey(Movimiento, null=False, blank=False, on_delete=models.CASCADE)
    motivo = models.ForeignKey(Motivo, null=False, blank=False, on_delete=models.CASCADE)
    fecha = models.DateField(null=True, blank=True)
    cantidad = models.IntegerField(null=False, blank=False)

    class Meta:
        verbose_name_plural = 'Devoluciones'
        db_table = 'Devoluciones'
