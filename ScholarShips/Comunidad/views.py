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
'''
class UpdateComunidad(APIView):
    def put(self, request, pk, format=None):
        comunidad = Comunidad.objects.get(pk=pk)
        serializer = ComunidadSerializer(comunidad, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

'''
class DeleteComunidad(APIView):
    def delete(self, request, pk, format=None):
        comunidad = Comunidad.objects.get(pk=pk)
        comunidad.delete()
        return Response({'message':'Eliminado con exito'}, status=status.HTTP_204_NO_CONTENT)


