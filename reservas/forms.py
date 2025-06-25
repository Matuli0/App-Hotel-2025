from django import forms
from .models import Reserva, Habitacion
from django.utils import timezone

class ReservaForm(forms.ModelForm):
    class Meta:
        model = Reserva
        fields = ['habitacion', 'pasajero', 'fecha_reserva']
        widgets = {
            'fecha_reserva': forms.DateTimeInput(attrs={'type': 'datetime-local'}),
        }

    def clean_fecha_reserva(self):
        fecha_reserva = self.cleaned_data.get('fecha_reserva')
        # Aquí puedes validar si la fecha de reserva está en el rango correcto.
        if fecha_reserva < timezone.now():
            raise forms.ValidationError("La fecha de reserva no puede ser en el pasado.")
        return fecha_reserva
