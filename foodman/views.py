from django.http import JsonResponse
from django.views.decorators.http import require_http_methods
from foodman.models import Meals


@require_http_methods(["GET"])
def get_meals(request):
    data = list()

    for meal in Meals.objects.all():
        data.append({'name': meal.name, 'date': meal.date})

    return JsonResponse({'meals': data})
