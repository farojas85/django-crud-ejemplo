from django.shortcuts import render
from django.views import generic
from django.urls import reverse_lazy
from .models import Estudiante
from .forms import EstudianteForm

# Create your views here.
class EstudianteView(generic.ListView):
    paginate_by=5
    model = Estudiante
    context_object_name = 'estudiantes'
    template_name="estudiante/inicio.html"

class EstudianteNew(generic.CreateView):
    model= Estudiante
    template_name="estudiante/create.html"
    form_class=EstudianteForm
    success_url = reverse_lazy('estudiante:estudiante-inicio')

class EstudianteEdit(generic.UpdateView):
    model=Estudiante
    fields=['dni','nombres','apellidos']
    template_name="estudiante/edit.html"
    success_url = reverse_lazy('estudiante:estudiante-inicio')

class EstuanteDelete(generic.DeleteView):
    model=Estudiante
    success_url = reverse_lazy('estudiante:estudiante-inicio')

