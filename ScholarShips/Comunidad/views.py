from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from Comunidad.models import Comunidad #modelo
from Comunidad.serializer import ComunidadSerializer #serializer

# Create your views here.
class ComunidadView(APIView):
    def post(self, request):
        serializer = ComunidadSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)

    
class ListComunidad(APIView):
    def get(self, request):
        '''QuerySet --> Resulatdo de una Query. Lista de objetos'''
        comunidad = Comunidad.objects.all()
        print(comunidad)
        serializer = ComunidadSerializer(comunidad, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
