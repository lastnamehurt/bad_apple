import graphene

import apple.schema


class Query(apple.schema.Query, graphene.ObjectType):
    pass


schema = graphene.Schema(query=Query)
