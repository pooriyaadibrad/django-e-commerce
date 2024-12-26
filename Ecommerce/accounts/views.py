from django.shortcuts import render, redirect, HttpResponse
from rest_framework.response import Response
from rest_framework.decorators import api_view
from . import models, serializers
from rest_framework import status


@api_view(['POST'])
def create_person(request):
    data = request.data
    serializer_data = serializers.PersonSerializer(data=data)
    if serializer_data.is_valid():
        serializer_data.save()
        return Response(serializer_data.data, status=status.HTTP_201_CREATED)
    else:
        return Response(status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET'])
def raed_person(request):
    persons = models.Person.objects.all()
    serializer = serializers.PersonSerializer(persons, many=True)
    return Response(serializer.data)


@api_view(['DELETE'])
def delete_person(request):
    pass


@api_view(['PUT'])
def update_person(request):
    pass
