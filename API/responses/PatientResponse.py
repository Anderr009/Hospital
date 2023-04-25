from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import  Response
from django.core.exceptions import ObjectDoesNotExist
from API.models import Cliente
from API.serializers.PatientSerializer import patientSerializerBasic

@api_view(['GET'])
def patientBasic(request,cedulaP):
    if request.method == 'GET':
        try:
            patient = Cliente.objects.get(cedula=cedulaP)
        except ObjectDoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        serializer = patientSerializerBasic(patient)
        return Response(serializer.data)