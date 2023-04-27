from rest_framework import serializers
from API.models import Empleado 

class LoginSerializer(serializers.ModelSerializer):
    class Meta:
        model = Empleado
        fields=['id','username','passw']