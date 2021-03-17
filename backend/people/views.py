# CLASS BASED VIEWS

from .models import People
from .serializers import PeopleSerializer
from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status


class PeopleList(APIView):
    def get(self, request, format=None):
        people = People.objects.all()
        serializer = PeopleSerializer(people, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = PeopleSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class PeopleDetail(APIView):
    def get_detail(self, pk):
        try:
            return People.objects.get(pk=pk)
        except People.DoesNotExist:
            return Http404

    def get(self, request, pk, format=None):
        people = self.get_detail(pk)
        serializer = PeopleSerializer(people)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        people = self.get_detail(pk)
        serializer = PeopleSerializer(people, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        people = self.get_detail(pk)
        people.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

# FUNCTION BASED VIEWS

# from rest_framework import status
# from rest_framework.response import Response
# from rest_framework.decorators import api_view
# from .models import People
# from .serializers import PeopleSerializer

# # We will be using @csrf_exempt decorator as we want to POST to this view from client that does not have CSRF token

# # @api_view decorator for working with function bases views
# # APIView class for working with class based views


# @api_view(['GET', 'POST'])
# # Allow only GET and POST request for this view function
# def people_list(request, format=None):
#     if request.method == 'GET':
#         people = People.objects.all()
#         serializer = PeopleSerializer(people, many=True)
#         return Response(serializer.data)

#     elif request.method == 'POST':
#         serializer = PeopleSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_200_OK)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# @api_view(['GET', 'PUT', 'DELETE'])
# # Allow only GET, PUT and DELETE for this view function
# def people_detail(request, pk, format=None):
#     try:
#         people = People.objects.get(pk=pk)
#     except People.DoesNotExist:
#         return Response(status=status.HTTP_404_NOT_FOUND)

#     if request.method == 'GET':
#         serializer = PeopleSerializer(people)
#         return Response(serializer.data)

#     elif request.method == 'PUT':
#         serializer = PeopleSerializer(people, data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

#     elif request.method == 'DELETE':
#         people.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)
