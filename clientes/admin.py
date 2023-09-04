from django.contrib import admin
from clientes.models import Cliente, Producto

# Register your models here.
class ClienteAdmin(admin.ModelAdmin):
	list_display=('nombre', 'telefono', 'codigo')
	search_fields=['nombre']
	readonly_fields=('created','updated')
	filter_horizontal= ()
	list_filter=()
	fieldsets=()

admin.site.register(Cliente, ClienteAdmin)

class ProductoAdmin(admin.ModelAdmin):
	list_display=('descripcion', 'cantidad', 'costo')
	search_fields=['descripcion']
	readonly_fields=('created', 'updated')
	filter_horizontal= ()
	list_filter=()
	fieldsets=()

admin.site.register(Producto, ProductoAdmin)