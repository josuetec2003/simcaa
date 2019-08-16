from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.contrib.auth import login, logout, authenticate
from django.urls import reverse
from .forms import MyAuthForm
from .models import TipoUsuario

def index(request):
	form = MyAuthForm()
	return render(request, 'seguridad/index.html', {'form': form})

def procesar_login(request):
	if request.method == 'POST':
		form = MyAuthForm(request=request, data=request.POST)

		if form.is_valid():
			username = form.cleaned_data.get('username')
			password = form.cleaned_data.get('password')

			user = authenticate(username = request.POST['username'], password = request.POST['password'])

			if user.is_active:
				login(request, user)

				if not user.is_superuser:
					request.session['tipou'] = TipoUsuario.objects.get(user = user).descripcion
				else:
					request.session['tipou'] = 'admin'


				return HttpResponseRedirect(reverse('registro:index'))
			else:
				return render(request, 'seguridad/index.html', {'form': form})	
		else:
			return render(request, 'seguridad/index.html', {'form': form})




def procesar_logout(request):
	logout(request)
	return HttpResponseRedirect('/')

