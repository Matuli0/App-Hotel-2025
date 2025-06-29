from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from .models import Habitacion, Pasajero, Reserva
from .forms import ReservaForm
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import user_passes_test

# — Habitaciones
class HabitacionListView(ListView):
    model = Habitacion
    template_name = "reservas/habitacion_list.html"

class HabitacionCreateView(CreateView):
    model = Habitacion
    fields = ["numero", "capacidad", "orientacion"]
    success_url = reverse_lazy("habitacion-list")
    template_name = "reservas/habitacion_form.html"

class HabitacionUpdateView(UpdateView):
    model = Habitacion
    fields = ["capacidad", "orientacion"]
    success_url = reverse_lazy("habitacion-list")
    template_name = "reservas/habitacion_form.html"

class HabitacionDeleteView(DeleteView):
    model = Habitacion
    success_url = reverse_lazy("habitacion-list")
    template_name = "reservas/habitacion_confirm_delete.html"

# — Pasajeros
class PasajeroListView(ListView):
    model = Pasajero
    template_name = "reservas/pasajero_list.html"

class PasajeroCreateView(CreateView):
    model = Pasajero
    fields = ["nombre", "rut"]
    success_url = reverse_lazy("pasajero-list")
    template_name = "reservas/pasajero_form.html"

class PasajeroUpdateView(UpdateView):
    model = Pasajero
    fields = ["nombre", "rut"]
    success_url = reverse_lazy("pasajero-list")
    template_name = "reservas/pasajero_form.html"

class PasajeroDeleteView(DeleteView):
    model = Pasajero
    success_url = reverse_lazy("pasajero-list")
    template_name = "reservas/pasajero_confirm_delete.html"

# — Reservas
class ReservaListView(ListView):
    model = Reserva
    template_name = "reservas/reserva_list.html"

class ReservaCreateView(CreateView):
    model = Reserva
    form_class = ReservaForm  # Usa el formulario que hemos creado
    template_name = "reservas/reserva_form.html"
    success_url = reverse_lazy("reserva-list")  # Redirige a la lista de reservas tras crearla

class ReservaDeleteView(DeleteView):
    model = Reserva
    success_url = reverse_lazy("reserva-list")
    template_name = "reservas/reserva_confirm_delete.html"

# Vista principal protegida por login
@login_required
def home(request):
    return render(request, 'home.html')  # Página de inicio después de iniciar sesión

# Vista para el login (Usa la vista de login predeterminada de Django)
def admin_login(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('home')  # Redirigir al inicio después de login exitoso
            else:
                form.add_error(None, 'Usuario o contraseña incorrectos')
    else:
        form = AuthenticationForm()

    return render(request, 'admin/login.html', {'form': form})
