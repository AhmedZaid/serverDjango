from django.urls import path

from backend.Controllers import CarController
from backend.Services import CarService

urlpatterns = [
    path('cars/', CarController.CarController, name="slug")
]

