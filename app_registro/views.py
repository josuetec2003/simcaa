from django.http import JsonResponse
from django.shortcuts import render
from django.db.models import Q
from django.contrib.auth.decorators import login_required
from datetime import datetime
from .models import Participante

@login_required()
def index(request):
	request.session['page'] = 'registro'
	q = request.GET.get('q')

	if q:
		if request.session['tipou'] == 'registrador':
			participantes = Participante.objects.filter(
				Q(registrado=False) &
				(Q(nombre__startswith=q) | 
				Q(apellido__startswith=q) |
				Q(empresa__startswith=q) |
				Q(pais__startswith=q))
			)
		elif request.session['tipou'] == 'regalo':
			participantes = Participante.objects.filter(
				Q(registrado=True) & Q(obsequio=False) &
				(Q(nombre__startswith=q) | 
				Q(apellido__startswith=q) |
				Q(empresa__startswith=q) |
				Q(pais__startswith=q))
			)
		else:
			participantes = Participante.objects.filter(
				Q(nombre__startswith=q) | 
				Q(apellido__startswith=q) |
				Q(empresa__startswith=q) |
				Q(pais__startswith=q)
			)
	else:
		if request.session['tipou'] == 'regalo':
			participantes = Participante.objects.filter(registrado=True, obsequio=False)
		else:
			participantes = Participante.objects.filter(registrado=False)

	return render(request, 'registro/index.html', {'q': q, 'participantes': participantes})


@login_required()
def registrar(request):
	if request.is_ajax():
		accion = request.GET.get('accion')
		participante = Participante.objects.get(pk = request.GET.get('pid'))

		if accion == 'registrar':
			if participante.tipo_participante.tipo == 'Regular' and not participante.fecha_pago:
				m = f'No se puede registrar a {participante.nombre.upper()} {participante.apellido.upper()} ya que su pago está pendiente'
				exito = False
			else:
				participante.registrado = True
				participante.save()

				m = f'{participante.nombre} {participante.apellido} ha sido registrado en el evento'
				exito = True
				

			return JsonResponse({'mensaje': m, 'exito': exito})
		elif accion == 'pagar':
			try:
				pago = int(request.GET.get('pago'))

				participante.fecha_pago = datetime.now()
				participante.costo = pago
				participante.registrado = True
				participante.save()
				m = f'{participante.nombre} {participante.apellido} ha sido registrado en el evento'
				exito = True
			except:
				m = 'El monto de pago ingresado es incorrecto'
				exito = False
			

			return JsonResponse({'mensaje': m, 'exito': exito})

		elif accion == 'regalar':
			participante.obsequio = True
			participante.save()
			return JsonResponse({'mensaje': 'Obsequio registrado', 'exito': True})





@login_required()
def registrados(request):
	registrados = Participante.objects.filter(registrado = True)
	request.session['page'] = 'registrados'
	return render(request, 'registro/registrados.html', {'registrados': registrados})
