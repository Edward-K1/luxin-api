import graphene
from graphene_django.types import DjangoObjectType
from api.models import LuxinUser

class LuxinUserType(DjangoObjectType):
    class Meta:
        model = LuxinUser

class LuxinUserQuery(object):
    all_users = graphene.List(LuxinUserType)

    def resolve_all_users(self, info, **kwargs):
        return LuxinUser.objects.all()
