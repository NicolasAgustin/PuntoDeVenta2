
from pyexpat.errors import messages
from django.shortcuts import render, redirect

from clientes.models import Cliente
from clientes.forms import AddClienteForm, EditarClienteForm


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
			messages(request, "Error al guardar el cliente")
			return redirect('Clientes')
	return redirect('Clientes')


#TODO Al editar un cliente no se visualiza la informacion actual, pero si podes editarlo.
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