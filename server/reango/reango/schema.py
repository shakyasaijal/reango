import graphene


class Query(graphene.ObjectType):
    hello = graphene.String(default_value="Hi! Its Saijal.")
    pass

schema = graphene.Schema(query=Query)