from django.db import models

#Para los signals
from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver
from django.db.models import Sum

from bases.models import ClaseModelo
from inv.models import Producto

class Proveedor(ClaseModelo):
    descripcion=models.CharField(
        max_length=100,
        unique=True
        )
    direccion=models.CharField(
        max_length=250,
        null=True, blank=True
        )
    contacto=models.CharField(
        max_length=100
    )
    telefono=models.CharField(
        max_length=10,
        null=True, blank=True
    )
    email=models.CharField(
        max_length=250,
        null=True, blank=True
    )

    def __str__(self):
        return '{}'.format(self.descripcion)

    def save(self):
        self.descripcion = self.descripcion.upper()
        super(Proveedor, self).save()

    class Meta:
        verbose_name_plural = "Proveedores"


class ComprasEnc(ClaseModelo):
    fecha_compra=models.DateField(null=True,blank=True)
    observacion=models.TextField(blank=True,null=True)
    no_factura=models.PositiveIntegerField(unique=True)
    fecha_factura=models.DateField()
    sub_total=models.FloatField(default=0)
    descuento=models.FloatField(default=0)
    total=models.FloatField(default=0)

    proveedor=models.ForeignKey(Proveedor,on_delete=models.CASCADE)
    
    def __str__(self):
        return '{}'.format(self.observacion)

    def save(self):
        self.observacion = self.observacion.upper()
        if self.total == None  or self.descuento == None:
            self.sub_total = 0
            self.descuento = 0
            
        self.total = self.sub_total - self.descuento
        super(ComprasEnc,self).save()

    class Meta:
        verbose_name_plural = "Encabezado Compras"
        verbose_name="Encabezado Compra"

class ComprasDet(ClaseModelo):
    compra=models.ForeignKey(ComprasEnc,on_delete=models.CASCADE)
    producto=models.ForeignKey(Producto,on_delete=models.CASCADE)
    cantidad=models.BigIntegerField(default=0)
    precio_prv=models.FloatField(default=0)
    sub_total=models.FloatField(default=0)
    descuento=models.FloatField(default=0)
    total=models.FloatField(default=0)
    costo=models.FloatField(default=0)

    def __str__(self):
        return '{}'.format(self.producto)

    def save(self):
        self.sub_total = float(float(int(self.cantidad)) * float(self.precio_prv)) #cantidad * precio = subtotal
        self.total = self.sub_total - float(self.descuento)
        super(ComprasDet, self).save()
    
    class Meta:
        verbose_name_plural = "Detalles Compras"
        verbose_name="Detalle Compra"



@receiver(post_delete, sender=ComprasDet)    #despues de borrar, modelo a vigilar. El decorador de la funcion que se va a ejecutar despues de que ocurra lo que tiene como parametros
def detalle_compra_borrar(sender,instance, **kwargs): #Recibe el sender(modelo), una instancia(objeto que se esta eliminando), recuperamos
    id_producto = instance.producto.id #el id del producto y 
    id_compra = instance.compra.id     #id de la compra

    enc = ComprasEnc.objects.filter(pk=id_compra).first() #filtar la compra y actualizar totales. filtar que su Primary key = id de la compra. first(el primero)
    if enc: #Si eso existe 
        sub_total = ComprasDet.objects.filter(compra=id_compra).aggregate(Sum('sub_total')) 
        descuento = ComprasDet.objects.filter(compra=id_compra).aggregate(Sum('descuento')) 
        enc.sub_total=sub_total['sub_total__sum']                                           #}SE ACTUALIZAN VALORES NUEVOS
        enc.descuento=descuento['descuento__sum']                                           #}
        enc.save()
    
    prod=Producto.objects.filter(pk=id_producto).first() #Se busca el producto, donde su pk=id_prodcuto
    if prod: #si producto existe
        cantidad = int(prod.existencia) - int(instance.cantidad) 
        prod.existencia = cantidad
        prod.save()


@receiver(post_save, sender=ComprasDet)
def detalle_compra_guardar(sender,instance,**kwargs):
    id_producto = instance.producto.id
    fecha_compra=instance.compra.fecha_compra

    prod=Producto.objects.filter(pk=id_producto).first()
    if prod:
        cantidad = int(prod.existencia) + int(instance.cantidad)
        prod.existencia = cantidad
        prod.ultima_compra=fecha_compra
        prod.save()


