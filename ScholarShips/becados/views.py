from becados.models import Becado
from django.views.generic import DetailView
from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import BecadoSerializer
from django.http import HttpResponse
from rest_framework import status
#from becas.model import becas

'''class BecasDetailView(DetailView):
   model = 'becas'
   queryset = becas.objects.all()
   lookup_field = "area_de_interes", "grado_academico"
   
   def get_queryset(self):
      return self.request.filter("area_de_interes", "grado_academico")'''

class PerfilAPIView(APIView):
    def post(self, request):
        serializer = BecadoSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
        