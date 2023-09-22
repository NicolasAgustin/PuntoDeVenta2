from django import forms
from clientes.models import Cliente, Producto


class AddClienteForm(forms.ModelForm):
	class Meta:
		model=Cliente
		fields=('codigo', 'nombre', 'telefono')
		labels={
			'codigo': 'Código cliente: ',
			'nombre': 'Nombre cliente: ',
			'telefono': 'Telefono: (Contacto): '
		}


class EditarClienteForm(forms.ModelForm):

	codigo = forms.CharField(widget=forms.TextInput(attrs={'type': 'text', 'id': 'codigo_editar'}))
	nombre = forms.CharField(widget=forms.TextInput(attrs={'id': 'nombre_editar'}))
	telefono = forms.CharField(widget=forms.TextInput(attrs={'id': 'telefono_editar'}))

	class Meta:
		model=Cliente
		fields=('codigo', 'nombre', 'telefono')
		labels={
			'codigo': 'Código cliente: ',
			'nombre': 'Nombre cliente: ',
			'telefono': 'Telefono: (Contacto): '
		}


class AddProductoForm(forms.ModelForm):
	class Meta:
		model=Producto
		fields=('codigo', 'descripcion', 'imagen', 'costo', 'precio', 'cantidad')
		labels={
			'codigo': 'Cód Barras: ',
			'descripcion': 'Descripcion de producto: ',
			'imagen': 'Imagen: ',
			'costo': 'Costo $: ',
			'precio': 'Precio $: ',
			'cantidad': 'Cantidad: ',
			}
	
#class EditarClienteForm(forms.ModelForm):
	#class Meta:
		#imagen=forms.ImageField()
		#model=Cliente
		#fields=('codigo','nombre', 'telefono', 'imagen')
		#labels={
		#	'codigo': 'Código: ',
		#	'telefono': 'Telefono: ',
		#	'imagen': 'Imagen: ',
		#	'nombre': 'Descripcion: '
		#}
		
		#widgets={
		#	'codigo': forms.TextInput(attrs={'type: 'text', 'id': 'codigo_editar'}),
		#	'nombre': forms.TextInput(attrs={'id': 'nombre_editar'}),
		#	'telefono': forms.TextInput(attrs={'id': 'telefono_editar'}),
		#}


