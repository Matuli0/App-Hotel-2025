from django.urls import path
from .views import (
    HabitacionListView, HabitacionCreateView,
    HabitacionUpdateView, HabitacionDeleteView
)
from .views import PasajeroListView
from .views import PasajeroCreateView
from .views import PasajeroUpdateView
from .views import PasajeroDeleteView
from .views import ReservaListView
from .views import ReservaCreateView
from .views import ReservaDeleteView
urlpatterns = [
    path("habitaciones/",                HabitacionListView.as_view(),   name="habitacion-list"),
    path("habitaciones/nueva/",          HabitacionCreateView.as_view(), name="habitacion-create"),
    path("habitaciones/<int:pk>/editar/",HabitacionUpdateView.as_view(), name="habitacion-edit"),
    path("habitaciones/<int:pk>/borrar/",HabitacionDeleteView.as_view(), name="habitacion-delete"),
    path("pasajeros/",             PasajeroListView.as_view(),   name="pasajero-list"),
    path("pasajeros/nuevo/",       PasajeroCreateView.as_view(), name="pasajero-create"),
    path("pasajeros/<int:pk>/editar/", PasajeroUpdateView.as_view(), name="pasajero-edit"),
    path("pasajeros/<int:pk>/borrar/", PasajeroDeleteView.as_view(), name="pasajero-delete"),
    path("reservas/",            ReservaListView.as_view(),   name="reserva-list"),
    path("reservas/nueva/",      ReservaCreateView.as_view(), name="reserva-create"),
    path("reservas/<int:pk>/borrar/", ReservaDeleteView.as_view(), name="reserva-delete"),
]
