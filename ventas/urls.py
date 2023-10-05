from django.urls import path
from ventas.views import ventas_view
from ventas import views

#TODO separar url de clientes y ventas 
urlpatterns = [
   path('', ventas_view, name='Ventas'), 
   # path('clientes/', clientes_view, name='Clientes'),
   # path('add_cliente/', add_cliente_view, name='AddCliente'),
   # path('edit_cliente/', edit_cliente_view, name='EditCliente'),
   # path('delete_cliente/', delete_cliente_view, name='DeleteCliente'),
   # path('add_venta/', views.add_ventas.as_view(), name='AddVenta'),
   # path('export/', views.export_pdf_view, name="ExportPDF" ),
   # path('export/<id>/<iva>', views.export_pdf_view, name="ExportPDF" ),
]
