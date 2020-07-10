import graphene

from .user.schema import LuxinUserQuery

class Query(LuxinUserQuery, graphene.ObjectType):
    pass

schema = graphene.Schema(query=Query)