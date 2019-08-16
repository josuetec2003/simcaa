from django.contrib.auth.forms import AuthenticationForm

class MyAuthForm(AuthenticationForm):
	def __init__(self, *args, **kwargs):
		super().__init__(*args, **kwargs)

		self.fields['username'].widget.attrs.update({'class': 'form-control form-control-lg', 'placeholder': 'Usuario'})
		self.fields['password'].widget.attrs.update({'class': 'form-control form-control-lg', 'placeholder': 'Contraseña'})

