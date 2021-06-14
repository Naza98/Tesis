from django.shortcuts import render

from rest_framework.views import APIView
from rest_framework.response import Response
from django.shortcuts import get_object_or_404

from .serializers import ProductoSerializer
from inv.models import Producto

from django.db.models import Q

class ProductoList(APIView):
    def get(self,request):
        prod = Producto.objects.all()
        data = ProductoSerializer(prod,many=True).data #El many lo que hace es averiguar si dentro de la data, va mas de un registro
        return Response(data)


class ProductoDetalle(APIView):
    def get(self,request, codigo):
        prod = get_object_or_404(Producto,Q(codigo=codigo)|Q(codigo_barra=codigo)) #Que busque el producto en el modelo producto, que busque el codigo que se le va a pasar. Codigo o codigo barra
        data = ProductoSerializer(prod).data
        return Response(data)
