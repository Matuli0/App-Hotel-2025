from django.db import models
from django.conf import settings
from django.utils import timezone
from django.contrib.auth.models import AbstractUser

class Habitacion(models.Model):
    numero      = models.CharField("Número", max_length=10, unique=True)
    capacidad   = models.PositiveIntegerField("Capacidad de pasajeros")
    orientacion = models.CharField("Orientación", max_length=50)

    def __str__(self):
        return f"Habitación {self.numero} ({self.capacidad} pax)"

class Pasajero(models.Model):
    nombre = models.CharField("Nombre", max_length=100)
    rut    = models.CharField("RUT",    max_length=12, unique=True)

    def __str__(self):
        return f"{self.nombre} ({self.rut})"

class Reserva(models.Model):
    habitacion       = models.ForeignKey(Habitacion, on_delete=models.CASCADE, related_name="reservas")
    pasajero         = models.ForeignKey(Pasajero,   on_delete=models.CASCADE, related_name="reservas")
    fecha_asignacion = models.DateTimeField(auto_now_add=True)
    costo_total      = models.PositiveIntegerField(editable=False)

    COSTO_POR_PAX = 20000

    def save(self, *args, **kwargs):
        self.costo_total = self.COSTO_POR_PAX
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.pasajero} → Hab {self.habitacion.numero}"

class CustomUser(AbstractUser):
    is_admin = models.BooleanField(default=False)  # Marca a los administradores
    
    # Proporcionamos un `related_name` para evitar el conflicto
    groups = models.ManyToManyField(
        'auth.Group',
        related_name='customuser_set',  # Cambiar el related_name
        blank=True
    )
    user_permissions = models.ManyToManyField(
        'auth.Permission',
        related_name='customuser_permissions_set',  # Cambiar el related_name
        blank=True
    )