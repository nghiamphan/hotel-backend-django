from django.urls import path
from . import views

urlpatterns = [
    path("hotels/", views.get_hotels),
    path("reservations/", views.get_reservations),
]
