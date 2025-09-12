from django.contrib import admin
from django.urls import path,include
from Apps.PUBLICACIONES import views
from .views import PubliView

app_name='publicaciones'
urlpatterns = [
    path('',PubliView.as_view(), name='publiapp')
]
