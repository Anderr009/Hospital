from rest_framework import serializers
from API.models import Registro
class RegisterSerializer(serializers.ModelSerializer):
    class Meta:
        nombre9 = serializers.CharField(source='fk_cliente',read_only=True)
        model = Registro
        fields = ['cod_registro','motivo','fecha_llegada','fechahora_clasificacion','fechahora_final','enfermedad']