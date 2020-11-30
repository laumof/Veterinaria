import graphene

import pacientes.schema


class Query(pacientes.schema.Query, graphene.ObjectType):
    pass

schema = graphene.Schema(query=Query)
