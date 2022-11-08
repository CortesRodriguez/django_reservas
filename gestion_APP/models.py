from django.db import models


opcion = estado = [
 [0, "Reservado"],
 [1,"Completado"],
 [2,"Anulado"],
 [3,"No Asistens"]
]
# Create your models here.
class Reserva(models.Model):
    nombre = models.CharField(max_length=30)
    telefono = models.IntegerField()
    fecha = models.DateField()
    hora = models.TimeField()
    cantidad_personas= models.IntegerField()
    estado = models.IntegerField(choices= opcion)
    observacion = models.CharField(max_length=100)
