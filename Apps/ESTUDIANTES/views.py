from django.shortcuts import render
from django.views.generic import TemplateView

# Create your views here.
class EstudiantesView(TemplateView):
    template_name = 'estudiantes.html'