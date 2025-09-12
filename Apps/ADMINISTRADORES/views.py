from django.views.generic import TemplateView

# Create your views here.
class AdminView(TemplateView):
    template_name = 'administradores.html'
from django.views.generic import TemplateView
from .models import Administrador

class AdminView(TemplateView):
    template_name = 'administradores.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['administradores'] = Administrador.objects.all()
        return context