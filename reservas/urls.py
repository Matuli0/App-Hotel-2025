from django.urls import path
from .views import (
    HabitacionListView, HabitacionCreateView, HabitacionUpdateView, HabitacionDeleteView,
    PasajeroListView, PasajeroCreateView, PasajeroUpdateView,ReservaCreateView, PasajeroDeleteView,
    ReservaListView, ReservaCreateView, ReservaDeleteView,ReservaListView,ReservaUpdateView, home
)
from django.contrib.auth.views import LoginView  # Usando la vista de login predeterminada de Django

urlpatterns = [
    # Ruta de login (utilizando la vista predeterminada de Django)
    path('admin/login/', LoginView.as_view(template_name='admin/login.html'), name='admin_login'),

    # Ruta principal (home), protegida por login
    path('', home, name='home'),  # Si el usuario no está autenticado, será redirigido al login

    # Habitaciones
    path("habitaciones/", HabitacionListView.as_view(), name="habitacion-list"),
    path("habitaciones/nueva/", HabitacionCreateView.as_view(), name="habitacion-create"),
    path("habitaciones/<int:pk>/editar/", HabitacionUpdateView.as_view(), name="habitacion-edit"),
    path("habitaciones/<int:pk>/borrar/", HabitacionDeleteView.as_view(), name="habitacion-delete"),

    # Pasajeros
    path("pasajeros/", PasajeroListView.as_view(), name="pasajero-list"),
    path("pasajeros/nuevo/", PasajeroCreateView.as_view(), name="pasajero-create"),
    path("pasajeros/<int:pk>/editar/", PasajeroUpdateView.as_view(), name="pasajero-edit"),
    path("pasajeros/<int:pk>/borrar/", PasajeroDeleteView.as_view(), name="pasajero-delete"),

    # Reservas
    path("reservas/", ReservaListView.as_view(), name="reserva-list"),
    path("reservas/nueva/", ReservaCreateView.as_view(), name="reserva-create"),
    path("reservas/<int:pk>/borrar/", ReservaDeleteView.as_view(), name="reserva-delete"),
    path('reservas/nueva/', ReservaCreateView.as_view(), name='reserva-create'),
    path('reservas/', ReservaListView.as_view(), name='reserva-list'),
    path('reservas/<int:pk>/editar/', ReservaUpdateView.as_view(), name='reserva-edit'),
    path('reservas/<int:pk>/borrar/', ReservaDeleteView.as_view(), name='reserva-delete'),
]
