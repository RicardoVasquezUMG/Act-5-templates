from django.contrib import admin
from django.urls import path,include
from Apps.ADMINISTRADORES import views

from .views import AdminView, CrearAdministradorView , EditarAdministradorView

app_name='adminis'
urlpatterns = [
    path('', AdminView.as_view(), name='adminapp'),
    path('crear/', CrearAdministradorView.as_view(), name='crear'),
    path('editar/<int:pk>/', EditarAdministradorView.as_view(), name='editar')
]

