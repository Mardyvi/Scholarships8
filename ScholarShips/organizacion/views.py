import imp
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.parsers import MultiPartParser, FormParser
from organizacion.models import Organizacion
from organizacion.serializers import OrgSerializer


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


