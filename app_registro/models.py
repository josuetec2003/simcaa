from django.db import models

class TipoParticipante(models.Model):
	tipo = models.CharField(max_length=40)

	def __str__(self):
		return self.tipo


class Participante(models.Model):
	nombre 			= models.CharField(max_length=25)
	apellido 		= models.CharField(max_length=25)
	acta_estudiante = models.CharField(max_length=30, null=True, blank=True)
	empresa 		= models.CharField(max_length=35, null=True, blank=True)
	cargo 			= models.CharField(max_length=50, null=True, blank=True)
	titulo 			= models.CharField(max_length=50, null=True, blank=True)
	pais 			= models.CharField(max_length=40, null=True, blank=True)
	correo 			= models.EmailField(null=True, blank=True)
	telefono 		= models.CharField(max_length=15, null=True, blank=True)
	movil 			= models.CharField(max_length=15, null=True, blank=True)
	fecha_inscripcion = models.DateField()
	costo 			= models.IntegerField(null=True, blank=True)
	fecha_pago 		= models.DateTimeField(null=True, blank=True)
	observaciones 	= models.TextField(null=True, blank=True)
	tipo_participante = models.ForeignKey(TipoParticipante, on_delete=models.SET_NULL, null=True)
	registrado		= models.BooleanField(default=False)
	obsequio		= models.BooleanField(default=False)


	def __str__(self):
		return f'{self.nombre} {self.apellido}'

