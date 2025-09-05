from django.contrib import admin
from django.urls import path,include
from Apps.ADMINISTRADORES import views
from .views import AdminView

app_name='adminis'
urlpatterns = [
    path('',AdminView.as_view(), name='adminapp')
]

