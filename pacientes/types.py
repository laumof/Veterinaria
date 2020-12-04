from graphene_django import DjangoObjectType
from pacientes.models import Paciente

class PacienteType(DjangoObjectType):
    class Meta:
        model = Paciente
        only_fields = (
            'name',
            'size',
            'species',
            'race',
            'age',
            'color',
            'situation',
            'description',
            'owner',
            'phone1',
            'phone2',
            'dpi',
            'address',
            'admissionDate',
            'doctor',
            'departureDate',
            'cost',
        )
        use_connection = True
