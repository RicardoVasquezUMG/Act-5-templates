from django.contrib import admin
from django.urls import path,include
from Apps.HOME import views
from .views import HomeView

app_name='home'
urlpatterns = [
    path('',HomeView.as_view(), name='homeapp')
]
