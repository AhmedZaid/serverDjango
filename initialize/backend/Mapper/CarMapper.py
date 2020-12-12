from typing import List

import backend
from backend.ModelsDB.Car import Car
from backend.ModelsDomain.DomainCar import DomainCar


def requestToDomain(carRequest):
    carDomain = DomainCar()
    carDomain.carName = carRequest.get('name', '')
    carDomain.carId = carRequest.get('id', 0)
    return carDomain


def DomainToDB(car):
    carDomain = Car(pk=car.id, name=car.name)
    return carDomain


def DbToDomain(car):
    carDomain = DomainCar()
    carDomain.carName = car.name
    carDomain.carId = car.pk
    return carDomain.__dict__
