import graphene
import pacientes.schema
from graphene import relay, ObjectType
from pacientes.mutations import Paciente, PacienteCreate, PacienteDelete
from graphene import Argument, Field, ID, ObjectType, Schema
from graphene_django import DjangoConnectionField
from graphene_django.filter import DjangoFilterConnectionField
from pacientes.models import Paciente
from pacientes.types import PacienteType
from pacientes.filters import PacienteFilter

class Query(pacientes.schema.Query, graphene.ObjectType):
    pass

class Mutation(graphene.ObjectType):
    paciente_create = PacienteCreate.Field()
    paciente_delete = PacienteDelete.Field()

class Query(ObjectType):
    pacientes = DjangoFilterConnectionField(PacienteType, filterset_class=PacienteFilter)

class Query(ObjectType):

    pacientes = DjangoConnectionField(PacienteType)
    paciente = Field(PacienteType, id=Argument(ID, required=True))

    def resolve_pacientes(root, info, **kwargs):
        return Paciente.objects.all()
    def resolve_paciente(root, info, **kwargs):
        return Paciente.objects.get(id=kwargs.get('id'))


schema = graphene.Schema(query=Query, mutation=Mutation)
