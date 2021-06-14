from django.contrib import admin
from .models import ComprasDet, ComprasEnc, Proveedor

admin.site.register(ComprasEnc)
admin.site.register(ComprasDet)
admin.site.register(Proveedor)