from becados.models import Becado
from django.views.generic import DetailView, UpdateView
from rest_framework.response import Response
from .serializers import BecadoSerializer
from rest_framework.decorators import APIView, renderer_classes
from rest_framework.renderers import JSONRenderer, TemplateHTMLRenderer
#from becas.model import becas

'''class BecasDetailView(DetailView):
   model = 'becas'
   queryset = becas.objects.all()
   lookup_field = "area_de_interes", "grado_academico"
   
   def get_queryset(self):
      return self.request.filter("area_de_interes", "grado_academico")'''

class PerfilAPIView(UpdateView):
   model = 'Becado'
   serializer = BecadoSerializer
   
   def post (self, request):
      'nombre', 'apellido_paterno', 'apellido_materno', 'correo_electronico', 'area_de_interes', 'grado_academico', 'Estatus'
      return Response({"message": "Actualizado"})
        