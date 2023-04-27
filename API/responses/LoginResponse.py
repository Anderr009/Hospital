from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import  Response
from django.core.exceptions import ObjectDoesNotExist
from API.models import Empleado
from API.serializers.LoginSerializer import LoginSerializer

@api_view(['GET'])
def LoginBasic(request,user,passw):
    if request.method == 'GET':
        try:
            emp = Empleado.objects.get(username=user)
        except ObjectDoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        serializer = LoginSerializer(emp)
        return Response(serializer.data)
