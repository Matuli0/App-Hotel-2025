# hotel_pasajeros/views.py
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from .models import Habitacion, Pasajero, Reserva

# — Habitaciones
class HabitacionListView(ListView):
    model = Habitacion
    template_name = "reservas/habitacion_list.html"  # Asegúrate de que esta plantilla exista

class HabitacionCreateView(CreateView):
    model = Habitacion
    fields = ["numero", "capacidad", "orientacion"]
    success_url = '/habitaciones/'  # Redirige después de crear
    template_name = "reservas/habitacion_form.html"

class HabitacionUpdateView(UpdateView):
    model = Habitacion
    fields = ["capacidad", "orientacion"]
    success_url = '/habitaciones/'  # Redirige después de actualizar
    template_name = "reservas/habitacion_form.html"

class HabitacionDeleteView(DeleteView):
    model = Habitacion
    success_url = '/habitaciones/'  # Redirige después de eliminar
    template_name = "reservas/habitacion_confirm_delete.html"

# — Pasajeros
class PasajeroListView(ListView):
    model = Pasajero
    template_name = "reservas/pasajero_list.html"

class PasajeroCreateView(CreateView):
    model = Pasajero
    fields = ["nombre", "rut"]
    success_url = '/pasajeros/'  # Redirige después de crear
    template_name = "reservas/pasajero_form.html"

class PasajeroUpdateView(UpdateView):
    model = Pasajero
    fields = ["nombre", "rut"]
    success_url = '/pasajeros/'  # Redirige después de actualizar
    template_name = "reservas/pasajero_form.html"

class PasajeroDeleteView(DeleteView):
    model = Pasajero
    success_url = '/pasajeros/'  # Redirige después de eliminar
    template_name = "reservas/pasajero_confirm_delete.html"

# — Reservas
class ReservaListView(ListView):
    model = Reserva
    template_name = "reservas/reserva_list.html"

class ReservaCreateView(CreateView):
    model = Reserva
    fields = ["habitacion", "pasajero"]
    success_url = '/reservas/'  # Redirige después de crear
    template_name = "reservas/reserva_form.html"

class ReservaDeleteView(DeleteView):
    model = Reserva
    success_url = '/reservas/'  # Redirige después de eliminar
    template_name = "reservas/reserva_confirm_delete.html"

# Vista principal protegida por login
@login_required
def home(request):
    return render(request, 'home.html')  # Página de inicio después de iniciar sesión
