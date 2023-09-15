from django.shortcuts import render, redirect

from clientes.models import Cliente, Producto
from clientes.forms import AddClienteForm, EditarClienteForm, AddProductoForm


def clientes_view(request):
	clientes = Cliente.objects.all()
	form_personal = AddClienteForm()
	form_editar = EditarClienteForm()

	context = {
		'clientes': clientes,
		'form_personal': form_personal,
		'form_editar': form_editar
	}
	return render(request, 'clientes.html', context)

def add_cliente_view(request):
	if request.POST:
		form=AddClienteForm(request.POST, request.FILES)
	if form.is_valid:
		try:
			form.save()
		except:
			# messages(request, "Error al guardar el cliente")
			return redirect('Clientes')
	return redirect('Clientes')


def edit_cliente_view(request):
	if request.POST:
		cliente=Cliente.objects.get(pk=request.POST.get('id_personal_editar'))
		form=EditarClienteForm(
			request.POST, request.FILES, instance= cliente)
		if form.is_valid:
			form.save()
	return redirect('Clientes')


def delete_cliente_view(request):
	if request.POST:
		cliente=Cliente.objects.get(pk=request.POST.get('id_personal_eliminar'))
		cliente.delete()
	return redirect('Clientes')

def productos_view(request):
	# clientes = Cliente.objects.all()
	# form_editar = EditarClienteForm()
	productos = Producto.objects.all()
	form_add = AddProductoForm()
	context = {
		'productos':productos,
		'form_add':form_add
	}
	return render(request, 'productos.html', context)

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
