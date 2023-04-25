from rest_framework import serializers
from API.models import Cliente
class patientSerializerBasic(serializers.ModelSerializer):
    class Meta:
        model = Cliente
        fields = ['id','cedula','nombre1','nombre2','apellido1','apellido2','fecha_nacimiento','nacionalidad','tipo_sangre']