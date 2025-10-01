from django.contrib import admin
from django.urls import path,include
from Apps.PUBLICACIONES import views
from .views import PubliView, CrearPublicacionView

app_name='publicaciones'
urlpatterns = [
    path('', PubliView.as_view(), name='publiapp'),
    path('crear/', CrearPublicacionView.as_view(), name='crear'),
    path('editar/<int:pk>/', views.EditarPublicacionView.as_view(), name='editar'),
]
