from django.shortcuts import render


# Create your views here.
def ventas_view(request):
	num_ventas=156
	context={
		'num_ventas': num_ventas
	}
	return render(request, 'ventas.html',context)


