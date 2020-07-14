import graphene

from .user.schema import LuxinUserQuery
from .assessment.schema import AssessmentQuery


class Query(LuxinUserQuery, AssessmentQuery, graphene.ObjectType):
    pass


schema = graphene.Schema(query=Query)
