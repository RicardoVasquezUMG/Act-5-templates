from django.views.generic import TemplateView, CreateView
from django.urls import reverse_lazy
from .models import Publicacion
from .forms import PublicacionForm

class PubliView(TemplateView):
    template_name = 'publicaciones.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['publicaciones'] = Publicacion.objects.all()
        return context

class CrearPublicacionView(CreateView):
    model = Publicacion
    template_name = 'crear_publicacion.html'
    form_class = PublicacionForm
    success_url = reverse_lazy('publicaciones:publiapp')