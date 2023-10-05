from django import forms
from productos.models import Producto


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