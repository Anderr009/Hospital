from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view
from django.core.exceptions import ObjectDoesNotExist
from API.models import Registro,Cliente
from API.serializers.RegisterSerializer import RegisterSerializer

@api_view(['GET','POST'])
def RegisterFull(request,idC):
    if request.method == 'GET':
        try:
            cl = Cliente.objects.get(id=idC)
            reg = Registro.objects.select_related('fk_cliente','fk_empleado').filter(fk_cliente=idC)
        except ObjectDoesNotExist:
            return Response({'Mensaje':'No existe'},status=status.HTTP_404_NOT_FOUND)
        serializer = RegisterSerializer(reg,many=True)
        return Response(serializer.data,status=status.HTTP_200_OK)