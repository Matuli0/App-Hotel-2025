from django.urls import path
from .views import (
    HabitacionListView, HabitacionCreateView, HabitacionUpdateView, HabitacionDeleteView,
    PasajeroListView, PasajeroCreateView, PasajeroUpdateView, PasajeroDeleteView,
    ReservaListView, ReservaCreateView, ReservaDeleteView, home, admin_login
)
from django.contrib.auth.views import LoginView  # Importar la vista de login de Django

urlpatterns = [
    # Redirige a la vista de login si no está autenticado
    path('admin/login/', LoginView.as_view(template_name='admin/login.html'), name='admin_login'),  # Usando la vista de login predeterminada de Django

    # Ruta principal (home), protegida por login
    path('', home, name='home'),  # Redirige a home después de login (cambiar a login si es necesario)

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
]
