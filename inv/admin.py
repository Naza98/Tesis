from django.contrib import admin

from .models import Categoria, SubCategoria, Marca, Producto, \
    TipoMovimiento, Movimiento, Motivo, Devolucion

class ProductoAdmin(admin.ModelAdmin):
    list_display = [
        'nombre_producto',
        'marca',
        'descripcion',
        'precio',
        'existencia',
        'ultima_compra',
        'subcategoria',
        'foto',
    ]



admin.site.register(Producto, ProductoAdmin)
admin.site.register(Categoria)
admin.site.register(SubCategoria)
admin.site.register(Marca)
admin.site.register(TipoMovimiento)
admin.site.register(Movimiento)
admin.site.register(Motivo)
admin.site.register(Devolucion)
