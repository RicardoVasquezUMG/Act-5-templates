from django.shortcuts import render
from django.views.generic import TemplateView
from .models import Estudiante

# Create your views here.
class EstudiantesView(TemplateView):
    template_name = 'estudiantes.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['estudiantes'] = Estudiante.objects.all()
        return context

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['estudiantes'] = Estudiante.objects.all()
        return context
    template_name = 'estudiantes.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['estudiantes'] = Estudiante.objects.all()
        return context