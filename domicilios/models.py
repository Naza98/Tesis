from django.db import models

#Para los signals
from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver
from fac.models import Cliente


'''---------------------- Domicilios ---------------------- '''

class Provincia(models.Model):

    nombre_provincia = models.CharField(max_length=300, null=False, blank=False)

    def __str__(self):
        return self.nombre

    class Meta:

        db_table = 'Provincias'
        verbose_name = 'Provincia'
        verbose_name_plural = 'Provincias'



class Localidad(models.Model):

    nombre_localidad = models.CharField(max_length=300, null=False, blank=False)
    provincia = models.ForeignKey(Provincia, null=False, blank=False, on_delete=models.CASCADE)


    def __str__(self):
        return str(self.nombre)

    class Meta:

        db_table = 'Localidades'
        verbose_name = 'Localidad'
        verbose_name_plural = 'Localidades'


class Barrio(models.Model):

    localidad = models.ForeignKey(Localidad, null=False, blank=False,
    on_delete=models.CASCADE)
    nombre_barrio = models.CharField(max_length=300, null=False, blank=False)

    def __str__(self):
        return str(self.nombre)

    class Meta:

        db_table = 'Barrios'
        verbose_name = 'Barrio'
        verbose_name_plural = 'Barrios'

class Domicilio(models.Model):

    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    barrio = models.ForeignKey(Barrio, null=True, blank=True, on_delete=models.CASCADE)
    calle = models.CharField(max_length=300, blank=True, null=True)
    altura = models.CharField(max_length=300, blank=True, null=True)
    manzana = models.CharField(max_length=300, blank=True, null=True)
    departamento = models.CharField(max_length=300, blank=True, null=True)
    piso = models.CharField(max_length=300, blank=True, null=True)
    observacion = models.CharField(max_length=600, blank=True, null=True)
    # Agregar casa
    # para realizar bajas logicas
    baja = models.BooleanField(default=False)
    fecha = models.DateField(blank=True, null=True)

    class Meta:
        db_table = 'Domicilios'    

'''---------------------- Domicilios ---------------------- '''