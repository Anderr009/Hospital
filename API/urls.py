from django.urls import path
from .responses.PatientResponse import patientBasic
from .responses.LoginResponse import LoginBasic
from .responses.RegisterResponse import RegisterFull
urlpatterns = [
    path('PatientBasic/<str:cedulaP>',patientBasic),#http://127.0.0.1:8000/API/PatientBasic/cedula
    path('loginBasic/<str:usern>/<str:passw>',LoginBasic),#http://127.0.0.1:8000/API/loginBasic/username/pass
    path('RegisterClient/<int:idC>', RegisterFull),#http://127.0.0.1:8000/API/RegisterClient/ID
]