import imp
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.parsers import MultiPartParser, FormParser
from organizacion.models import Organizacion
from organizacion.serializers import OrgSerializer, OrgListSerializer


class OrgView(APIView):

    parser_classes = (MultiPartParser, FormParser)

    def get(self, request, format=None):
        orgs = Organizacion.objects.all()
        serializer = OrgSerializer(orgs, many=True)

        return Response(serializer.data,status=status.HTTP_200_OK)

    def post(self, request):
        
        serializer = OrgSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        return Response(serializer.data,status=status.HTTP_201_CREATED)

class OrgUpdateDeleteView(APIView):
    def get(self, request, id):
        orgs = Organizacion.objects.filter(id=id).first()
        if orgs is None:
            return Response({'error':'Bad request.'}, status=status.HTTP_400_BAD_REQUEST)
        serializer = OrgListSerializer(orgs)

        return Response(serializer.data,status=status.HTTP_200_OK)

    def patch(self, request, id):
        orgs = Organizacion.objects.filter(id=id).first()
        if orgs is None:
            return Response({'error':'Bad request.'}, status=status.HTTP_400_BAD_REQUEST)
        serializer = OrgSerializer(orgs, data=request.data,partial=True)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        return Response(serializer.data,status=status.HTTP_200_OK)
    
    def delete(self, request, id):
        orgs = Organizacion.objects.filter(id=id).first()
        if orgs is None:
            return Response({'error':'Bad request.'}, status=status.HTTP_400_BAD_REQUEST)
        orgs.delete()
        return Response({'message':'Institucion eliminada exitosamente.'},status=status.HTTP_200_OK)
