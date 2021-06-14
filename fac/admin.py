from django.contrib import admin

from .models import Cliente, FacturaEnc, FacturaDet

class ClienteAdmin(admin.ModelAdmin):
    list_display = [
        'nombres',
        'apellidos',
        'numero_dni',
    ]

admin.site.register(Cliente, ClienteAdmin)
admin.site.register(FacturaEnc)
admin.site.register(FacturaDet)
