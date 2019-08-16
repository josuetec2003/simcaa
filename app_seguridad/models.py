from django.db import models
from django.contrib.auth.models import User

class TipoUsuario(models.Model):
	VALORES = (
		('registrador', 'Registrador'),
		('regalo', 'Regalo'),
	)
	descripcion = models.CharField(max_length=15, choices=VALORES)
	user = models.OneToOneField(User, on_delete=models.CASCADE)
