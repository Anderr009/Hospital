from django.urls import path
from .responses.PatientResponse import patientBasic
urlpatterns = [
    path('PatientBasic/<str:cedulaP>',patientBasic)#http://127.0.0.1:8000/API/PatientBasic/cedula
]