from django.urls import path
from . import views

urlpatterns = [
    path("", views.getAPOD, name="getAPOD")
]