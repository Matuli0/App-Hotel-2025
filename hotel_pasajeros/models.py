# hotel_pasajeros/models.py
from django.db import models

class Habitacion(models.Model):
    numero = models.CharField(max_length=10)
    capacidad = models.IntegerField()
    orientacion = models.CharField(max_length=20)

    def __str__(self):
        return f"Habitación {self.numero}"

class Pasajero(models.Model):
    nombre = models.CharField(max_length=100)
    rut = models.CharField(max_length=20, unique=True)

    def __str__(self):
        return self.nombre

class Reserva(models.Model):
    habitacion = models.ForeignKey(Habitacion, on_delete=models.CASCADE)
    pasajero = models.ForeignKey(Pasajero, on_delete=models.CASCADE)
    fecha_reserva = models.DateField()

    def __str__(self):
        return f"Reserva {self.id} - {self.pasajero.nombre} en Habitación {self.habitacion.numero}"
