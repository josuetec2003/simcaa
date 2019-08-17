from django.http import JsonResponse, HttpResponse
from django.shortcuts import render
from django.db.models import Q
from django.contrib.auth.decorators import login_required
from datetime import datetime
from .models import Participante, TipoParticipante
from django import forms
import django_excel as excel

class UploadFileForm(forms.Form):
	flListado = forms.FileField()

@login_required()
def importar(request):
	if request.method == 'POST':
		#vamos a importar el excel
		form = UploadFileForm(request.POST, request.FILES)
		def choice_func(row):
			print (row)
			print (row[14])
			q = TipoParticipante.objects.filter(tipo=row[14])[0]
			row[14] = q
			return row

		if form.is_valid():
			#filehandle = request.FILES['flListado']
			#return excel.make_response(filehandle.get_sheet(), "csv", file_name="download")
			#request.FILES['flListado'].save_book_to_database(
			#	models=[Participante],
			#	initializers=[None],
			#	mapdicts[['nombre', 'apellido', 'acta_estudiante', 'empresa', 'cargo', 'titulo', 'pais', 'correo', 'telefono', 'movil', 'fecha_inscripcion', 'costo', 'fecha_pago', 'observaciones', 'tipo_participante', 'registrado', 'obsequio',],]
			#)
			request.FILES['flListado'].save_to_database(
				name_columns_by_row = 2,
				model = Participante,
				initializer = choice_func,
				mapdict = ['nombre', 'apellido', 'acta_estudiante', 'empresa', 'cargo', 'titulo', 'pais', 'correo', 'telefono', 'movil', 'fecha_inscripcion', 'costo', 'fecha_pago', 'observaciones', 'tipo_participante', 'registrado', 'obsequio']
			)
			return HttpResponse('Hemos importado con exito el listado!!!!!')
		else:
			return HttpResponse('Ha ocurrido un error al importar el listado... :(')
	else:
		#no importamos nada, sino que mostramos el form.
		request.session['page'] = 'importar'
		return render(request, 'registro/importar.html', {})

@login_required()
def index(request):
	request.session['page'] = 'registro'
	q = request.GET.get('q')

	if q:
		if request.session['tipou'] == 'registrador':
			participantes = Participante.objects.filter(
				Q(registrado=False) &
				(Q(nombre__contains=q) |
				Q(empresa__contains=q) |
				Q(pais__contains=q))
			)
		elif request.session['tipou'] == 'regalo':
			participantes = Participante.objects.filter(
				Q(registrado=True) & Q(obsequio=False) &
				(Q(nombre__contains=q) |
				Q(empresa__contains=q) |
				Q(pais__contains=q))
			)
		else:
			participantes = Participante.objects.filter(
				Q(nombre__contains=q) |
				Q(empresa__contains=q) |
				Q(pais__contains=q)
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
				m = f'No se puede registrar a {participante.nombre.upper()} ya que su pago está pendiente'
				exito = False
			else:
				participante.registrado = True
				participante.save()

				m = f'{participante.nombre} ha sido registrado en el evento'
				exito = True

			return JsonResponse({'mensaje': m, 'exito': exito})
		elif accion == 'pagar':
			try:
				pago = int(request.GET.get('pago'))

				participante.fecha_pago = datetime.now()
				participante.costo = pago
				participante.registrado = True
				participante.save()
				m = f'{participante.nombre} ha sido registrado en el evento'
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
