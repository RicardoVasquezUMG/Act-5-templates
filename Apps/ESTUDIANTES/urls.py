from django.contrib import admin
from django.urls import path,include
from Apps.ESTUDIANTES import views
from .views import EstudiantesView

app_name='student'
urlpatterns = [
    path('',EstudiantesView.as_view(), name='Estudiantesapp')
]