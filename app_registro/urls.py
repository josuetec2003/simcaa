from django.urls import path
from . import views

app_name = 'registro'

urlpatterns = [
    path('', views.index, name='index'),
    path('registrados/', views.registrados, name='registrados'),
    path('registrar/', views.registrar, name='registrar'),
    path('importar/', views.importar, name='importar'),
]
