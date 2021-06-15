import datetime
from django.shortcuts import redirect, render, HttpResponseRedirect
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib import messages
from django.http import JsonResponse

from django.views.generic import CreateView, UpdateView

from .models import Provincia, Localidad, Barrio, Domicilio
from .models import Domicilio
from .forms import *
from fac.models import Cliente



class DomicilioCreateView(SuccessMessageMixin, CreateView):

    model = Domicilio
    form_class = DomicilioForm
    template_name = 'domicilio_form.html'

    def get_context_data(self, **kwargs):

        context = super().get_context_data(**kwargs)

        context['id_cliente'] = self.kwargs['id']
        context['domicilios'] = Domicilio.objects.filter(cliente__id=self.kwargs['id'])
        if Cliente.objects.filter(id=self.kwargs['id']).exists():
            context['module_father'] = 'clientes'

        context['provincia'] = Provincia.objects.all()
        context['localidad'] = Localidad.objects.all()
        context['barrio'] = Barrio.objects.all()
        return context

    def post(self, request, *args, **kwargs):

        domicilio_form = DomicilioForm(data=self.request.POST) #recibe por post los datos del cliente
        domicilio_form.data._mutable = True
        domicilio_form.data['cliente'] = self.kwargs['id'] #id de la persona
        domicilio_form.data._mutable = False
        if domicilio_form.is_valid(): #validacion del formulario
            domicilio_form.save() #si los datos son validos, se guardan
            messages.success(request, 'El domicilio se agregó con éxito')
            return HttpResponseRedirect('/domicilios/alta/%s' %
                                        self.kwargs['id'])
        else:
            messages.error(request, 'Existen errores en el formulario') #sino, mensaje de error y redireccion al formulario nuevamente
            return render(request, 'domicilio_form.html', {
                'form': domicilio_form, 'id': self.kwargs['id']})

'''
class DomicilioDeleteView(DeleteView):
    
    template_name = 'domicilio_confirm_delete.html'
    model = Domicilio
    success_url = '/domicilios/alta'

    def delete(self, request, *args, **kwargs):

        messages.error(request, 'El domicilio se eliminó correctamente')
        super(DomicilioDeleteView, self).delete(request, *args, **kwargs)
        #Domicilio.objects.get(pk=kwargs['pk']).delete()
        return HttpResponseRedirect('/domicilios/alta/' + str(kwargs['id']))
'''

def eliminar_domicilio(request, id):
    domicilio = Domicilio.objects.get(pk=id)
    domicilio.baja = True
    domicilio.fecha_baja = datetime.datetime.now().date()
    domicilio.save()
    messages.success(request, "El domicilio se eliminó correctamente")
    return redirect(to="/clientes/listado")


class DomicilioUpdateView(UpdateView):

    template_name = 'domicilio_form.html'
    model = Domicilio
    form_class = DomicilioForm
    success_url = '/clientes/listado'
    success_message = 'El domicilio fue actualizado con éxito'

    def get_context_data(self, **kwargs):

        context = super().get_context_data(**kwargs)

        context['id_domicilio'] = self.kwargs['pk']
        context['id_provincia'] = self.kwargs['pk']
        context['id_localidad'] = self.kwargs['pk']
        context['id_barrio'] = self.kwargs['pk']

        return context

  