from django.urls import path
from ventas.views import ventas_view
from clientes.views import clientes_view, add_cliente_view, edit_cliente_view, delete_cliente_view, productos_view, add_producto_view


#TODO separar url de clientes y ventas 
urlpatterns = [
   path('', ventas_view, name='Ventas'), 
   path('clientes/', clientes_view, name='Clientes'),
   path('add_cliente/', add_cliente_view, name='AddCliente'),
   path('edit_cliente/', edit_cliente_view, name='EditCliente'),
   path('delete_cliente/', delete_cliente_view, name='DeleteCliente'),
   path('productos/', productos_view, name='Productos'),
   path('add_producto/', add_producto_view, name='AddProducto'),
]
