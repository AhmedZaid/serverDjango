from django.views.decorators.csrf import csrf_exempt

from backend.Services import CarService


@csrf_exempt
def CarController(request):
    if request.method == 'GET':
        return CarService.get(request)
    if request.method == 'POST':
        return CarService.post(request)
    if request.method == 'PUT':
        return CarService.update(request)
    if request.method == 'DELETE':
        return CarService.delete(request)
