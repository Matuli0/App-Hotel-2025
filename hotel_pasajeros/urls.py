from django.contrib import admin
from django.urls import path, include
from django.views.generic import RedirectView

urlpatterns = [
    path("admin/", admin.site.urls),
    # Redirige la raíz a /habitaciones/
    path("", RedirectView.as_view(url="habitaciones/", permanent=False)),
    path("", include("reservas.urls")),
]
