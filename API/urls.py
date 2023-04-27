from django.urls import path
from .responses.PatientResponse import patientBasic
from .responses.LoginResponse import LoginSerializer
urlpatterns = [
    path('PatientBasic/<str:cedulaP>',patientBasic),#http://127.0.0.1:8000/API/PatientBasic/cedula
    path('loginBasic/<str:user>/<str:passw>',LoginSerializer),
]