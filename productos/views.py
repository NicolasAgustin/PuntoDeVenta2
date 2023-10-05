from django.shortcuts import redirect, render
from productos.models import Producto
from productos.forms import AddProductoForm

# Create your views here.
def productos_view(request):
	# clientes = Cliente.objects.all()
	# form_editar = EditarClienteForm()
	productos = Producto.objects.all()
	form_add = AddProductoForm()
	context = {
		'productos': productos,
		'form_add': form_add
	}
	return render(request, 'productos.html', context)


def edit_producto(request):
	# if request.POST:
	# 	cliente=Cliente.objects.get(pk=request.POST.get('id_personal_editar'))
	# 	form=EditarClienteForm(
	# 		request.POST, request.FILES, instance= cliente)
	# 	if form.is_valid:
	# 		form.save()
	# return redirect('Clientes')
    pass


def add_producto_view(request):
	if request.POST:
		form=AddProductoForm(request.POST, request.FILES)
	if form.is_valid:
		try:
			form.save()
		except Exception as ex:
			# TODO: Agregar mensajes de error para el formulario
			# messages(request, "Error al guardar el Producto")
			return redirect('Productos')
	return redirect('Productos')


# class add_ventas(ListView):
#     template_name = 'add_ventas.html'
#     model = Egreso
