from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from .models import People
from .serializers import PeopleSerializer

# We will be using @csrf_exempt decorator as we want to POST to this view from client that does not have CSRF token


@csrf_exempt
def people_list(request):
    if request.method == 'GET':
        people = People.objects.all()
        serializer = PeopleSerializer(people, many=True)
        return JsonResponse(serializer.data, safe=False)

    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = PeopleSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)


@csrf_exempt
def people_detail(request, pk):
    try:
        people = People.objects.get(pk=pk)
    except People.DoesNotExist:
        return HttpResponse(status=404)

    if request.method == 'GET':
        serializer = PeopleSerializer(people)
        return JsonResponse(serializer.data)

    elif request.method == 'PUT':
        data = JSONParser().parse(request)
        serializer = PeopleSerializer(people, data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data)
        return JsonResponse(serializer.errors, status=400)

    elif request.method == 'DELETE':
        people.delete()
        return HttpResponse(status=204)
