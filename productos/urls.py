from django.urls import path
from productos import views


urlpatterns = [
    path('', views.productos_view, name='Productos'),
    path('add_producto/', views.add_producto_view, name='AddProducto'),
    path("edit_producto/", views.edit_producto, name="EditProducto")
]
