import graphene
from graphene_django.types import DjangoObjectType

from apple.models import BadApple


class BadAppleType(DjangoObjectType):
    class Meta:
        model = BadApple


class Query(object):
    all_bad_apples = graphene.List(BadAppleType)

    bad_apple = graphene.Field(BadAppleType,
                               id=graphene.Int(),
                               first_name=graphene.String(),
                               last_name=graphene.String())

    def resolve_all_bad_apples(self, info, **kwargs):
        return BadApple.objects.all()

    def resolve_bad_apple(self, info, **kwargs):
        return BadApple.objects.get(id=kwargs.get('id', None))
