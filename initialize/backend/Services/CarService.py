import json

from django.http import HttpResponse

from backend.Mapper import CarMapper
from backend.ModelsDB.Car import Car


def get(request):
    cars = Car.objects.all()
    store_names = [{"name": car.name, "id": car.pk} for car in cars]
    # return HttpResponse(json.dumps(store_names), content_type='application/json')
    domainCars = [CarMapper.DbToDomain(car) for car in cars]
    return HttpResponse(json.dumps(domainCars), content_type='application/json')


def post(request):
    body = json.loads(request.body)
    domainCar = CarMapper.requestToDomain(body)
    dbCar = CarMapper.DomainToDB(domainCar)
    dbCar.save()
    return HttpResponse(json.dumps(None), content_type='application/json')


def update(request):
    body = json.loads(request.body)
    domainCar = CarMapper.requestToDomain(body)
    car = Car.objects.get(pk=domainCar.id)
    if car is not None:
        dbCar = CarMapper.DomainToDB(domainCar)
        dbCar.save()
    else:
        raise Exception()
    return HttpResponse(json.dumps(None), content_type='application/json')


def delete(request):
    body = json.loads(request.body)
    domainCar = CarMapper.requestToDomain(body)
    car = Car.objects.get(pk=domainCar.id)
    if car.pk != 0:
        car.delete()
    else:
        raise Exception()
    return HttpResponse(json.dumps(None), content_type='application/json')
