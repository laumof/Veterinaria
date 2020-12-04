from graphene import Boolean, Field, ID, InputObjectType, Mutation, String
from rest_framework import serializers
from pacientes.models import Paciente
from pacientes.types import PacienteType



class PacienteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Paciente
        fields = (
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


class PacienteInputType(InputObjectType):
    name = String()
    size = String()
    species = String()
    race = String()
    age = String()
    color = String()
    situation = String()
    description = String()
    owner = String()
    phone1 = String()
    phone2 = String()
    dpi = String()
    address = String()
    admissionDate = String()
    doctor = String()
    departureDate = String()
    cost = String()


class PacienteCreate(Mutation):
    class Arguments:
        input = PacienteInputType(required=True)

    paciente = Field(PacienteType)

    @classmethod
    def mutate(cls, root, info, **data):
        serializer = PacienteSerializer(data=data.get('input'))
        serializer.is_valid(raise_exception=True)

        return PacienteCreate(paciente=serializer.save())


class PacienteDelete(Mutation):
    class Arguments:
        id = ID(required=True)

    ok = Boolean()

    @classmethod
    def mutate(cls, root, info, **data):
        paciente = Paciente.objects.get(id=data.get('id'))
        paciente.delete()

        return PacienteDelete(ok=True)
