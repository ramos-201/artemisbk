import graphene
from graphene import String


class Query(graphene.ObjectType):
    hello = String(default_value='Hello')
