import graphene
from graphene import relay, ObjectType
from graphene_django import DjangoObjectType
from graphene_django.filter import DjangoFilterConnectionField


from pacientes.models import Paciente


class PacienteNode(DjangoObjectType):
    class Meta:
        model = Paciente
        filter_fields = {
            'name': ['exact', 'icontains', 'istartswith'],
            'size': ['exact', 'icontains'],
            'species': ['exact', 'icontains'],
            'race': ['exact', 'icontains'],
            'age': ['exact', 'icontains'],
            'color': ['exact', 'icontains'],
            'situation': ['exact', 'icontains'],
            'description': ['exact', 'icontains'],
            'owner': ['exact', 'icontains'],
            'phone1': ['exact', 'icontains'],
            'phone2': ['exact', 'icontains'],
            'dpi': ['exact', 'icontains'],
            'address': ['exact', 'icontains'],
            'admissionDate': ['exact', 'icontains'],
            'doctor': ['exact', 'icontains'],
            'departureDate': ['exact', 'icontains'],
            'cost': ['exact', 'icontains'],

        }
        interfaces = (relay.Node, )


class Query(graphene.ObjectType):

    paciente = relay.Node.Field(PacienteNode)
    all_pacientes = DjangoFilterConnectionField(PacienteNode)
