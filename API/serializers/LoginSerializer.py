from rest_framework import serializers
from API.models import Empleado,Cargo
#Serializador de cargos para saber el nivel de usuario
class CargosSerializer(serializers.ModelSerializer):
    class Meta:
        model=Cargo
        fields=['nombre']
#Serializador de login basico donde se brindaran datos para validar el login de un user
class LoginSerializer(serializers.ModelSerializer):
    cargo = serializers.CharField(source='fk_cargo.nombre',read_only=True)
    class Meta:
        model = Empleado
        fields=['id','username','passw','cargo','niv_user']
