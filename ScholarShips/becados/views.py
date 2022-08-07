from becados.models import Becado
from django.views.generic import DetailView, UpdateView
from rest_framework.response import Response
from .serializers import BecadoSerializer
#from becas.model import becas

class BecasDetailView(DetailView):
   context_object_name = 'becas'
   queryset = becas.objects.all()
   lookup_field = "area_de_interes", "grado_academico"
   
   def get_queryset(self):
      return self.request.filter("area_de_interes", "grado_academico")
   
class PerfilView(UpdateView):
   context_object_name = 'Becado'
   serializer = BecadoSerializer
   
   def post ():
      'nombre', 'apellido_paterno', 'apellido_materno', 'correo_electronico'