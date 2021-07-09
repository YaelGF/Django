from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse_lazy
from django.views.generic import TemplateView
from .forms import EmpleadoForm
from django.views.generic import DetailView
from .models import Empleado

# Create your views here.

class EmployeeImage(TemplateView):
    form = EmpleadoForm
    template_name = 'emp_image.html'

    def post (self, request, *args, **kwargs):
        form = EmpleadoForm(request.POST, request.FILES)
        if form.is_valid():
            obj = form.save()
            return HttpResponseRedirect(reverse_lazy('emp_image_display', kwargs = {'pk': obj.id}))

        
        context = self.get_context_data(form = form)
        return self.render_to_response(context)

    def get(self, request, *args, **kwargs):
        return self.post(request, *args, **kwargs)

class EmpImageDisplay(DetailView):
    model = Empleado
    template_name = 'emp_image_display.html'
    context_object_name = 'emp'
