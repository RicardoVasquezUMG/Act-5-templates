from django.views.generic import TemplateView

class PubliView(TemplateView):
    template_name = 'publicaciones.html'
from django.views.generic import TemplateView
from .models import Publicacion

class PubliView(TemplateView):
    template_name = 'publicaciones.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['publicaciones'] = Publicacion.objects.all()
        return context