from django.urls import path
from clientes.views import clientes_view

urlpatterns = [
    path("", clientes_view, name="Clientes"),
]
